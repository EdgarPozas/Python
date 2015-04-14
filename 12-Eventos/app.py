#importamos la libreria tkinter
#la cual contiene metodos para crear interfaces visuales
#desde tkinter importar todos los metodos
from Tkinter import *
#la libreria tkMessageBox nos permite usar cuadros de alerta o messagebox
import tkMessageBox
#hacemos una instancia de tkinter con Tk()
v=Tk()

#Esta es la funcion que al llamarla nos muestra el nombre 
def mostrarnombre():
	#usamos tkMessagebox + showinfo o uno de los siguientes metodos
	#showinfo()
	#showwarning()
	#showerror ()
	#askquestion()
	#askokcancel()
	#askyesno ()
	#askretrycancel ()
	#esta recibe como primer parametro el titulo y en segundo el contenido de el mensaje
	#con el metodo get() podemos tomar valor de un textbox Entry
	tkMessageBox.showinfo("Titulo","Tu nombre es : "+txt.get())

#pady indica que va a tener un padding en y de 10
Label(v,text="Ingresa tu nombre").pack(pady=10)
#para obtener los datos de un entry es recomendable definirlos de esta manera
#crear una variable para identidicarlo
txt=Entry(v,width=10)
txt.pack(pady=10)
#para decirle que va a hacer usamos el atributo command y le decimos que funcion va a realizar
#en este caso cuando le demos click
#va a ejecutar la función mostrar nombre
#la funcion debe de ser definida primero sino python no la reconocera
Button(v,text="Mostrar nombre",command=mostrarnombre).pack()


#definimos el titulo de la ventana
v.title("Titulo")

#definimos la geometria de la ventana
v.geometry("300x300")

#Creamos el loop principal el cual va a crear la ventana
v.mainloop()
