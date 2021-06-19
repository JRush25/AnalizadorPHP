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
    'const' : 'CONST'
#Joselyne Torres (fin)
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
    'CADENA',
    'BOOLEAN',
    'INCREMENTO'
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
t_INCREMENTO = r'\+\+'

#Joselyne Torres (inicio)
def t_ID(t):
    r'\$[a-zA-Z_]\w+'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_CADENA(t):
    r'\'[\w\W\s]*\''
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
def t_WHILE(t):
    r'while'
    return t
def t_FOR(t):
    r'for'
    return t
def t_AND(t):
    r'and'
    return t
def t_OR(t):
    r'or'
    return t
def t_INCLUDE(t):
    r'include'
    return t
def t_TRY(t):
    r'try'
    return t
def t_CATCH(t):
    r'catch'
    return t
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
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")