# Calculadora
import math
import tkinter as tk

primerNombre = ""
operacion = ""


def clear():
    global primerNombre, operacion
    quatreText.delete(0, tk.END)
    primerNombre = ""
    operacion = ""


def igual():
    global primerNombre, operacion
    segonNombre = quatreText.get()
    if primerNombre and segonNombre and operacion:
        try:
            if operacion == "+":
                resultat = str(float(primerNombre) + float(segonNombre))
            elif operacion == "-":
                resultat = str(float(primerNombre) - float(segonNombre))
            elif operacion == "*":
                resultat = str(float(primerNombre) * float(segonNombre))
            elif operacion == "/":
                if float(segonNombre) != 0:
                    resultat = str(float(primerNombre) / float(segonNombre))
                else:
                    resultat = "ERROR"
            quatreText.delete(0, tk.END)
            quatreText.insert(0, resultat)
        except ValueError:
            quatreText.delete(0, tk.END)
            quatreText.insert(0, "ERROR")


def click_boto(number):
    entrada_actual = quatreText.get()
    quatreText.delete(0, tk.END)
    quatreText.insert(0, entrada_actual + str(number))


def set_operacion(op):
    global operacion, primerNombre
    if primerNombre:
        igual()
    primerNombre = quatreText.get()
    operacion = op
    quatreText.delete(0, tk.END)


finestra = tk.Tk()
finestra.title("Calculadora")

quatreText = tk.Entry(finestra, font=("Courier", 10), width=30, borderwidth=2)
quatreText.grid(row=10, column=0, columnspan=4)

for i in range(10):
    boto = tk.Button(finestra, text=str(i), font=("Arial", 12), width=5, height=2, command=lambda i=i: click_boto(i))
    fila = (i - 1) // 3 + 1
    columna = (i - 1) % 3
    boto.grid(row=fila, column=columna)

botoClear = tk.Button(finestra, text="Clear", font=("Arial", 12), width=5, height=2, command=clear)
botoClear.grid(row=4, column=0)

botoSuma = tk.Button(finestra, text="+", font=("Arial", 12), width=5, height=2, command=lambda: set_operacion("+"))
botoSuma.grid(row=4, column=1)

botoResta = tk.Button(finestra, text="-", font=("Arial", 12), width=5, height=2, command=lambda: set_operacion("-"))
botoResta.grid(row=4, column=2)

botoMultiplicacio = tk.Button(finestra, text="*", font=("Arial", 12), width=5, height=2,
                              command=lambda: set_operacion("*"))
botoMultiplicacio.grid(row=5, column=1)

botoDivision = tk.Button(finestra, text="/", font=("Arial", 12), width=5, height=2, command=lambda: set_operacion("/"))
botoDivision.grid(row=5, column=2)

botoIgual = tk.Button(finestra, text="=", font=("Arial", 12), width=5, height=2, command=igual)
botoIgual.grid(row=5, column=0)

finestra.mainloop()
