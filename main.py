from lexer.main import Lexer
from parser.main import Parser

FRAGMENT = """
    if(5<6) {
        int i = 0;
    }
    else if(10 > 6 || 8 > 0) {
        float i = 2;
    }
    else if(1) {
        float i = 2;
    }
    else {
        int i = 1;
    }
"""

def main():
    lexer = Lexer()
    tokens = lexer.parse(FRAGMENT)
    tokens = lexer.merge_coupled_tokens(tokens)
    parser = Parser()
    ast = parser.parse(tokens)
    print(ast)
if __name__ == "__main__":
    main()
