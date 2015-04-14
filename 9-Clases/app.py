#Creamos una clase o un objeto
#esta puede tener cualquier nombre
class Humano:
	#Este es el metodo que se va a ejecutar
	#cuando se cree una instanciade la clase
	#el parametro s es un valor automatico que hace que desde
	#cualquier punto de la clase se puedan acceder a los metodos
	def __init__(s):
		print "Esto es lo inicial"
		s.saluda()
	#Son metodos que puede realizar el humano
	def saluda(s):
		print "Te mano saludos"
	def adios(s):
		print "Adios"

#creamos en la variable H la instancia de la clase Humano
H=Humano()
#Podemos acceder al metodo adios desde la variable H
H.adios()