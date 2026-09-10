"""Data-preparation helpers. No cell, pack, or vehicle simulator is implemented."""
from __future__ import annotations
import ast
import csv
import hashlib
import json
import math
import operator
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8", newline="\n")

def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        raise ValueError("Refusing a CSV with unknown columns")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

def git_blob_sha1(payload: bytes) -> str:
    prefix = b"blob " + str(len(payload)).encode("ascii") + b"\0"
    return hashlib.sha1(prefix + payload).hexdigest()

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def safe_destination(root: Path, relative: str) -> Path:
    rel = Path(relative)
    if rel.is_absolute() or ".." in rel.parts or "\\" in relative:
        raise ValueError("Unsafe destination")
    dest = (root / rel).resolve()
    if not dest.is_relative_to(root.resolve()):
        raise ValueError("Destination escapes root")
    return dest

def discharge_positive(current: float, original_positive: str) -> float:
    if original_positive not in {"charge", "discharge"}:
        raise ValueError("Explicit source current convention is required")
    if not math.isfinite(current):
        raise ValueError("Current must be finite")
    return -current if original_positive == "charge" else current

def celsius_to_kelvin(value: float) -> float:
    result = value + 273.15
    if not math.isfinite(result) or result <= 0:
        raise ValueError("Invalid absolute temperature")
    return result

def sample_expression(expression: str, x: float, low: float, high: float) -> float:
    """Evaluate a whitelisted scalar fit inside a declared domain; never use eval."""
    if not (math.isfinite(x) and low <= x <= high):
        raise ValueError("Outside declared source domain")
    if len(expression) > 4096:
        raise ValueError("Expression too long")
    tree = ast.parse(expression, mode="eval")
    if len(list(ast.walk(tree))) > 500:
        raise ValueError("Expression too complex")
    binary = {ast.Add: operator.add, ast.Sub: operator.sub,
              ast.Mult: operator.mul, ast.Div: operator.truediv}
    functions = {"exp": math.exp, "tanh": math.tanh}
    def visit(node: ast.AST) -> float:
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return float(node.value)
        if isinstance(node, ast.Name) and node.id == "x":
            return x
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            return visit(node.operand) * (-1 if isinstance(node.op, ast.USub) else 1)
        if isinstance(node, ast.BinOp):
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Pow):
                if abs(right) > 32:
                    raise ValueError("Exponent exceeds allowed evaluation budget")
                result = left ** right
                if isinstance(result, complex):
                    raise ValueError("Complex result is not a scalar material fit")
                return float(result)
            if type(node.op) in binary:
                return binary[type(node.op)](left, right)
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id in functions and len(node.args) == 1 and not node.keywords):
            return functions[node.func.id](visit(node.args[0]))
        raise ValueError("Unsupported or unsafe expression node")
    result = visit(tree)
    if not math.isfinite(result):
        raise ValueError("Nonfinite fit result")
    return result
