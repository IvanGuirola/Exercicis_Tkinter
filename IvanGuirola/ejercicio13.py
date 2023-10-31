# Ejercicio 13 y 14
import os
from tkinter import *

from PIL import ImageTk, Image

rutaDirectorio = "./imagenes"
listaImagenes = os.listdir(rutaDirectorio)

indiceActual = 0
photoImages = []


def mostrarImage():
    global indiceActual

    if hasattr(mostrarImage, "imagenLabel"):
        mostrarImage.imagenLabel.grid_forget()

    imagenPath = os.path.join(rutaDirectorio, listaImagenes[indiceActual])
    print(imagenPath)

    imagen = Image.open(imagenPath)
    photo = ImageTk.PhotoImage(imagen)
    photoImages.append(photo)

    mostrarImage.imagenLabel = Label(root, image=photo)
    mostrarImage.imagenLabel.grid(row=0, column=0, padx=10, pady=10)

    if indiceActual == 0:
        botonAnterior.config(state=DISABLED)
    else:
        botonAnterior.config(state=NORMAL)

    if indiceActual == len(listaImagenes) - 1:
        botonSiguiente.config(state=DISABLED)
    else:
        botonSiguiente.config(state=NORMAL)

    infoEtiqueta.config(text=f"Imatge {indiceActual + 1} de {len(listaImagenes)}")


def siguienteImagen():
    global indiceActual
    indiceActual += 1
    mostrarImage()


def imagenAnterior():
    global indiceActual
    indiceActual -= 1
    mostrarImage()


root = Tk()
root.title("Visor de Imagenes")
root.geometry("800x800")

imagenFrame = LabelFrame(root, text="Imagenes", padx=100, pady=100)
imagenFrame.grid(row=0, column=0, padx=100, pady=100)

botonSiguiente = Button(root, text="Siguiente Fotografía", command=siguienteImagen)
botonAnterior = Button(root, text="Fotografía Anterior", command=imagenAnterior)
botonSalir = Button(root, text="Salir", command=root.quit)

botonSiguiente.grid(row=1, column=0, padx=10, pady=10)
botonAnterior.grid(row=1, column=1, padx=10, pady=10)
botonSalir.grid(row=1, column=2, padx=10, pady=10)

infoEtiqueta = Label(root, text="", bd=2, relief=SUNKEN, anchor=E)
infoEtiqueta.grid(row=2, column=0, columnspan=3, sticky=W + E)
infoEtiqueta.config(text=f"Imatge {indiceActual + 1} de {len(listaImagenes)}", anchor=E)

mostrarImage()

root.mainloop()
