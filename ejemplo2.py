

import tkinter as tk
from tkinter import ttk

def nuevo():
    print("Nuevo archivo.")

def acerca_de():
    print("Acerca de:")


ventana_principal = tk.Tk()
ventana_principal.title("Mi primera aplicación")

barra_de_menu = tk.Menu()

menu_archivo = tk.Menu(barra_de_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo",command=nuevo)

menu_ayuda = tk.Menu(barra_de_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de...",command=acerca_de)

barra_de_menu.add_cascade(label="Archivo",menu=menu_archivo)
barra_de_menu.add_cascade(label="Ayuda",menu=menu_ayuda)

ventana_principal.config(width=300, height=200,menu=barra_de_menu)
ventana_principal.mainloop()