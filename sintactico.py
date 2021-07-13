import ply.yacc as yacc
from lexico import tokens
# Diccionario de Sentencias
senten = { }
listas = { }

#JoselyneTorres_inicio
def p_programa(p):
    'programa : INICIO sentencias FIN'
    pass


def p_sentencias(p):
    '''sentencias : asignacion
                    | comparacion
                    | funcion
                    | impresion
                    | repeticion
                    | expresion
                    | excepcion
                    | estdatos
    '''


def p_asignacion(p):
    '''asignacion : ID ASIGNACION valor PCOMA
                | ID REF ID PCOMA
                | ID ASIGNACION estdatos PCOMA
                | ID ASIGNACION expresion PCOMA'''

    print ("Se asigno el valor %s a %s"%(p[3],p[1]))


def p_valor(p):
    '''valor : ID
            | NUMBER
            | BOOLEAN
            | CADENA'''
    p[0] = p[1]

def p_opcomparacion(p):
    '''opcomparacion : IGUAL
                    | MAYOR
                    | MENOR
                    | MAYORIGUAL
                    | MENORIGUAL '''
    p[0] = p[1]

def p_expresioncmp(p):
    '''expcmp : valor opcomparacion valor
            | LPAREN valor opcomparacion valor RPAREN oplog LPAREN valor opcomparacion valor RPAREN
            | LPAREN valor opcomparacion valor RPAREN oplog LPAREN valor opcomparacion valor RPAREN oplog expcmp'''


def p_expresioncmplog(p):
    ''' expcmplog : expcmp oplog expcmp
                | expcmp oplog expcmplog'''


def p_oplog(p):
    '''oplog : BOOLEAN_OR
            | BOOLEAN_AND
            | AND
            | OR'''
    p[0] = p[1]


def p_comparacionif(p):
    '''comparacion : IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE
                    | IF LPAREN expcmplog RPAREN LLLAVE sentencias RLLAVE'''


def p_comparacionif_else(p):
    '''comparacion : IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE ELSE LLLAVE sentencias RLLAVE'''

def p_comparacionif_elseif_else(p):
    '''comparacion : IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE ELSEIF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE ELSE LLLAVE sentencias RLLAVE '''

def p_array(p):
    '''array : ARRAY LPAREN valor DOUBLE_ARROW valor RPAREN
            | ARRAY LPAREN valor RPAREN'''


def p_sort(p):
    'sort : SORT LPAREN ID RPAREN PCOMA'

def p_estdatos(p):
    '''estdatos : array
                | array_map
                | heap'''

def p_expresionmat(p):
    '''expresionmat : NUMBER operadormat NUMBER'''

    if p[2] == '+':
        p[0] = p[1] + p[3]
        #print(p[0])
    elif p[2] == '-':
        p[0] = p[1] - p[3]
        #print(p[0])
    elif p[2] == '*':
        p[0] = p[1] * p[3]
        #print(p[0])
    elif p[2] == '/':
        p[0] = p[1] / p[3]
        #print(p[0])

def p_operadormat_plus(p):
    '''operadormat : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE'''
    p[0] = p[1]

def p_expresion(p):
    '''expresion : expresionmat
                | expcmplog'''
def p_funcion(p):
    'funcion : sort'

def p_funciondef(p):
    '''funcion : FUNCTION NFUNCION ID LPAREN args RPAREN LLLAVE sentencias RLLAVE
            | FUNCTION NFUNCION ID LPAREN args RPAREN LLLAVE sentencias RETURN valor PCOMA RLLAVE'''


def p_args(p):
    '''args : ID
            | ID args'''

def p_excepcion(p):
    '''excepcion : TRY LLLAVE sentencias RLLAVE CATCH LPAREN EXCEPTION ID RPAREN LLLAVE ECHO CADENA COMA ID FLECHA GETMESSAGE RLLAVE'''

#JoselyneTorres_fin

def p_impresion(p):
 '''impresion : ECHO valor PCOMA
             | PRINT valor PCOMA
             | PRINT expresionmat PCOMA'''
 print(p[2])

def p_repeticioncompfor(p):
  '''repeticionrep : MAYOR
                  | MENOR
                  | MAYORIGUAL
                  | MENORIGUAL '''
  p[0] = p[1]
def p_actualizar(p):
  '''actualizar : INCREMENTO
                | DECREMENTO
  '''

def p_repeticionfor(p):
  'repeticion : FOR LPAREN ID ASIGNACION NUMBER PCOMA ID repeticionrep NUMBER PCOMA ID actualizar RPAREN LLLAVE sentencias RLLAVE'



def p_repeticionwhile(p):
  '''repeticion : WHILE LPAREN ID opcomparacion valor RPAREN LLLAVE sentencias ID actualizar PCOMA RLLAVE
                  | DO LLLAVE sentencias ID actualizar PCOMA RLLAVE WHILE LPAREN ID opcomparacion valor RPAREN PCOMA
  '''

def p_array_map(p):
    'array_map : ARRAY_MAP LPAREN funcion COMA array RPAREN PCOMA'

def p_heap(p):
    '''heap : INSERT LPAREN LCORCH NUMBER COMA NUMBER RCORCH RPAREN PCOMA
                | INSERT LPAREN ARRAY LPAREN valor DOUBLE_ARROW NUMBER RPAREN RPAREN PCOMA'''
    print ("Heap creado, se ha insertado el %s en %s" %(p[6],p[4]))



# Error rule for syntax errors
def p_expression_name(p):
    'expression : ID'
    try:
        p[0] = senten[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0
def p_error(p):
    print("Syntax error at '%s'" %p.value)

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
