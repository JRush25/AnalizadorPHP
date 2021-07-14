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
    'include' : 'INCLUDE',
    'try' : 'TRY',
    'catch' : 'CATCH',
    'abstract' : 'ABSTRACT',
    'declare' : 'DECLARE',
    'echo' : 'ECHO',
    'public' :'PUBLIC',
    'private' : 'PRIVATE',
    'protected': 'PROTECTED',
    'array' : 'ARRAY',
    'getMessage' : 'GETMESSAGE',
    'print': 'PRINT',
    'sort' : 'SORT',
    'Exception' : 'EXCEPTION',
    'return' : 'RETURN',
    'const' : 'CONST', #Joselyne Torres (fin)
    'case' : 'CASE', #David Cevallos Inicio
    'break' : 'BREAK',
    'class' : 'CLASS',
    'continue': 'CONTINUE',
    'default' : 'DEFAULT',
    'do' : 'DO',
    'extends' : 'EXTENDS',
    'final' : 'FINAL',
  'function' : 'FUNCTION',
  'global' : 'GLOBAL',
  'instanceof' : 'INSTANCEOF', #David Cevallos fin
    'array_map' : 'ARRAY_MAP',
    'heap' : 'HEAP',
    'insert' : 'INSERT'





}
tokens = (
    'NUMBER',
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
    'BOOLEAN',
    'INICIO',
    'FIN',
    'PCOMA',
    'LLLAVE',
    'RLLAVE',
    'IGUAL',
    'MENORIGUAL',
    'MAYORIGUAL',
    'COMA',
    'FLECHA',
    'NFUNCION',
    'INCREMENTO',
     #David Cevallos Inicio

    'COMMENT',
    'CONCAT_EQUAL',
    'DECREMENTO',
    'DIV_EQUAL',
    'IS_NOT_EQUAL',
    'DOUBLE_ARROW', #David Cevallos Final
    'LCORCH',
    'RCORCH'

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
t_REF = r'=\&'
t_INCREMENTO = r'\+\+'
t_INICIO = r'<\?php'
t_FIN = r'\?>'
t_PCOMA = r';'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_IGUAL = r'=='
t_FLECHA = r'\-\>'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_COMA = r','
  #David Cevallos Inicio

t_COMMENT=r'\#'
t_CONCAT_EQUAL=r'\.\='
t_DECREMENTO= r'\-\-'
t_DIV_EQUAL= r'\/\='
t_IS_NOT_EQUAL= r'\!\='
t_DOUBLE_ARROW= r'\=\>'  #David Cevallos Fin
t_LCORCH= r'\['
t_RCORCH= r'\]'


#Joselyne Torres (inicio)
def t_ID(t):
    r'\$[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_NFUNCION(t):
    r'[a-zA-Z]\w*'
    t.type = reserved.get(t.value, 'NFUNCION')  # Check for reserved words
    return t
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_CADENA(t):
    r'\'[\w\W\s]*\'|"[\w\W\s]*\"'
    t.value = str(t.value)
    return t
def t_BOOLEAN(t):
    r'(True|False)'
    t.value = bool(t.value)
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
def t_INCLUDE(t):
    r'include'
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
def t_GETMESSAGE(t):
    r'\-\>getmessage\(\)'

    return (t)
def t_ABSTRACT(t):
    r'abstract'
    return t
def t_DECLARE(t):
    r'declare'
    return t
def t_ECHO(t):
    r'echo'
    return t
def t_CONST(t):
    r'const'
    return t
#Joselyne Torres (fin)
def t_CASE(t):
    r'case'
    return t
def t_BREAK(t): #David Cevallos Inicio
  r'break'
  return t
def t_CLASS(t):
  r'class'
  return t
def t_CONTINUE(t):
  r'continue'
  return t
def t_DEFAULT(t):
    r'default'
    return t
def t_DO(t):
    r'do'
    return t
def t_EXTENDS(t):
    r'extends'
    return t
def t_FINAL(t):
    r'final'
    return t
def t_FUNCTION(t):
  r'function'
  return t
def t_GLOBAL(t):
    r'global'
    return t
def t_INSTANCEOF(t):
    r'instanceof'
    return t
#David Cevallos Fin
def t_ARRAY_MAP(t):
    r'array_map'
    return t
def t_HEAP(t):
    r'heap'
    return t
def t_PRINT(t):
    r'print'
    return t





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

