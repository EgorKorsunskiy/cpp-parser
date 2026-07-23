from typing import List, Tuple
from lexer.token_lists import TokenTypes
from parser.ast_entities import CallExprNode, InfixExprNode, PrefixExprNode
from utils.main import getTokenType

PREFIX = 100
LOWEST = 0

# Parser for expressions
class PrattParser:
    def __init__(self):
        self.infixParseFnc = {}
        self.prefixParseFnc = {}

        self.prefixParseFnc[TokenTypes.MIN] = self.parsePrefixExpr
        self.prefixParseFnc[TokenTypes.NOT] = self.parsePrefixExpr
        self.prefixParseFnc[TokenTypes.IDENT] = self.parsePrefixExpr
        self.prefixParseFnc[TokenTypes.LPAREN] = self.parseGroupedExpr
        self.prefixParseFnc[TokenTypes.CALL] = self.parseCallExpr

        self.infixParseFnc[TokenTypes.PLUS] = self.parseInfixExpr
        self.infixParseFnc[TokenTypes.MIN] = self.parseInfixExpr
        self.infixParseFnc[TokenTypes.MUL] = self.parseInfixExpr
        self.infixParseFnc[TokenTypes.DIVIDE] = self.parseInfixExpr
        self.infixParseFnc[TokenTypes.GTE] = self.parseInfixExpr
        self.infixParseFnc[TokenTypes.LTE] = self.parseInfixExpr
        self.infixParseFnc[TokenTypes.GT] = self.parseInfixExpr
        self.infixParseFnc[TokenTypes.LT] = self.parseInfixExpr
        self.infixParseFnc[TokenTypes.EQ] = self.parseInfixExpr

        self.size = None
        self.cursor = None
        self.expr = None

    def parseCallExpr(self):
        currToken = self.pick()
        params = []
        while getTokenType(self.pick()) != TokenTypes.RPAREN:
            expr = self.parseExpr(LOWEST)
            params.append(expr)
            self.next()
        self.next()

        return CallExprNode(currToken, params)

    def parseGroupedExpr(self):
        self.next()

        expr = self.parseExpr(LOWEST) # "sucks" everything inside braces
        # There is no infix function for RBRACE so parseExpr will terminate after its appearance
        self.next()

        return expr


    def parsePrefixExpr(self):
        currToken = self.pick()
        self.next()
        
        right = self.expand_expr(PREFIX)
        return PrefixExprNode(currToken, right)

    def parseInfixExpr(self, left):
        token = self.pick()
        bp = self.getInfixBindingPower(getTokenType(token))
        self.next()

        right = self.parseExpr(bp)

        return InfixExprNode(token, left, right)


    def setExpr(self, expr: List):
        self.size = len(expr)
        self.cursor = 0
        self.expr = expr
    
    def next(self):
        self.cursor += 1

    def getTokensLeft(self):
        return self.cursor < self.size

    def pick(self):
        return self.expr[self.cursor]

    def parseExpr(self, min_bp):
        if not self.getTokensLeft():
            return None
        prefixFunc = self.prefixParseFnc[getTokenType(self.pick())]
        left = prefixFunc()
        self.next()
        currToken = getTokenType(self.pick)
        if currToken not in self.infixParseFnc:
                return left
        bp = self.getInfixBindingPower(currToken)
        while self.getTokensLeft() and bp > min_bp:
            infixFunc = self.infixParseFnc[currToken]
            left = infixFunc(left) 

        return left
        

    def getInfixBindingPower(self, op: TokenTypes) -> Tuple[int,int]:
        match op:
            case TokenTypes.PLUS | TokenTypes.MIN:
                return 3
            case TokenTypes.MUL | TokenTypes.DIVIDE:
                return 4
            case TokenTypes.LTE | TokenTypes.GTE | TokenTypes.EQ | TokenTypes.LT | TokenTypes.GT:
                return 5
            case _:
                return LOWEST