import sqlite3
import tkinter as tk
from tkinter import messagebox


def insertarDatos():
    conexionBD = sqlite3.connect('data/basquet.db')
    cursorDN = conexionBD.cursor()

    nombre = entryNombre.get()
    apellido = entryApellido.get()
    altura = entryAltura.get()
    edad = entryEdad.get()

    cursorDN.execute('INSERT INTO jugadores (nombre, apellido, altura, edad) VALUES (?, ?, ?, ?)',
                     (nombre, apellido, altura, edad))

    conexionBD.commit()
    conexionBD.close()

    entryNombre.delete(0, tk.END)
    entryApellido.delete(0, tk.END)
    entryAltura.delete(0, tk.END)
    entryEdad.delete(0, tk.END)

    messagebox.showinfo('Éxito', 'Los datos se han insertado correctamente.')


def imprimirResultados():
    conexionBD = sqlite3.connect('data/basquet.db')
    cursorDN = conexionBD.cursor()

    # Ejecutar una consulta para obtener los datos de la tabla jugadores
    cursorDN.execute('SELECT * FROM jugadores')
    datos = cursorDN.fetchall()

    conexionBD.close()

    # Mostrar los resultados en una nueva ventana
    resultados_window = tk.Toplevel(ventana)
    resultados_window.title('Resultados de la Base de Datos')

    # Crear una etiqueta para mostrar los resultados
    resultados_label = tk.Label(resultados_window, text='Resultados:')
    resultados_label.pack()

    # Crear un widget Text para mostrar los datos
    resultados_text = tk.Text(resultados_window)
    resultados_text.pack()

    # Agregar los datos al widget Text
    for fila in datos:
        resultados_text.insert(tk.END, f'Nombre: {fila[1]}\n')
        resultados_text.insert(tk.END, f'Apellido: {fila[2]}\n')
        resultados_text.insert(tk.END, f'Altura: {fila[3]}\n')
        resultados_text.insert(tk.END, f'Edad: {fila[4]}\n\n')

    resultados_text.config(state=tk.DISABLED)  # Deshabilitar la edición del Text


ventana = tk.Tk()
ventana.title('Inserción de Datos')

labelNombre = tk.Label(ventana, text='Nombre:')
entryNombre = tk.Entry(ventana)

labelApellido = tk.Label(ventana, text='Apellido:')
entryApellido = tk.Entry(ventana)

labelAltura = tk.Label(ventana, text='Altura:')
entryAltura = tk.Entry(ventana)

labelEdad = tk.Label(ventana, text='Edad:')
entryEdad = tk.Entry(ventana)

botonInsertar = tk.Button(ventana, text='Insertar Datos', command=insertarDatos)
botonImprimir = tk.Button(ventana, text='Imprimir Resultados', command=imprimirResultados)

labelNombre.grid(row=0, column=0)
entryNombre.grid(row=0, column=1)

labelApellido.grid(row=1, column=0)
entryApellido.grid(row=1, column=1)

labelAltura.grid(row=2, column=0)
entryAltura.grid(row=2, column=1)

labelEdad.grid(row=3, column=0)
entryEdad.grid(row=3, column=1)

botonInsertar.grid(row=4, column=0, columnspan=2)
botonImprimir.grid(row=5, column=0, columnspan=2)

ventana.mainloop()
