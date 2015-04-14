#Este encabezado nos hace tener codificacion utf-8 y usar caracteres especiales
# -*- coding: utf-8 -*-
#importamos tkinter para interfaz grafica
from Tkinter import *
#importamos los msgbox
import tkMessageBox
#importamos la libreria de la base de datos
import sqlite3
#creamos una clase ventana para organizar mejor el codigo
class Ventana:
	#metodo inicial
	def __init__(s):
		#se crea la variable v igual a tkinter
		s.v=Tk()
		#se crea una variable que va a contener la conexion ala base de datos
		s.conn = sqlite3.connect('base_d.db')
		#Se crea el menu
		s.menu=Menu(s.v)
		s.menu.add_command(label="Altas",command=lambda:s.draw("Altas"))
		s.menu.add_command(label="Bajas",command=lambda:s.draw("Bajas"))
		s.menu.add_command(label="Consultas",command=lambda:s.draw("Consultas"))
		s.menu.add_command(label="Actualizaciones",command=lambda:s.draw("Actualizaciones"))
		#se crea el diseño de la ventana
		s.fr=Frame(s.v)
		s.fr.pack()
		s.lb1=Label(s.fr,text="asd")
		s.lb2=Label(s.fr,text="Id")
		s.lb3=Label(s.fr,text="Nombre")
		s.lb4=Label(s.fr,text="Edad")
		#textbox
		s.ent1=Entry(s.fr)
		s.ent2=Entry(s.fr)
		s.ent3=Entry(s.fr)
		s.ent4=Entry(s.fr)
		#button
		s.btn1=Button(s.fr)
		#llamamos ala funcion draw y pasamos para que este de inicio en altas
		s.draw("Altas")
		#agregamos el menu
		s.v.config(menu=s.menu)
		#definimos el tamaño
		s.v.geometry("600x200")
		#usamos el loop principal para crear la ventan
		s.v.mainloop()
	#funcion para dibujar elementos recibe 2 parametros
	#el primero es s y es el metodo self para usar elementos de otros metodos
	#por segundo recibe en que vista se va a ver
	def draw(s,type):
		#con un if vemos en que vista estamos
		#cada vista tiene sus metodos en el boton
		#para que en altas se guarden
		#bajas se borren etc...
		if type=="Altas":
			s.lb1.config(text="Altas")
			s.btn1.config(text="Guardar",command=s.altas)
		elif type=="Bajas":
			s.lb1.config(text="Bajas")
			s.btn1.config(text="Borrar",command=s.bajas)
		elif type=="Consultas":
			s.lb1.config(text="Consultas")
			s.btn1.config(text="Consultar",command=s.consultas)
		elif type=="Actualizaciones":
			s.lb1.config(text="Actualizaciones")
			s.btn1.config(text="Actualizar",command=s.actualizaciones)
		#ponemos los elementos en forma de grid para mas sencilla distribucion
		#en forma de tabla
		s.lb1.grid(padx=10,pady=10,column=2,row=0)
		s.lb2.grid(padx=10,pady=10,column=1,row=1)
		s.lb3.grid(padx=10,pady=10,column=2,row=1)
		s.lb4.grid(padx=10,pady=10,column=3,row=1)
		#los textbox o entrys tambien los agregamos
		s.ent1.grid(padx=10,pady=10,column=1,row=2)
		s.ent2.grid(padx=10,pady=10,column=2,row=2)
		s.ent3.grid(padx=10,pady=10,column=3,row=2)
		#El boton lo agregamos
		s.btn1.grid(padx=10,pady=10,column=2,row=3)
	#ponemos en un try para controlar los errores
	#metodo altas para guardar datos
	def altas(s):
		try:
			#tomamos la variable conn y con el metodo execute
			#ejecutamos la insercion sql
			s.conn.execute("insert into users (id,nombre,edad) values('"+s.ent1.get()+"','"+s.ent2.get()+"','"+s.ent3.get()+"')")
			#con la funcion commit guardamos lo ejecutado
			s.conn.commit()
			#si todo va bien nos manda un mensaje
			tkMessageBox.showinfo("Sistema","Inserción correcta")
		except Exception, e:
			#si hay errores imprime en la consola el error
			print e
			#un msgbox de error
			tkMessageBox.showinfo("Sistema","error al ingresar")
	#dar de baja
	def bajas(s):
		try:
			#sql borrar
			s.conn.execute("delete from users where id='"+s.ent1.get()+"'")
			#guardar
			s.conn.commit()
			#mensaje
			tkMessageBox.showinfo("Sistema","Borrado")
		except Exception, e:
			print e
			tkMessageBox.showinfo("Sistema","error al borrar")
	#actualizar campos
	def actualizaciones(s):
		try:
			#sql
			s.conn.execute("update users set nombre='"+s.ent2.get()+"', edad='"+s.ent3.get()+"' where id='"+s.ent1.get()+"'")
			#guardar
			s.conn.commit()
			#mensaje
			tkMessageBox.showinfo("Sistema","Actualizado")
		except Exception, e:
			print e
			tkMessageBox.showinfo("Sistema","error al actualizar")
	#consultar
	def consultas(s):
		try:
			#en la variable data guardamos los datos de la consulta
			data=s.conn.execute("select * from users where id='"+s.ent1.get()+"'")
			s.conn.commit()
			#con un for recorremos los campos para mostrarlos
			for x in data:
				#en un mensaje mostramos el nombre y edad
				tkMessageBox.showinfo("Sistema","Nombre : "+x[1]+"\nEdad : "+x[2])
		except Exception, e:
			print e
			tkMessageBox.showinfo("Sistema","error al consultar")
#instanciamos la clase para iniciarla
v=Ventana()
