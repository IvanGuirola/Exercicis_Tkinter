# Ejercicio 19
import tkinter as tk
from tkinter import messagebox


def mostrarVentanaDePregunta():
    respuesta = messagebox.askquestion('Pregunta', 'Quieres continuar?')
    etiquetaResultado.config(text=f'Has clicado {"si" if respuesta == "yes" else "no"}')


def mostrarVentanaOkCancel():
    respuesta = messagebox.askokcancel('Pregunta', 'Estas seguro de que quieres hacer esto?')
    etiquetaResultado.config(text=f'Has clicado {"si" if respuesta else "no"}')


def mostrarVentanaYesNo():
    respuesta = messagebox.askyesno('Pregunta', 'Estas de acuerdo?')
    etiquetaResultado.config(text=f'Has clicado {"si" if respuesta else "no"}')


ventanaPrincipal = tk.Tk()
ventanaPrincipal.title('Ventanas Emergentes')

etiquetaResultado = tk.Label(ventanaPrincipal, text="")
etiquetaResultado.pack()

botonPregunta = tk.Button(ventanaPrincipal, text='Pregunta', command=mostrarVentanaDePregunta)
botonOkCancel = tk.Button(ventanaPrincipal, text='OK/Cancel', command=mostrarVentanaOkCancel)
botonYesNo = tk.Button(ventanaPrincipal, text='YES/NO', command=mostrarVentanaYesNo)

botonPregunta.pack()
botonYesNo.pack()
botonOkCancel.pack()

ventanaPrincipal.mainloop()
