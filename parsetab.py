
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AND ARRAY ARRAY_MAP ASIGNACION BOOLEAN BOOLEAN_AND BOOLEAN_OR BREAK CADENA CASE CATCH CLASS COMA COMMENT CONCAT_EQUAL CONST CONTINUE DECLARE DECREMENTO DEFAULT DIVIDE DIV_EQUAL DO DOUBLE_ARROW ECHO ELSE ELSEIF EXCEPTION EXTENDS FIN FINAL FLECHA FOR FUNCTION GETMESSAGE GLOBAL HEAP ID IF IGUAL INCLUDE INCREMENTO INICIO INSERT INSTANCEOF IS_NOT_EQUAL LCORCH LLLAVE LPAREN MAYOR MAYORIGUAL MENOR MENORIGUAL MINUS MOD NFUNCION NUMBER OR PCOMA PLUS PRINT PRIVATE PROTECTED PUBLIC RCORCH REF RETURN RLLAVE RPAREN SORT TIMES TRY WHILEprograma : INICIO sentencias FINsentencias : asignacion\n                    | comparacion\n                    | funcion\n                    | impresion\n                    | repeticion\n                    | expresion\n                    | excepcion\n                    | heap\n                    | array_map\n    asignacion : ID ASIGNACION valor PCOMA\n                | ID REF ID PCOMA\n                | ID ASIGNACION estdatos PCOMA\n                | ID ASIGNACION expresion PCOMAvalor : ID valor : NUMBER valor : CADENAvalor : BOOLEANopcomparacion : IGUAL\n                    | MAYOR\n                    | MENOR\n                    | MAYORIGUAL\n                    | MENORIGUAL\n    expcmp : valor opcomparacion valor\n            | LPAREN valor opcomparacion valor RPAREN oplog LPAREN valor opcomparacion valor RPAREN\n            | LPAREN valor opcomparacion valor RPAREN oplog LPAREN valor opcomparacion valor RPAREN oplog expcmp expcmplog : expcmp oplog expcmp\n                | expcmp oplog expcmplogoplog : BOOLEAN_OR\n            | BOOLEAN_AND\n            | AND\n            | ORcomparacion : IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE\n                    | IF LPAREN expcmplog RPAREN LLLAVE sentencias RLLAVEcomparacion : IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE ELSE LLLAVE sentencias RLLAVEcomparacion : IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE ELSEIF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE ELSE LLLAVE sentencias RLLAVE array : ARRAY LPAREN valor DOUBLE_ARROW valor RPAREN\n            | ARRAY LPAREN valor RPARENsort : SORT LPAREN ID RPAREN PCOMAestdatos : array\n                | array_map\n                | heapexpresionmat : NUMBER operadormat NUMBERoperadormat : PLUS\n                    | DIVIDE\n                    | MINUS\n                    | TIMESexpresion : expresionmat\n                | expcmplogfuncion : sortfuncion : FUNCTION NFUNCION ID LPAREN args RPAREN LLLAVE sentencias RLLAVE\n            | FUNCTION NFUNCION ID LPAREN args RPAREN LLLAVE sentencias RETURN valor PCOMA RLLAVEargs : ID\n            | ID argsexcepcion : TRY LLLAVE sentencias RLLAVE CATCH LPAREN EXCEPTION ID RPAREN LLLAVE ECHO CADENA COMA ID FLECHA GETMESSAGE RLLAVEimpresion : ECHO valor PCOMA\n             | PRINT valor PCOMArepeticionrep : MAYOR\n                  | MENOR\n                  | MAYORIGUAL\n                  | MENORIGUAL\n  actualizar : INCREMENTO\n                | DECREMENTO\n  repeticion : FOR LPAREN ID ASIGNACION NUMBER PCOMA ID repeticionrep NUMBER PCOMA ID actualizar RPAREN LLLAVE sentencias RLLAVErepeticion : WHILE LPAREN ID opcomparacion valor RPAREN LLLAVE sentencias ID actualizar PCOMA RLLAVE\n                  | DO LLLAVE sentencias ID actualizar PCOMA RLLAVE WHILE LPAREN ID opcomparacion valor RPAREN PCOMA\n  array_map : ARRAY_MAP LPAREN funcion COMA array RPAREN PCOMAheap : INSERT LPAREN LCORCH NUMBER COMA NUMBER RCORCH RPAREN PCOMA\n                | INSERT LPAREN ARRAY LPAREN valor DOUBLE_ARROW NUMBER RPAREN RPAREN PCOMA'
    
_lr_action_items = {'INICIO':([0,],[2,]),'$end':([1,34,],[0,-1,]),'ID':([2,4,5,6,7,8,9,10,11,12,16,18,19,21,22,27,29,33,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52,55,61,62,63,66,76,79,80,81,83,84,86,88,94,95,96,97,98,102,104,108,112,113,115,126,127,134,142,143,144,145,147,149,152,163,168,169,170,171,172,175,177,183,187,188,190,194,196,197,198,200,204,207,209,210,215,216,219,220,],[13,-2,-3,-4,-5,-6,-7,-8,-9,-10,45,-49,-50,45,45,-48,-17,-18,45,75,45,-19,-20,-21,-22,-23,45,-15,-16,45,-29,-30,-31,-32,82,85,87,13,13,93,-24,45,-27,-28,-56,-57,-43,105,-11,-13,-14,45,-12,115,45,45,13,13,115,-39,45,146,-33,-34,45,13,13,165,-67,174,13,45,45,-51,45,185,-68,192,-69,-35,-25,45,13,45,-52,-65,-26,211,13,-66,13,-64,-55,-36,]),'IF':([2,62,63,112,113,145,147,168,196,209,215,],[15,15,15,15,15,15,15,15,15,15,15,]),'FUNCTION':([2,62,63,65,112,113,145,147,168,196,209,215,],[20,20,20,20,20,20,20,20,20,20,20,20,]),'ECHO':([2,62,63,112,113,145,147,168,186,196,209,215,],[21,21,21,21,21,21,21,21,195,21,21,21,]),'PRINT':([2,62,63,112,113,145,147,168,196,209,215,],[22,22,22,22,22,22,22,22,22,22,22,]),'FOR':([2,62,63,112,113,145,147,168,196,209,215,],[23,23,23,23,23,23,23,23,23,23,23,]),'WHILE':([2,62,63,112,113,145,147,148,168,196,209,215,],[25,25,25,25,25,25,25,164,25,25,25,25,]),'DO':([2,62,63,112,113,145,147,168,196,209,215,],[26,26,26,26,26,26,26,26,26,26,26,]),'TRY':([2,62,63,112,113,145,147,168,196,209,215,],[28,28,28,28,28,28,28,28,28,28,28,]),'INSERT':([2,35,62,63,112,113,145,147,168,196,209,215,],[30,30,30,30,30,30,30,30,30,30,30,30,]),'ARRAY_MAP':([2,35,62,63,112,113,145,147,168,196,209,215,],[31,31,31,31,31,31,31,31,31,31,31,31,]),'SORT':([2,62,63,65,112,113,145,147,168,196,209,215,],[32,32,32,32,32,32,32,32,32,32,32,32,]),'NUMBER':([2,16,21,22,35,37,38,39,40,41,42,43,47,48,49,50,51,56,57,58,59,60,62,63,79,90,97,103,104,108,112,113,123,127,139,144,145,147,158,159,160,161,162,168,169,170,172,194,196,197,209,215,],[24,46,46,46,70,46,-19,-20,-21,-22,-23,46,46,-29,-30,-31,-32,86,-44,-45,-46,-47,24,24,46,107,46,117,46,46,24,24,138,46,151,46,24,24,173,-58,-59,-60,-61,24,46,46,46,46,24,46,24,24,]),'LPAREN':([2,15,23,25,30,31,32,35,43,47,48,49,50,51,62,63,74,82,91,112,113,122,131,145,147,155,164,168,169,196,197,209,215,],[16,43,55,61,64,65,66,16,16,16,-29,-30,-31,-32,16,16,97,102,108,16,16,137,144,16,16,169,175,16,16,16,16,16,16,]),'CADENA':([2,16,21,22,35,37,38,39,40,41,42,43,47,48,49,50,51,62,63,79,97,104,108,112,113,127,144,145,147,168,169,170,172,194,195,196,197,209,215,],[29,29,29,29,29,29,-19,-20,-21,-22,-23,29,29,-29,-30,-31,-32,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,202,29,29,29,29,]),'BOOLEAN':([2,16,21,22,35,37,38,39,40,41,42,43,47,48,49,50,51,62,63,79,97,104,108,112,113,127,144,145,147,168,169,170,172,194,196,197,209,215,],[33,33,33,33,33,33,-19,-20,-21,-22,-23,33,33,-29,-30,-31,-32,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'FIN':([3,4,5,6,7,8,9,10,11,12,18,19,27,29,33,45,46,76,80,81,83,84,86,94,95,96,98,126,142,143,152,171,177,187,188,190,198,200,204,210,216,219,220,],[34,-2,-3,-4,-5,-6,-7,-8,-9,-10,-49,-50,-48,-17,-18,-15,-16,-24,-27,-28,-56,-57,-43,-11,-13,-14,-12,-39,-33,-34,-67,-51,-68,-69,-35,-25,-52,-65,-26,-66,-64,-55,-36,]),'RLLAVE':([4,5,6,7,8,9,10,11,12,18,19,27,29,33,45,46,76,80,81,83,84,86,89,94,95,96,98,126,129,130,136,142,143,152,157,171,177,179,187,188,190,191,193,198,200,203,204,210,213,216,217,218,219,220,],[-2,-3,-4,-5,-6,-7,-8,-9,-10,-49,-50,-48,-17,-18,-15,-16,-24,-27,-28,-56,-57,-43,106,-11,-13,-14,-12,-39,142,143,148,-33,-34,-67,171,-51,-68,188,-69,-35,-25,198,200,-52,-65,208,-26,-66,216,-64,219,220,-55,-36,]),'RETURN':([4,5,6,7,8,9,10,11,12,18,19,27,29,33,45,46,76,80,81,83,84,86,94,95,96,98,126,142,143,152,157,171,177,187,188,190,198,200,204,210,216,219,220,],[-2,-3,-4,-5,-6,-7,-8,-9,-10,-49,-50,-48,-17,-18,-15,-16,-24,-27,-28,-56,-57,-43,-11,-13,-14,-12,-39,-33,-34,-67,172,-51,-68,-69,-35,-25,-52,-65,-26,-66,-64,-55,-36,]),'ASIGNACION':([13,85,],[35,103,]),'REF':([13,],[36,]),'IGUAL':([13,14,24,29,33,44,45,46,67,70,87,156,185,],[-15,38,-16,-17,-18,38,-15,-16,38,-16,38,38,38,]),'MAYOR':([13,14,24,29,33,44,45,46,67,70,87,146,156,185,],[-15,39,-16,-17,-18,39,-15,-16,39,-16,39,159,39,39,]),'MENOR':([13,14,24,29,33,44,45,46,67,70,87,146,156,185,],[-15,40,-16,-17,-18,40,-15,-16,40,-16,40,160,40,40,]),'MAYORIGUAL':([13,14,24,29,33,44,45,46,67,70,87,146,156,185,],[-15,41,-16,-17,-18,41,-15,-16,41,-16,41,161,41,41,]),'MENORIGUAL':([13,14,24,29,33,44,45,46,67,70,87,146,156,185,],[-15,42,-16,-17,-18,42,-15,-16,42,-16,42,162,42,42,]),'BOOLEAN_OR':([17,29,33,45,46,76,77,80,114,190,204,],[48,-17,-18,-15,-16,-24,48,48,48,48,-26,]),'BOOLEAN_AND':([17,29,33,45,46,76,77,80,114,190,204,],[49,-17,-18,-15,-16,-24,49,49,49,49,-26,]),'AND':([17,29,33,45,46,76,77,80,114,190,204,],[50,-17,-18,-15,-16,-24,50,50,50,50,-26,]),'OR':([17,29,33,45,46,76,77,80,114,190,204,],[51,-17,-18,-15,-16,-24,51,51,51,51,-26,]),'PCOMA':([18,27,29,33,45,46,53,54,67,68,69,70,71,72,73,75,76,80,81,86,110,117,119,120,121,128,140,152,153,166,173,177,178,182,184,187,190,204,206,],[-49,-48,-17,-18,-15,-16,83,84,94,95,96,-16,-40,-41,-42,98,-24,-27,-28,-43,126,134,136,-62,-63,-38,152,-67,-37,177,183,-68,187,191,193,-69,-25,-26,210,]),'COMA':([19,92,107,126,171,198,202,],[-50,109,123,-39,-51,-52,207,]),'NFUNCION':([20,],[52,]),'PLUS':([24,70,],[57,57,]),'DIVIDE':([24,70,],[58,58,]),'MINUS':([24,70,],[59,59,]),'TIMES':([24,70,],[60,60,]),'LLLAVE':([26,28,99,100,133,135,154,176,189,205,212,],[62,63,112,113,145,147,168,186,196,209,215,]),'RPAREN':([29,33,45,46,76,77,78,80,81,93,101,111,115,116,118,120,121,125,128,132,141,150,151,153,165,167,180,181,190,199,201,204,],[-17,-18,-15,-16,-24,99,100,-27,-28,110,114,128,-53,133,135,-62,-63,140,-38,-54,153,166,167,-37,176,178,189,190,-25,205,206,-26,]),'DOUBLE_ARROW':([29,33,45,46,111,124,],[-17,-18,-15,-16,127,139,]),'ARRAY':([35,64,109,],[74,91,74,]),'LCORCH':([64,],[90,]),'INCREMENTO':([105,174,192,],[120,120,120,]),'DECREMENTO':([105,174,192,],[121,121,121,]),'CATCH':([106,],[122,]),'EXCEPTION':([137,],[149,]),'RCORCH':([138,],[150,]),'ELSE':([142,208,],[154,212,]),'ELSEIF':([142,],[155,]),'FLECHA':([211,],[214,]),'GETMESSAGE':([214,],[217,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'sentencias':([2,62,63,112,113,145,147,168,196,209,215,],[3,88,89,129,130,157,163,179,203,213,218,]),'asignacion':([2,62,63,112,113,145,147,168,196,209,215,],[4,4,4,4,4,4,4,4,4,4,4,]),'comparacion':([2,62,63,112,113,145,147,168,196,209,215,],[5,5,5,5,5,5,5,5,5,5,5,]),'funcion':([2,62,63,65,112,113,145,147,168,196,209,215,],[6,6,6,92,6,6,6,6,6,6,6,6,]),'impresion':([2,62,63,112,113,145,147,168,196,209,215,],[7,7,7,7,7,7,7,7,7,7,7,]),'repeticion':([2,62,63,112,113,145,147,168,196,209,215,],[8,8,8,8,8,8,8,8,8,8,8,]),'expresion':([2,35,62,63,112,113,145,147,168,196,209,215,],[9,69,9,9,9,9,9,9,9,9,9,9,]),'excepcion':([2,62,63,112,113,145,147,168,196,209,215,],[10,10,10,10,10,10,10,10,10,10,10,]),'heap':([2,35,62,63,112,113,145,147,168,196,209,215,],[11,73,11,11,11,11,11,11,11,11,11,11,]),'array_map':([2,35,62,63,112,113,145,147,168,196,209,215,],[12,72,12,12,12,12,12,12,12,12,12,12,]),'valor':([2,16,21,22,35,37,43,47,62,63,79,97,104,108,112,113,127,144,145,147,168,169,170,172,194,196,197,209,215,],[14,44,53,54,67,76,14,14,14,14,101,111,118,124,14,14,141,156,14,14,14,14,181,182,201,14,14,14,14,]),'expcmp':([2,35,43,47,62,63,112,113,145,147,168,169,196,197,209,215,],[17,17,77,80,17,17,17,17,17,17,17,180,17,204,17,17,]),'expcmplog':([2,35,43,47,62,63,112,113,145,147,168,196,209,215,],[18,18,78,81,18,18,18,18,18,18,18,18,18,18,]),'sort':([2,62,63,65,112,113,145,147,168,196,209,215,],[19,19,19,19,19,19,19,19,19,19,19,19,]),'expresionmat':([2,35,62,63,112,113,145,147,168,196,209,215,],[27,27,27,27,27,27,27,27,27,27,27,27,]),'opcomparacion':([14,44,67,87,156,185,],[37,79,37,104,170,194,]),'oplog':([17,77,80,114,190,],[47,47,47,131,197,]),'operadormat':([24,70,],[56,56,]),'estdatos':([35,],[68,]),'array':([35,109,],[71,125,]),'args':([102,115,],[116,132,]),'actualizar':([105,174,192,],[119,184,199,]),'repeticionrep':([146,],[158,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> INICIO sentencias FIN','programa',3,'p_programa','sintactico.py',6),
  ('sentencias -> asignacion','sentencias',1,'p_sentencias','sintactico.py',11),
  ('sentencias -> comparacion','sentencias',1,'p_sentencias','sintactico.py',12),
  ('sentencias -> funcion','sentencias',1,'p_sentencias','sintactico.py',13),
  ('sentencias -> impresion','sentencias',1,'p_sentencias','sintactico.py',14),
  ('sentencias -> repeticion','sentencias',1,'p_sentencias','sintactico.py',15),
  ('sentencias -> expresion','sentencias',1,'p_sentencias','sintactico.py',16),
  ('sentencias -> excepcion','sentencias',1,'p_sentencias','sintactico.py',17),
  ('sentencias -> heap','sentencias',1,'p_sentencias','sintactico.py',18),
  ('sentencias -> array_map','sentencias',1,'p_sentencias','sintactico.py',19),
  ('asignacion -> ID ASIGNACION valor PCOMA','asignacion',4,'p_asignacion','sintactico.py',24),
  ('asignacion -> ID REF ID PCOMA','asignacion',4,'p_asignacion','sintactico.py',25),
  ('asignacion -> ID ASIGNACION estdatos PCOMA','asignacion',4,'p_asignacion','sintactico.py',26),
  ('asignacion -> ID ASIGNACION expresion PCOMA','asignacion',4,'p_asignacion','sintactico.py',27),
  ('valor -> ID','valor',1,'p_valor_id','sintactico.py',33),
  ('valor -> NUMBER','valor',1,'p_valor_number','sintactico.py',37),
  ('valor -> CADENA','valor',1,'p_valor_cadena','sintactico.py',41),
  ('valor -> BOOLEAN','valor',1,'p_valor_boolean','sintactico.py',45),
  ('opcomparacion -> IGUAL','opcomparacion',1,'p_opcomparacion','sintactico.py',49),
  ('opcomparacion -> MAYOR','opcomparacion',1,'p_opcomparacion','sintactico.py',50),
  ('opcomparacion -> MENOR','opcomparacion',1,'p_opcomparacion','sintactico.py',51),
  ('opcomparacion -> MAYORIGUAL','opcomparacion',1,'p_opcomparacion','sintactico.py',52),
  ('opcomparacion -> MENORIGUAL','opcomparacion',1,'p_opcomparacion','sintactico.py',53),
  ('expcmp -> valor opcomparacion valor','expcmp',3,'p_expresioncmp','sintactico.py',58),
  ('expcmp -> LPAREN valor opcomparacion valor RPAREN oplog LPAREN valor opcomparacion valor RPAREN','expcmp',11,'p_expresioncmp','sintactico.py',59),
  ('expcmp -> LPAREN valor opcomparacion valor RPAREN oplog LPAREN valor opcomparacion valor RPAREN oplog expcmp','expcmp',13,'p_expresioncmp','sintactico.py',60),
  ('expcmplog -> expcmp oplog expcmp','expcmplog',3,'p_expresioncmplog','sintactico.py',64),
  ('expcmplog -> expcmp oplog expcmplog','expcmplog',3,'p_expresioncmplog','sintactico.py',65),
  ('oplog -> BOOLEAN_OR','oplog',1,'p_oplog','sintactico.py',69),
  ('oplog -> BOOLEAN_AND','oplog',1,'p_oplog','sintactico.py',70),
  ('oplog -> AND','oplog',1,'p_oplog','sintactico.py',71),
  ('oplog -> OR','oplog',1,'p_oplog','sintactico.py',72),
  ('comparacion -> IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE','comparacion',7,'p_comparacionif','sintactico.py',76),
  ('comparacion -> IF LPAREN expcmplog RPAREN LLLAVE sentencias RLLAVE','comparacion',7,'p_comparacionif','sintactico.py',77),
  ('comparacion -> IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE ELSE LLLAVE sentencias RLLAVE','comparacion',11,'p_comparacionif_else','sintactico.py',81),
  ('comparacion -> IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE ELSEIF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE ELSE LLLAVE sentencias RLLAVE','comparacion',18,'p_comparacionif_elseif_else','sintactico.py',84),
  ('array -> ARRAY LPAREN valor DOUBLE_ARROW valor RPAREN','array',6,'p_array','sintactico.py',87),
  ('array -> ARRAY LPAREN valor RPAREN','array',4,'p_array','sintactico.py',88),
  ('sort -> SORT LPAREN ID RPAREN PCOMA','sort',5,'p_sort','sintactico.py',92),
  ('estdatos -> array','estdatos',1,'p_estdatos','sintactico.py',95),
  ('estdatos -> array_map','estdatos',1,'p_estdatos','sintactico.py',96),
  ('estdatos -> heap','estdatos',1,'p_estdatos','sintactico.py',97),
  ('expresionmat -> NUMBER operadormat NUMBER','expresionmat',3,'p_expresionmat','sintactico.py',100),
  ('operadormat -> PLUS','operadormat',1,'p_operadormat','sintactico.py',103),
  ('operadormat -> DIVIDE','operadormat',1,'p_operadormat','sintactico.py',104),
  ('operadormat -> MINUS','operadormat',1,'p_operadormat','sintactico.py',105),
  ('operadormat -> TIMES','operadormat',1,'p_operadormat','sintactico.py',106),
  ('expresion -> expresionmat','expresion',1,'p_expresion','sintactico.py',110),
  ('expresion -> expcmplog','expresion',1,'p_expresion','sintactico.py',111),
  ('funcion -> sort','funcion',1,'p_funcion','sintactico.py',113),
  ('funcion -> FUNCTION NFUNCION ID LPAREN args RPAREN LLLAVE sentencias RLLAVE','funcion',9,'p_funciondef','sintactico.py',116),
  ('funcion -> FUNCTION NFUNCION ID LPAREN args RPAREN LLLAVE sentencias RETURN valor PCOMA RLLAVE','funcion',12,'p_funciondef','sintactico.py',117),
  ('args -> ID','args',1,'p_args','sintactico.py',121),
  ('args -> ID args','args',2,'p_args','sintactico.py',122),
  ('excepcion -> TRY LLLAVE sentencias RLLAVE CATCH LPAREN EXCEPTION ID RPAREN LLLAVE ECHO CADENA COMA ID FLECHA GETMESSAGE RLLAVE','excepcion',17,'p_excepcion','sintactico.py',125),
  ('impresion -> ECHO valor PCOMA','impresion',3,'p_impresion','sintactico.py',130),
  ('impresion -> PRINT valor PCOMA','impresion',3,'p_impresion','sintactico.py',131),
  ('repeticionrep -> MAYOR','repeticionrep',1,'p_repeticioncompfor','sintactico.py',135),
  ('repeticionrep -> MENOR','repeticionrep',1,'p_repeticioncompfor','sintactico.py',136),
  ('repeticionrep -> MAYORIGUAL','repeticionrep',1,'p_repeticioncompfor','sintactico.py',137),
  ('repeticionrep -> MENORIGUAL','repeticionrep',1,'p_repeticioncompfor','sintactico.py',138),
  ('actualizar -> INCREMENTO','actualizar',1,'p_actualizar','sintactico.py',142),
  ('actualizar -> DECREMENTO','actualizar',1,'p_actualizar','sintactico.py',143),
  ('repeticion -> FOR LPAREN ID ASIGNACION NUMBER PCOMA ID repeticionrep NUMBER PCOMA ID actualizar RPAREN LLLAVE sentencias RLLAVE','repeticion',16,'p_repeticionfor','sintactico.py',147),
  ('repeticion -> WHILE LPAREN ID opcomparacion valor RPAREN LLLAVE sentencias ID actualizar PCOMA RLLAVE','repeticion',12,'p_repeticionwhile','sintactico.py',152),
  ('repeticion -> DO LLLAVE sentencias ID actualizar PCOMA RLLAVE WHILE LPAREN ID opcomparacion valor RPAREN PCOMA','repeticion',14,'p_repeticionwhile','sintactico.py',153),
  ('array_map -> ARRAY_MAP LPAREN funcion COMA array RPAREN PCOMA','array_map',7,'p_array_map','sintactico.py',157),
  ('heap -> INSERT LPAREN LCORCH NUMBER COMA NUMBER RCORCH RPAREN PCOMA','heap',9,'p_heap','sintactico.py',160),
  ('heap -> INSERT LPAREN ARRAY LPAREN valor DOUBLE_ARROW NUMBER RPAREN RPAREN PCOMA','heap',10,'p_heap','sintactico.py',161),
]
