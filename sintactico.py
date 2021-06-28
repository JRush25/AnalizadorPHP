import ply.yacc as yacc
from lexico import tokens

def p_programa(p):
    'programa : INICIO sentencias FIN'
    pass
def p_sentencias(p):
    '''sentencias : asignacion
                    | comparacion'''

def p_asignacion(p):
    '''asignacion : ID ASIGNACION valor PCOMA
                | ID REF ID PCOMA'''
def p_valor(p):
    '''valor : ID
             | NUMBER
             | CADENA
             | BOOLEAN
    '''

def p_opcomparacion(p):
    '''opcomparacion : IGUAL
                    | MAYOR
                    | MENOR
                    | MAYORIGUAL
                    | MENORIGUAL
    '''

def p_expresioncmp(p):
    'expcmp : valor opcomparacion valor'

def p_comparacionif(p):
    'comparacion : IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE'



# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
