
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AND ASIGNACION BOOLEAN BOOLEAN_AND BOOLEAN_OR BREAK CADENA CASE CATCH CLASS COMMENT CONCAT_EQUAL CONST CONTINUE DECLARE DECREMENTO DEFAULT DIVIDE DIV_EQUAL DO DOUBLE_ARROW ECHO ELSE ELSEIF EXTENDS FIN FINAL FOR FUNCTION GLOBAL ID IF IGUAL INCLUDE INCREMENTO INICIO INSTANCEOF IS_NOT_EQUAL LLLAVE LPAREN MAYOR MAYORIGUAL MENOR MENORIGUAL MINUS MOD NUMBER OR PCOMA PLUS PRINT PRIVATE PROTECTED PUBLIC REF RLLAVE RPAREN TIMES TRY WHILEprograma : INICIO sentencias FINsentencias : asignacion\n                    | comparacionasignacion : ID ASIGNACION valor PCOMA\n                | ID REF ID PCOMAvalor : ID\n             | NUMBER\n             | CADENA\n             | BOOLEAN\n    opcomparacion : IGUAL\n                    | MAYOR\n                    | MENOR\n                    | MAYORIGUAL\n                    | MENORIGUAL\n    expcmp : valor opcomparacion valorcomparacion : IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE'
    
_lr_action_items = {'INICIO':([0,],[2,]),'$end':([1,8,],[0,-1,]),'ID':([2,9,10,11,23,24,25,26,27,28,29,],[6,12,17,12,12,-10,-11,-12,-13,-14,6,]),'IF':([2,29,],[7,7,]),'FIN':([3,4,5,20,21,32,],[8,-2,-3,-4,-5,-16,]),'RLLAVE':([4,5,20,21,31,32,],[-2,-3,-4,-5,32,-16,]),'ASIGNACION':([6,],[9,]),'REF':([6,],[10,]),'LPAREN':([7,],[11,]),'NUMBER':([9,11,23,24,25,26,27,28,],[14,14,14,-10,-11,-12,-13,-14,]),'CADENA':([9,11,23,24,25,26,27,28,],[15,15,15,-10,-11,-12,-13,-14,]),'BOOLEAN':([9,11,23,24,25,26,27,28,],[16,16,16,-10,-11,-12,-13,-14,]),'PCOMA':([12,13,14,15,16,17,],[-6,20,-7,-8,-9,21,]),'IGUAL':([12,14,15,16,19,],[-6,-7,-8,-9,24,]),'MAYOR':([12,14,15,16,19,],[-6,-7,-8,-9,25,]),'MENOR':([12,14,15,16,19,],[-6,-7,-8,-9,26,]),'MAYORIGUAL':([12,14,15,16,19,],[-6,-7,-8,-9,27,]),'MENORIGUAL':([12,14,15,16,19,],[-6,-7,-8,-9,28,]),'RPAREN':([12,14,15,16,18,30,],[-6,-7,-8,-9,22,-15,]),'LLLAVE':([22,],[29,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'sentencias':([2,29,],[3,31,]),'asignacion':([2,29,],[4,4,]),'comparacion':([2,29,],[5,5,]),'valor':([9,11,23,],[13,19,30,]),'expcmp':([11,],[18,]),'opcomparacion':([19,],[23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> INICIO sentencias FIN','programa',3,'p_programa','sintactico.py',5),
  ('sentencias -> asignacion','sentencias',1,'p_sentencias','sintactico.py',8),
  ('sentencias -> comparacion','sentencias',1,'p_sentencias','sintactico.py',9),
  ('asignacion -> ID ASIGNACION valor PCOMA','asignacion',4,'p_asignacion','sintactico.py',12),
  ('asignacion -> ID REF ID PCOMA','asignacion',4,'p_asignacion','sintactico.py',13),
  ('valor -> ID','valor',1,'p_valor','sintactico.py',15),
  ('valor -> NUMBER','valor',1,'p_valor','sintactico.py',16),
  ('valor -> CADENA','valor',1,'p_valor','sintactico.py',17),
  ('valor -> BOOLEAN','valor',1,'p_valor','sintactico.py',18),
  ('opcomparacion -> IGUAL','opcomparacion',1,'p_opcomparacion','sintactico.py',22),
  ('opcomparacion -> MAYOR','opcomparacion',1,'p_opcomparacion','sintactico.py',23),
  ('opcomparacion -> MENOR','opcomparacion',1,'p_opcomparacion','sintactico.py',24),
  ('opcomparacion -> MAYORIGUAL','opcomparacion',1,'p_opcomparacion','sintactico.py',25),
  ('opcomparacion -> MENORIGUAL','opcomparacion',1,'p_opcomparacion','sintactico.py',26),
  ('expcmp -> valor opcomparacion valor','expcmp',3,'p_expresioncmp','sintactico.py',30),
  ('comparacion -> IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE','comparacion',7,'p_comparacionif','sintactico.py',33),
]
