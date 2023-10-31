# Ejercicio 23
import os
import tkinter as tk
from tkinter import filedialog as quelcom

from PIL import Image, ImageTk

imagenSeleccionada = None
imagenTk = None


def abrirImagen():
    global imagenSeleccionada, imagenTk

    carpetaOrigen = quelcom.askdirectory(initialdir=os.getcwd(), title='Seleccionar una carpeta de imágenes')

    if carpetaOrigen:
        archivos = os.listdir(carpetaOrigen)
        archivosImagen = [archivo for archivo in archivos if archivo.endswith('.jpg')]
        if not archivosImagen:
            etiquetaResultado.config(text='No se encontraron imágenes en la carpeta.')
            return

        imagenSeleccionada = os.path.join(carpetaOrigen, archivosImagen[0])
        ventanaSecundaria = tk.Toplevel()
        ventanaSecundaria.title('Imagen y ruta')

        etiquetaRuta = tk.Label(ventanaSecundaria, text=f'Ruta de la imagen:\n{imagenSeleccionada}')
        etiquetaRuta.pack()

        imagen = Image.open(imagenSeleccionada)
        imagenTk = ImageTk.PhotoImage(imagen)
        etiquetaImagen = tk.Label(ventanaSecundaria, image=imagenTk)
        etiquetaImagen.image = imagenTk
        etiquetaImagen.pack()

        botonGuardar = tk.Button(ventanaSecundaria, text='Guardar', command=guardarImagen)
        botonGuardar.pack()


def guardarImagen():
    if imagenSeleccionada:
        archivoGuardado = quelcom.asksaveasfile(defaultextension='.jpg', filetypes=[('Archivos de imagen', 'jpg')])
        if archivoGuardado:
            imagenOriginal = Image.open(imagenSeleccionada)
            imagenOriginal.save(archivoGuardado.name)
            archivoGuardado.close()
            etiquetaResultado.config(text='Imagen guardado correctamente.')


ventanaPrincipal = tk.Tk()
ventanaPrincipal.title('Abrir Imagen')

botonAbrir = tk.Button(ventanaPrincipal, text='Abrir Imagen', command=abrirImagen)
botonAbrir.pack()

etiquetaResultado = tk.Label(ventanaPrincipal, text='')
etiquetaResultado.pack()

ventanaPrincipal.mainloop()
