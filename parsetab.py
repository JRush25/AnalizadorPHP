
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AND ARRAY ARRAY_MAP ASIGNACION BOOLEAN BREAK CADENA CASE CATCH CLASS COMA COMMENT CONCAT_EQUAL CONST CONTINUE DECLARE DECREMENTO DEFAULT DIVIDE DIV_EQUAL DO DOUBLE_ARROW ECHO ELSE ELSEIF EXCEPTION EXTENDS FIN FINAL FLECHA FOR FUNCTION GETMESSAGE GLOBAL HEAP ID IF IGUAL INCLUDE INCREMENTO INICIO INSERT INSTANCEOF IS_NOT_EQUAL LCORCH LLLAVE LPAREN MAYOR MAYORIGUAL MENOR MENORIGUAL MINUS MOD NFUNCION NUMBER OR PCOMA PLUS PRINT PRIVATE PROTECTED PUBLIC RCORCH REF RETURN RLLAVE RPAREN SORT TIMES TRY WHILEprograma : INICIO sentencias FINsentencias : asignacion\n                    | comparacion\n                    | funcion\n                    | impresion\n                    | repeticion\n                    | expresion\n                    | excepcion\n                    | estdatos\n    asignacion : ID ASIGNACION valor PCOMA\n                | ID REF ID PCOMA\n                | ID ASIGNACION estdatos PCOMA\n                | ID ASIGNACION expresion PCOMAvalor : ID\n            | NUMBER\n            | BOOLEAN\n            | CADENAopcomparacion : IGUAL\n                    | MAYOR\n                    | MENOR\n                    | MAYORIGUAL\n                    | MENORIGUAL\n                    | IS_NOT_EQUALexpcmp : valor opcomparacion valor\n            | LPAREN valor opcomparacion valor RPAREN oplog LPAREN valor opcomparacion valor RPAREN\n             expcmplog : expcmp oplog expcmp\n                | expcmp oplog expcmplogoplog : AND\n            | ORcomparacion : IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE\n                    | IF LPAREN expcmplog RPAREN LLLAVE sentencias RLLAVEcomparacion : IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE ELSE LLLAVE sentencias RLLAVEcomparacion : IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE ELSEIF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE ELSE LLLAVE sentencias RLLAVE array : ARRAY LPAREN valor DOUBLE_ARROW valor RPAREN\n            | ARRAY LPAREN valor RPARENsort : SORT LPAREN ID RPAREN PCOMAestdatos : array\n                | array_map\n                | heapexpresionmat : NUMBER operadormat NUMBERoperadormat : PLUS\n                    | MINUS\n                    | TIMES\n                    | DIVIDEexpresion : expresionmat\n                | expcmplogfuncion : sortfuncion : FUNCTION NFUNCION ID LPAREN args RPAREN LLLAVE sentencias RLLAVE\n            | FUNCTION NFUNCION ID LPAREN args RPAREN LLLAVE sentencias RETURN valor PCOMA RLLAVEargs : ID\n            | ID argsexcepcion : TRY LLLAVE sentencias RLLAVE CATCH LPAREN EXCEPTION ID RPAREN LLLAVE ECHO CADENA COMA ID RLLAVEimpresion : ECHO valor PCOMA\n             | PRINT valor PCOMA\n             | PRINT expresionmat PCOMArepeticionrep : MAYOR\n                  | MENOR\n                  | MAYORIGUAL\n                  | MENORIGUAL actualizar : INCREMENTO\n                | DECREMENTO\n  repeticion : FOR LPAREN ID ASIGNACION NUMBER PCOMA ID repeticionrep NUMBER PCOMA ID actualizar RPAREN LLLAVE sentencias RLLAVErepeticion : WHILE LPAREN ID opcomparacion valor RPAREN LLLAVE sentencias ID actualizar PCOMA RLLAVE\n                  | DO LLLAVE sentencias ID actualizar PCOMA RLLAVE WHILE LPAREN ID opcomparacion valor RPAREN PCOMA\n  array_map : ARRAY_MAP LPAREN funcion COMA array RPAREN PCOMAheap : INSERT LPAREN LCORCH NUMBER COMA NUMBER RCORCH RPAREN PCOMA\n                | INSERT LPAREN ARRAY LPAREN valor DOUBLE_ARROW NUMBER RPAREN RPAREN PCOMA'
    
_lr_action_items = {'INICIO':([0,],[2,]),'$end':([1,37,],[0,-1,]),'ID':([2,4,5,6,7,8,9,10,11,15,17,18,20,21,22,28,29,30,31,36,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,59,65,66,67,68,69,76,79,80,81,83,84,85,87,89,96,97,98,99,103,105,109,110,113,114,115,117,125,135,139,143,144,145,146,148,150,151,163,168,169,170,171,172,175,177,183,187,188,190,194,196,197,199,205,207,208,212,213,214,216,],[12,-2,-3,-4,-5,-6,-7,-8,-9,49,-46,-47,49,49,-45,-17,-37,-38,-39,-16,49,75,49,-18,-19,-20,-21,-22,-23,49,-14,-15,49,-28,-29,82,86,88,12,12,91,49,-24,49,-26,-27,-53,-54,-55,-40,106,-10,-12,-13,-11,117,49,49,-35,49,12,12,117,-36,147,-34,-30,-31,49,12,12,165,-65,174,12,49,49,-48,49,185,-66,192,-67,-32,-25,49,12,-49,-63,209,12,-64,-52,12,-62,-33,]),'IF':([2,66,67,114,115,146,148,168,196,207,213,],[14,14,14,14,14,14,14,14,14,14,14,]),'FUNCTION':([2,66,67,70,114,115,146,148,168,196,207,213,],[19,19,19,19,19,19,19,19,19,19,19,19,]),'ECHO':([2,66,67,114,115,146,148,168,186,196,207,213,],[20,20,20,20,20,20,20,20,195,20,20,20,]),'PRINT':([2,66,67,114,115,146,148,168,196,207,213,],[21,21,21,21,21,21,21,21,21,21,21,]),'FOR':([2,66,67,114,115,146,148,168,196,207,213,],[23,23,23,23,23,23,23,23,23,23,23,]),'WHILE':([2,66,67,114,115,146,148,149,168,196,207,213,],[25,25,25,25,25,25,25,164,25,25,25,25,]),'DO':([2,66,67,114,115,146,148,168,196,207,213,],[26,26,26,26,26,26,26,26,26,26,26,]),'TRY':([2,66,67,114,115,146,148,168,196,207,213,],[27,27,27,27,27,27,27,27,27,27,27,]),'SORT':([2,66,67,70,114,115,146,148,168,196,207,213,],[32,32,32,32,32,32,32,32,32,32,32,32,]),'NUMBER':([2,15,20,21,38,40,41,42,43,44,45,46,47,51,52,53,60,61,62,63,64,66,67,69,79,94,104,105,109,113,114,115,128,142,145,146,148,158,159,160,161,162,168,169,170,172,194,196,207,213,],[24,50,50,58,58,50,-18,-19,-20,-21,-22,-23,50,50,-28,-29,87,-41,-42,-43,-44,24,24,50,50,112,119,50,50,50,24,24,141,153,50,24,24,173,-56,-57,-58,-59,24,50,50,50,50,24,24,24,]),'ARRAY':([2,38,66,67,71,111,114,115,146,148,168,196,207,213,],[33,33,33,33,95,33,33,33,33,33,33,33,33,33,]),'ARRAY_MAP':([2,38,66,67,114,115,146,148,168,196,207,213,],[34,34,34,34,34,34,34,34,34,34,34,34,]),'INSERT':([2,38,66,67,114,115,146,148,168,196,207,213,],[35,35,35,35,35,35,35,35,35,35,35,35,]),'LPAREN':([2,14,23,25,32,33,34,35,38,47,51,52,53,66,67,82,95,114,115,124,132,146,148,155,164,168,169,196,207,213,],[15,47,59,65,68,69,70,71,15,15,15,-28,-29,15,15,103,113,15,15,138,145,15,15,169,175,15,15,15,15,15,]),'BOOLEAN':([2,15,20,21,38,40,41,42,43,44,45,46,47,51,52,53,66,67,69,79,105,109,113,114,115,145,146,148,168,169,170,172,194,196,207,213,],[36,36,36,36,36,36,-18,-19,-20,-21,-22,-23,36,36,-28,-29,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'CADENA':([2,15,20,21,38,40,41,42,43,44,45,46,47,51,52,53,66,67,69,79,105,109,113,114,115,145,146,148,168,169,170,172,194,195,196,207,213,],[28,28,28,28,28,28,-18,-19,-20,-21,-22,-23,28,28,-28,-29,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,201,28,28,28,]),'FIN':([3,4,5,6,7,8,9,10,11,17,18,22,28,29,30,31,36,49,50,76,80,81,83,84,85,87,96,97,98,99,110,125,139,143,144,151,171,177,187,188,190,197,199,208,212,214,216,],[37,-2,-3,-4,-5,-6,-7,-8,-9,-46,-47,-45,-17,-37,-38,-39,-16,-14,-15,-24,-26,-27,-53,-54,-55,-40,-10,-12,-13,-11,-35,-36,-34,-30,-31,-65,-48,-66,-67,-32,-25,-49,-63,-64,-52,-62,-33,]),'RLLAVE':([4,5,6,7,8,9,10,11,17,18,22,28,29,30,31,36,49,50,76,80,81,83,84,85,87,90,96,97,98,99,110,125,130,131,137,139,143,144,151,157,171,177,179,187,188,190,191,193,197,199,202,208,209,211,212,214,215,216,],[-2,-3,-4,-5,-6,-7,-8,-9,-46,-47,-45,-17,-37,-38,-39,-16,-14,-15,-24,-26,-27,-53,-54,-55,-40,107,-10,-12,-13,-11,-35,-36,143,144,149,-34,-30,-31,-65,171,-48,-66,188,-67,-32,-25,197,199,-49,-63,206,-64,212,214,-52,-62,216,-33,]),'RETURN':([4,5,6,7,8,9,10,11,17,18,22,28,29,30,31,36,49,50,76,80,81,83,84,85,87,96,97,98,99,110,125,139,143,144,151,157,171,177,187,188,190,197,199,208,212,214,216,],[-2,-3,-4,-5,-6,-7,-8,-9,-46,-47,-45,-17,-37,-38,-39,-16,-14,-15,-24,-26,-27,-53,-54,-55,-40,-10,-12,-13,-11,-35,-36,-34,-30,-31,-65,172,-48,-66,-67,-32,-25,-49,-63,-64,-52,-62,-33,]),'ASIGNACION':([12,86,],[38,104,]),'REF':([12,],[39,]),'IGUAL':([12,13,24,28,36,48,49,50,58,72,88,156,185,],[-14,41,-15,-17,-16,41,-14,-15,-15,41,41,41,41,]),'MAYOR':([12,13,24,28,36,48,49,50,58,72,88,147,156,185,],[-14,42,-15,-17,-16,42,-14,-15,-15,42,42,159,42,42,]),'MENOR':([12,13,24,28,36,48,49,50,58,72,88,147,156,185,],[-14,43,-15,-17,-16,43,-14,-15,-15,43,43,160,43,43,]),'MAYORIGUAL':([12,13,24,28,36,48,49,50,58,72,88,147,156,185,],[-14,44,-15,-17,-16,44,-14,-15,-15,44,44,161,44,44,]),'MENORIGUAL':([12,13,24,28,36,48,49,50,58,72,88,147,156,185,],[-14,45,-15,-17,-16,45,-14,-15,-15,45,45,162,45,45,]),'IS_NOT_EQUAL':([12,13,24,28,36,48,49,50,58,72,88,156,185,],[-14,46,-15,-17,-16,46,-14,-15,-15,46,46,46,46,]),'AND':([16,28,36,49,50,76,77,80,116,190,],[52,-17,-16,-14,-15,-24,52,52,52,-25,]),'OR':([16,28,36,49,50,76,77,80,116,190,],[53,-17,-16,-14,-15,-24,53,53,53,-25,]),'PCOMA':([17,22,28,29,30,31,36,49,50,55,56,57,58,72,73,74,75,76,80,81,87,108,110,119,121,122,123,139,140,151,166,173,177,178,182,184,187,190,204,],[-46,-45,-17,-37,-38,-39,-16,-14,-15,83,84,85,-15,96,97,98,99,-24,-26,-27,-40,125,-35,135,137,-60,-61,-34,151,-65,177,183,-66,187,191,193,-67,-25,208,]),'COMA':([18,93,112,125,171,197,201,],[-47,111,128,-36,-48,-49,205,]),'NFUNCION':([19,],[54,]),'PLUS':([24,58,],[61,61,]),'MINUS':([24,58,],[62,62,]),'TIMES':([24,58,],[63,63,]),'DIVIDE':([24,58,],[64,64,]),'LLLAVE':([26,27,100,101,134,136,154,176,189,203,210,],[66,67,114,115,146,148,168,186,196,207,213,]),'RPAREN':([28,36,49,50,76,77,78,80,81,91,92,102,110,117,118,120,122,123,126,127,133,139,152,153,165,167,180,181,190,198,200,],[-17,-16,-14,-15,-24,100,101,-26,-27,108,110,116,-35,-50,134,136,-60,-61,139,140,-51,-34,166,167,176,178,189,190,-25,203,204,]),'DOUBLE_ARROW':([28,36,49,50,92,129,],[-17,-16,-14,-15,109,142,]),'LCORCH':([71,],[94,]),'INCREMENTO':([106,174,192,],[122,122,122,]),'DECREMENTO':([106,174,192,],[123,123,123,]),'CATCH':([107,],[124,]),'EXCEPTION':([138,],[150,]),'RCORCH':([141,],[152,]),'ELSE':([143,206,],[154,210,]),'ELSEIF':([143,],[155,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'sentencias':([2,66,67,114,115,146,148,168,196,207,213,],[3,89,90,130,131,157,163,179,202,211,215,]),'asignacion':([2,66,67,114,115,146,148,168,196,207,213,],[4,4,4,4,4,4,4,4,4,4,4,]),'comparacion':([2,66,67,114,115,146,148,168,196,207,213,],[5,5,5,5,5,5,5,5,5,5,5,]),'funcion':([2,66,67,70,114,115,146,148,168,196,207,213,],[6,6,6,93,6,6,6,6,6,6,6,6,]),'impresion':([2,66,67,114,115,146,148,168,196,207,213,],[7,7,7,7,7,7,7,7,7,7,7,]),'repeticion':([2,66,67,114,115,146,148,168,196,207,213,],[8,8,8,8,8,8,8,8,8,8,8,]),'expresion':([2,38,66,67,114,115,146,148,168,196,207,213,],[9,74,9,9,9,9,9,9,9,9,9,9,]),'excepcion':([2,66,67,114,115,146,148,168,196,207,213,],[10,10,10,10,10,10,10,10,10,10,10,]),'estdatos':([2,38,66,67,114,115,146,148,168,196,207,213,],[11,73,11,11,11,11,11,11,11,11,11,11,]),'valor':([2,15,20,21,38,40,47,51,66,67,69,79,105,109,113,114,115,145,146,148,168,169,170,172,194,196,207,213,],[13,48,55,56,72,76,13,13,13,13,92,102,120,126,129,13,13,156,13,13,13,13,181,182,200,13,13,13,]),'expcmp':([2,38,47,51,66,67,114,115,146,148,168,169,196,207,213,],[16,16,77,80,16,16,16,16,16,16,16,180,16,16,16,]),'expcmplog':([2,38,47,51,66,67,114,115,146,148,168,196,207,213,],[17,17,78,81,17,17,17,17,17,17,17,17,17,17,]),'sort':([2,66,67,70,114,115,146,148,168,196,207,213,],[18,18,18,18,18,18,18,18,18,18,18,18,]),'expresionmat':([2,21,38,66,67,114,115,146,148,168,196,207,213,],[22,57,22,22,22,22,22,22,22,22,22,22,22,]),'array':([2,38,66,67,111,114,115,146,148,168,196,207,213,],[29,29,29,29,127,29,29,29,29,29,29,29,29,]),'array_map':([2,38,66,67,114,115,146,148,168,196,207,213,],[30,30,30,30,30,30,30,30,30,30,30,30,]),'heap':([2,38,66,67,114,115,146,148,168,196,207,213,],[31,31,31,31,31,31,31,31,31,31,31,31,]),'opcomparacion':([13,48,72,88,156,185,],[40,79,40,105,170,194,]),'oplog':([16,77,80,116,],[51,51,51,132,]),'operadormat':([24,58,],[60,60,]),'args':([103,117,],[118,133,]),'actualizar':([106,174,192,],[121,184,198,]),'repeticionrep':([147,],[158,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> INICIO sentencias FIN','programa',3,'p_programa','sintactico.py',9),
  ('sentencias -> asignacion','sentencias',1,'p_sentencias','sintactico.py',14),
  ('sentencias -> comparacion','sentencias',1,'p_sentencias','sintactico.py',15),
  ('sentencias -> funcion','sentencias',1,'p_sentencias','sintactico.py',16),
  ('sentencias -> impresion','sentencias',1,'p_sentencias','sintactico.py',17),
  ('sentencias -> repeticion','sentencias',1,'p_sentencias','sintactico.py',18),
  ('sentencias -> expresion','sentencias',1,'p_sentencias','sintactico.py',19),
  ('sentencias -> excepcion','sentencias',1,'p_sentencias','sintactico.py',20),
  ('sentencias -> estdatos','sentencias',1,'p_sentencias','sintactico.py',21),
  ('asignacion -> ID ASIGNACION valor PCOMA','asignacion',4,'p_asignacion','sintactico.py',26),
  ('asignacion -> ID REF ID PCOMA','asignacion',4,'p_asignacion','sintactico.py',27),
  ('asignacion -> ID ASIGNACION estdatos PCOMA','asignacion',4,'p_asignacion','sintactico.py',28),
  ('asignacion -> ID ASIGNACION expresion PCOMA','asignacion',4,'p_asignacion','sintactico.py',29),
  ('valor -> ID','valor',1,'p_valor','sintactico.py',35),
  ('valor -> NUMBER','valor',1,'p_valor','sintactico.py',36),
  ('valor -> BOOLEAN','valor',1,'p_valor','sintactico.py',37),
  ('valor -> CADENA','valor',1,'p_valor','sintactico.py',38),
  ('opcomparacion -> IGUAL','opcomparacion',1,'p_opcomparacion','sintactico.py',42),
  ('opcomparacion -> MAYOR','opcomparacion',1,'p_opcomparacion','sintactico.py',43),
  ('opcomparacion -> MENOR','opcomparacion',1,'p_opcomparacion','sintactico.py',44),
  ('opcomparacion -> MAYORIGUAL','opcomparacion',1,'p_opcomparacion','sintactico.py',45),
  ('opcomparacion -> MENORIGUAL','opcomparacion',1,'p_opcomparacion','sintactico.py',46),
  ('opcomparacion -> IS_NOT_EQUAL','opcomparacion',1,'p_opcomparacion','sintactico.py',47),
  ('expcmp -> valor opcomparacion valor','expcmp',3,'p_expresioncmp','sintactico.py',51),
  ('expcmp -> LPAREN valor opcomparacion valor RPAREN oplog LPAREN valor opcomparacion valor RPAREN','expcmp',11,'p_expresioncmp','sintactico.py',52),
  ('expcmplog -> expcmp oplog expcmp','expcmplog',3,'p_expresioncmplog','sintactico.py',57),
  ('expcmplog -> expcmp oplog expcmplog','expcmplog',3,'p_expresioncmplog','sintactico.py',58),
  ('oplog -> AND','oplog',1,'p_oplog','sintactico.py',62),
  ('oplog -> OR','oplog',1,'p_oplog','sintactico.py',63),
  ('comparacion -> IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE','comparacion',7,'p_comparacionif','sintactico.py',68),
  ('comparacion -> IF LPAREN expcmplog RPAREN LLLAVE sentencias RLLAVE','comparacion',7,'p_comparacionif','sintactico.py',69),
  ('comparacion -> IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE ELSE LLLAVE sentencias RLLAVE','comparacion',11,'p_comparacionif_else','sintactico.py',73),
  ('comparacion -> IF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE ELSEIF LPAREN expcmp RPAREN LLLAVE sentencias RLLAVE ELSE LLLAVE sentencias RLLAVE','comparacion',18,'p_comparacionif_elseif_else','sintactico.py',76),
  ('array -> ARRAY LPAREN valor DOUBLE_ARROW valor RPAREN','array',6,'p_array','sintactico.py',79),
  ('array -> ARRAY LPAREN valor RPAREN','array',4,'p_array','sintactico.py',80),
  ('sort -> SORT LPAREN ID RPAREN PCOMA','sort',5,'p_sort','sintactico.py',84),
  ('estdatos -> array','estdatos',1,'p_estdatos','sintactico.py',87),
  ('estdatos -> array_map','estdatos',1,'p_estdatos','sintactico.py',88),
  ('estdatos -> heap','estdatos',1,'p_estdatos','sintactico.py',89),
  ('expresionmat -> NUMBER operadormat NUMBER','expresionmat',3,'p_expresionmat','sintactico.py',92),
  ('operadormat -> PLUS','operadormat',1,'p_operadormat_plus','sintactico.py',108),
  ('operadormat -> MINUS','operadormat',1,'p_operadormat_plus','sintactico.py',109),
  ('operadormat -> TIMES','operadormat',1,'p_operadormat_plus','sintactico.py',110),
  ('operadormat -> DIVIDE','operadormat',1,'p_operadormat_plus','sintactico.py',111),
  ('expresion -> expresionmat','expresion',1,'p_expresion','sintactico.py',115),
  ('expresion -> expcmplog','expresion',1,'p_expresion','sintactico.py',116),
  ('funcion -> sort','funcion',1,'p_funcion','sintactico.py',118),
  ('funcion -> FUNCTION NFUNCION ID LPAREN args RPAREN LLLAVE sentencias RLLAVE','funcion',9,'p_funciondef','sintactico.py',121),
  ('funcion -> FUNCTION NFUNCION ID LPAREN args RPAREN LLLAVE sentencias RETURN valor PCOMA RLLAVE','funcion',12,'p_funciondef','sintactico.py',122),
  ('args -> ID','args',1,'p_args','sintactico.py',126),
  ('args -> ID args','args',2,'p_args','sintactico.py',127),
  ('excepcion -> TRY LLLAVE sentencias RLLAVE CATCH LPAREN EXCEPTION ID RPAREN LLLAVE ECHO CADENA COMA ID RLLAVE','excepcion',15,'p_excepcion','sintactico.py',130),
  ('impresion -> ECHO valor PCOMA','impresion',3,'p_impresion','sintactico.py',135),
  ('impresion -> PRINT valor PCOMA','impresion',3,'p_impresion','sintactico.py',136),
  ('impresion -> PRINT expresionmat PCOMA','impresion',3,'p_impresion','sintactico.py',137),
  ('repeticionrep -> MAYOR','repeticionrep',1,'p_repeticioncompfor','sintactico.py',141),
  ('repeticionrep -> MENOR','repeticionrep',1,'p_repeticioncompfor','sintactico.py',142),
  ('repeticionrep -> MAYORIGUAL','repeticionrep',1,'p_repeticioncompfor','sintactico.py',143),
  ('repeticionrep -> MENORIGUAL','repeticionrep',1,'p_repeticioncompfor','sintactico.py',144),
  ('actualizar -> INCREMENTO','actualizar',1,'p_actualizar','sintactico.py',147),
  ('actualizar -> DECREMENTO','actualizar',1,'p_actualizar','sintactico.py',148),
  ('repeticion -> FOR LPAREN ID ASIGNACION NUMBER PCOMA ID repeticionrep NUMBER PCOMA ID actualizar RPAREN LLLAVE sentencias RLLAVE','repeticion',16,'p_repeticionfor','sintactico.py',152),
  ('repeticion -> WHILE LPAREN ID opcomparacion valor RPAREN LLLAVE sentencias ID actualizar PCOMA RLLAVE','repeticion',12,'p_repeticionwhile','sintactico.py',157),
  ('repeticion -> DO LLLAVE sentencias ID actualizar PCOMA RLLAVE WHILE LPAREN ID opcomparacion valor RPAREN PCOMA','repeticion',14,'p_repeticionwhile','sintactico.py',158),
  ('array_map -> ARRAY_MAP LPAREN funcion COMA array RPAREN PCOMA','array_map',7,'p_array_map','sintactico.py',162),
  ('heap -> INSERT LPAREN LCORCH NUMBER COMA NUMBER RCORCH RPAREN PCOMA','heap',9,'p_heap','sintactico.py',165),
  ('heap -> INSERT LPAREN ARRAY LPAREN valor DOUBLE_ARROW NUMBER RPAREN RPAREN PCOMA','heap',10,'p_heap','sintactico.py',166),
]
