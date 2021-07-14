import tkinter
from tkinter import Tk
from lexico import analizar
import sintactico as sl

ventana = Tk()
ventana.geometry("800x640")


def analisisLexico(areaResultado, txt):
    areaResultado.delete("1.0", 'end-1c')
    linea = ""
    linea = analizar(txt)
    for variable in linea:
        areaResultado.insert(tkinter.INSERT, variable)
        areaResultado.insert(tkinter.INSERT, "\n")


def analisisSintactico(areaResultado, txt):
    areaResultado.delete("1.0", 'end-1c')
    sl.parser.parse(txt)
    if sl.error[0] != "":
        areaResultado.insert(tkinter.INSERT, sl.error[0])
        sl.error[0] = ""

    else:
        areaResultado.insert(tkinter.INSERT, "Analisis Sintactico Correcto")


def analizadorSintac(codigo_text_area):
    areaResultado.delete("1.0", 'end-1c')

    txt = areaCodigo.get("1.0", 'end-1c')

    if txt != "":
        analisisSintactico(areaResultado, txt)


def analizadorLex(codigo_text_area):
    areaResultado.delete("1.0", 'end-1c')

    txt = areaCodigo.get("1.0", 'end-1c')

    if txt != "":
        analisisLexico(areaResultado, txt)


etiqueta = tkinter.Label(ventana, text="Analizador PHP", font="Verdana", fg="blue")
etiqueta.place(x=50, y=10, width=150, height=50)

areaCodigo = tkinter.Text(ventana)
areaCodigo.configure(relief="raised", borderwidth=2)
areaCodigo.place(x=10, y=50, width=500, height=250)

btn_lex = tkinter.Button(ventana, text=" Analizador Lexico ", padx=20, pady=20, command=lambda: analizadorLex(areaCodigo))

btn_lex.place(x=10, y=300, width=150, height=50)

btn_sin = tkinter.Button(ventana, text="Analizador Sintactico", padx=20, pady=20, command=lambda: analizadorSintac(areaCodigo))

btn_sin.place(x=230, y=300, width=160, height=50)
areaResultado = tkinter.Text(ventana, height=5, width=40)
areaResultado.configure(relief="raised", borderwidth=2)
areaResultado.place(x=10, y=350, width=500, height=250)


ventana.mainloop()