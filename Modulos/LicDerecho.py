from Humano import Humano

class LicDerecho(Humano):#Esta clase hereda los metodos y atributos de la super clase persona, la clase de la cuale heredan se la pone entre parentesis
	def __init__(self, nombre, apellido, edad, comida,  universidad, especialidad, cantidadLibros):
		Humano.__init__(self, nombre, apellido, edad, comida)
		self.universidad = universidad
		self.especialidad =  especialidad
		self.cantidadLibros = cantidadLibros

	def estudiarCaso(self, caso):
		print "Debo estudiar el caso", caso	

	def mostrarUniversidad(self):
		print self.nombre, "Se graduo en ", self.universidad

	def mostrarEspecialidad(self):
		print self.nombre, "Se especializa en ", self.especialidad

	def mostrarLibrosLeidos(self):
		print self.nombre, "Se ha leido ", self.libros

				