#importamos la libreria tkinter
#la cual contiene metodos para crear interfaces visuales
#desde tkinter importar todos los metodos
from Tkinter import *

#hacemos una instancia de tkinter con Tk()
v=Tk()

#v es la ventana principal
#El metodo pack() empaqueta el objeto y lo muestra
#width es el ancho y height es el alto 

#Menu en la parte superior
#creamos el menu
menu=Menu(v)
#vamos añadiendo opciones con add_command()
#label es el texto que se va a mostrar
#tiene tambien el atributo command es lo que hara al darle click
menu.add_command(label="Menu")
#con esto indicamos que la ventana v es la que va a tener el menu
v.config(menu=menu)

#LabelFrame es un contenedor y recibe a donde se va a agregar y un texto
lp=LabelFrame(v,text="Titulo")

lp.pack()
Label(lp,text="Texto dentro de LabelFrame").pack()
#Label o etiqueda que indica texto
Label(v,text="Texto del label").pack()
Button(v,text="Button").pack()
#caja de texto en la cual puedes ingresar datos desde el teclado
Entry(v).pack()

#Radiobutton es un item que al darle click se queda seleccionado
Radiobutton(v,text="Holaa").pack()
#CheckBox cuadro donde al dar click aparece una palomita
Checkbutton(v,text="Holaa").pack()
Text(v,width=10,height=3).pack()
#listbox es una lista de items
lb=Listbox(v)
#el metodo insert recibe la posicion que se va a poner y el texto
lb.insert(1,"uno")
lb.insert(2,"uno")
lb.insert(3,"uno")
lb.insert(4,"uno")
lb.pack()

#definimos el titulo de la ventana
v.title("Titulo")
#definimos la geometria de la ventana
v.geometry("300x300")
#Creamos el loop principal el cual va a crear la ventana
v.mainloop()
