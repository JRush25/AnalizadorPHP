import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import  *
from PyQt5.QtCore import  *

import ply.yacc as yacc
import ply.lex as lex
import lexico



class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args,**kwargs)
        self.resize(720,600) #Tamaño

        #Cargar señales aqui abajo

        self.setWindowTitle("PHP Compiler")#Nombre de Ventana

        #Widgets
        label1 = QLabel("Toolbar") #Nombre de Toolbar
        label1.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label1)

        toolbar = QToolBar("Analizadores")
        toolbar.setIconSize(QSize(64,64))
        self.addToolBar(toolbar)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        #Acciones de Toolbar
        button_lexer = QAction(QIcon("LexBut.jpg"),"Analizador Lexico",self)
        button_lexer.setStatusTip("Lex")#Aparece abajo cuando paso el mouse
        button_lexer.triggered.connect(lambda x: self.onMyToolbarButtonLexico(x, label=label1))
        toolbar.addAction(button_lexer)#Se añadio el boton

        toolbar.addSeparator()

        button_sintax = QAction(QIcon("SinBut.jpg"), "Analizador Sintactico", self)
        button_sintax.setStatusTip("Syntax")
        button_sintax.triggered.connect(lambda x: self.onMyToolbarButtonSyntax(x, label=label1))
        toolbar.addAction(button_sintax)  # Se añadio el boton


        #Texto para escribir
        self.textArea = QPlainTextEdit(self)
        self.textArea.move(0,95)
        self.textArea.resize(360,480)

        #Resultado
        self.textArea = QPlainTextEdit(self)
        self.textArea.insertPlainText("Resultado\n")
        self.textArea.move(360, 95)
        self.textArea.resize(360, 480)
        self.textArea.setReadOnly(True)

        button_lexer.setCheckable(True) #Boton no ha sido seleccionado
        button_sintax.setCheckable(True) #Boton no ha sido seleccionado

        self.setStatusBar(QStatusBar(self))#Barra de Estado


    #Definimos los Slots(Comportamientos) que usaremos en signals

    #Slot Lexico
    def onMyToolbarButtonLexico(self,s,label):
        print("Analizador Lexico ON: ",s)
        lexer = lex.lex()
        label.setText("Tokenizer Finalizado")

    #Slot Sintactico
    def onMyToolbarButtonSyntax(self,s,label):
        print("Analizador Sintactico ON: ",s)
        label.setText("Sintaxis Finalizada")


    def onWindowTitleChange(self,s):
        print(s)


    #def contextMenuEvent(self, event):
     #   print("Hiciste clic en",event)


app = QApplication(sys.argv) #Llamamos a la App
window = MainWindow() #Llamamos a la ventana
window.show() #Mostramos la ventana
app.exec_()
print("Compiler Closed")




