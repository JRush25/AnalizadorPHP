import ply.lex as lex
# List of token names.   This is always required
reserved = {
#Joselyne Torres (inicio)
    'if' : 'IF',
    'elseif' : 'ELSEIF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'while' : 'WHILE',
    'and' : 'AND',
    'or' : 'OR',
    'try' : 'TRY',
    'catch' : 'CATCH',
    'echo' : 'ECHO',
    'array' : 'ARRAY',
    'print': 'PRINT',
    'sort' : 'SORT',
    'Exception' : 'EXCEPTION',
    'return' : 'RETURN',
     #Joselyne Torres (fin)
     #David Cevallos Inicio
    'do' : 'DO',
    'function' : 'FUNCTION',
   #David Cevallos fin
    'array_map' : 'ARRAY_MAP',
    'insert' : 'INSERT'





}
tokens = (
    'NUMBER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MOD',
    'ID',
#Joselyne Torres (inicio)
    'MENOR',
    'MAYOR',
    'ASIGNACION',
    'REF',
    'CADENA',
    'BOOLEANT',
    'BOOLEANF',
    'INICIO',
    'FIN',
    'PCOMA',
    'LLLAVE',
    'RLLAVE',
    'IGUAL',
    'MENORIGUAL',
    'MAYORIGUAL',
    'COMA',
    'NFUNCION',
    'INCREMENTO',
     #David Cevallos Inicio

    'DECREMENTO',
    'IS_NOT_EQUAL',
    'DOUBLE_ARROW', #David Cevallos Final
    'LCORCH',
    'RCORCH',
    'SINGLEARROW'

#Joselyne Torres (fin)
) + tuple(reserved.values())
# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'%'
t_MENOR = r'<'
t_MAYOR = r'>'
t_ASIGNACION = r'='
t_REF = r'=\s\&'
t_INCREMENTO = r'\+\+'
t_INICIO = r'<\?php'
t_FIN = r'\?>'
t_PCOMA = r';'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_IGUAL = r'=='
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_COMA = r','
  #David Cevallos Inicio

t_DECREMENTO= r'\-\-'
t_IS_NOT_EQUAL= r'\!\='
t_DOUBLE_ARROW= r'\=\>'  #David Cevallos Fin
t_LCORCH= r'\['
t_RCORCH= r'\]'
t_SINGLEARROW = r'->'


#Joselyne Torres (inicio)
def t_ID(t):
    r'\$[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


# A regular expression rule with some action code
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CADENA(t):
    r'\'[\w\W\s]*\'|"[\w\W\s]*\"'
    t.value = str(t.value)
    return t
def t_BOOLEANT(t):
    r'(True)'
    t.type = reserved.get(t.value, 'BOOLEANT')
    t.value = bool(t.value)
    return t
def t_BOOLEANF(t):
    r'(False)'
    t.type = reserved.get(t.value, 'BOOLEANF')
    t.value = bool(t.value)
    return t
def t_NFUNCION(t):
    r'[a-zA-Z]\w*'
    t.type = reserved.get(t.value, 'NFUNCION')  # Check for reserved words
    return t
def t_IF(t):
    r'if'
    return t
def t_ELSEIF(t):
    r'elseif'
    return t
def t_ELSE(t):
    r'else'
    return t
def t_ARRAY(t):
    r'array'
    return t
def t_SORT(t):
    r'sort'
    return t
def t_WHILE(t):
    r'while'
    return t
def t_FOR(t):
    r'for'
    return t
def t_AND(t):
    r'(and|\&\&)'
    return t
def t_OR(t):
    r'(or|\|\|)'
    return t

def t_TRY(t):
    r'try'
    return t
def t_EXCEPTION(t):
    r'exception'
    return t
def t_RETURN(t):
    r'return'
    return t
def t_CATCH(t):
    r'catch'
    return t

def t_ECHO(t):
    r'echo'
    return t

#Joselyne Torres (fin)

 #David Cevallos Inicio

def t_DO(t):
    r'do'
    return t

def t_FUNCTION(t):
  r'function'
  return t

#David Cevallos Fin
def t_ARRAY_MAP(t):
    r'array_map'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_COMMENT(t):
    r'\/\/.*'
    pass




# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
# Build the lexer
lexer = lex.lex()
'''
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
'''
def analizar(data):
    lexer.input(data)
    arr = []
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        arr.append(tok)
    return arr

