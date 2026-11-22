"""Safe AST-Based Scientific Calculator (No unsafe eval!)"""
import ast, math, operator

OPS = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
    ast.Div: operator.truediv, ast.Pow: operator.pow, ast.Mod: operator.mod,
}
FUNCS = {"sin": math.sin, "cos": math.cos, "tan": math.tan, "sqrt": math.sqrt, "log": math.log10, "ln": math.log}
CONSTS = {"pi": math.pi, "e": math.e}

def _eval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)): return node.value
    if isinstance(node, ast.Name) and node.id in CONSTS: return CONSTS[node.id]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub): return -_eval(node.operand)
    if isinstance(node, ast.BinOp) and type(node.op) in OPS: return OPS[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in FUNCS:
        return FUNCS[node.func.id](*[_eval(a) for a in node.args])
    raise ValueError("Unsupported expression")

def calculate(expr: str) -> float:
    return round(float(_eval(ast.parse(expr, mode="eval").body)), 6)

if __name__ == "__main__":
    for ex in ["sqrt(144) + 2**5", "sin(pi / 2) * 100", "log(1000)"]:
        print(f"{ex} = {calculate(ex)}")
