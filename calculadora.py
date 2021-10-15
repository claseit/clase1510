import tkinter as tk

def convertir(valor):
    try:
        valor = float(valor)
    except ValueError:
        valor = "error"
    return valor


def sumar():
    a = cuno.get()
    a = convertir(a)
    b = cdos.get()
    b = convertir(b)
    if a != "error" and b != "error":
        c = a + b
    else:
        c = "error"
    ctres.insert(0,c)





######################################

ventana = tk.Tk()
ventana.config(width=300,height=300)
ventana.title("Calculadora v2.1")


euno = tk.Label(text="Dato uno:")
euno.place(x=20,y=20)
cuno = tk.Entry()
cuno.place(x=20, y=50)

edos = tk.Label(text="Dato dos:")
edos.place(x=160,y=20)
cdos = tk.Entry()
cdos.place(x=160,y=50)

bsuma = tk.Button(text=" + ",command=sumar)
bsuma.place(x=20,y=100)

bresta = tk.Button(text=" - ")
bresta.place(x=100,y=100)

bmult = tk.Button(text=" x ")
bmult.place(x=180,y=100)

bdiv = tk.Button(text=" / ")
bdiv.place(x=260,y=100)

etres = tk.Label(text="Resultado:")
etres.place(x=90,y=150)
ctres = tk.Entry()
ctres.place(x=90,y=180)

binfo = tk.Button(text="Info")
binfo.place(x=40,y=230,width=100,height=40)

binfo = tk.Button(text="Salir")
binfo.place(x=160,y=230,width=100,height=40)


ventana.mainloop()