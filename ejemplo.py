import tkinter as tk
from tkinter import ttk


def presionado():
    caja_s.delete(0,tk.END)
    nombre = caja.get()
    #print("Hola "+nombre)
    frase ="Hola " + nombre
    caja_s.insert(0,frase)
    boton.config(text="Chau")



########################################

ventana = tk.Tk()
ventana.config(width=300,height=300)
ventana.title("Ejemplo")

boton = tk.Button(text="Hola",command=presionado)
boton.place(x=20,y=20,width=100,height=50)

caja = tk.Entry()
caja.place(x=20,y=120)

etq = tk.Label(text="Ingrese su nombre: ")
etq.place(x=20,y=90)

etqs = tk.Label(text="Saludo: ")
etqs.place(x=20,y=190)

caja_s = tk.Entry()
caja_s.place(x=20,y=220)

ventana.mainloop()