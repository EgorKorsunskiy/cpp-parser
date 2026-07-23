class InfixExprNode:
    def __init__(self, tok=None, left=None, right=None) -> None:
        self.tok = tok
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return f"{self.tok} {self.left} {self.right}"

class PrefixExprNode:
    def __init__(self, tok=None, right=None) -> None:
        self.tok = tok
        self.right = right
    def __repr__(self) -> str:
        return f"{self.tok} {self.right}"

class CallExprNode:
    def __init__(self, tok=None, params=None) -> None:
        self.tok = tok
        self.params = params
    def __repr__(self) -> str:
        return f"{self.tok} {" ".join(str(param for param in self.params))}"

class ProgrammeNode:
    def __init__(self) -> None:
        self.stmts = []
    def __str__(self) -> str:
        return "\n\n".join(str(stmt) for stmt in self.stmts)

class InitStmt:
    def __init__(self) -> None:
        self.type = None
        self.name = None
        self.value = None
    def __repr__(self) -> str:
        return f"type: {self.type}\n name: {self.name}\n value: {self.value}\n"

class LoopStmt:
    def __init__(self) -> None:
        self.condition = None
        self.body = []
    def __repr__(self) -> str:
        return f"condition: {self.condition}\n {"\n".join(str(stmt) for stmt in self.body)}\n"

class ConditionStmt:
    def __init__(self) -> None:
        self.condition = None
        self.thenBody = []
    def __repr__(self) -> str:
        return f"{self.condition}\n {"\n".join(str(stmt) for stmt in self.thenBody)}\n"

class IfStmt(ConditionStmt):
    def __init__(self) -> None:
        super().__init__()
        self.rejectBody = []
        self.alternatives: ConditionStmt = []
    def __repr__(self) -> str:
        base = super().__repr__()
        return f"{base}{"\n".join(str(stmt) for stmt in self.rejectBody)}\n {"\n".join(str(stmt) for stmt in self.alternatives)}\n"

class FuncStatement:
    def __init__(self) -> None:
        self.type = None
        self.name = None
        self.args = []
        self.body = []
    def __repr__(self) -> str:
        return f"{self.type}\n {self.name}\n {" ".join(str(arg) for arg in self.args)} {"\n".join(str(stmt) for stmt in self.body)}"
