from Humano import Humano

class IngSistemas(Humano):#Esta clase hereda los metodos y atributos de la super clase persona, la clase de la cuale heredan se la pone entre parentesis
	
	def __init__(self, nombre, apellido, edad, comida, salario, horasLaborales, experiencia):#Podemos crear otro metodo init en una subclase, este tendra mas importancia que el de la super clase cuando instanciemos de la clase ingSistemas
		
		Humano.__init__(self, nombre, apellido, edad, comida)
		self.salario = salario
		self.horasLaborales = horasLaborales
		self.experiencia = experiencia
		#print "Ademas de ser un Humano, soy un ingeniero"

	def getSalario(self):
		return self.salario

	def getHorasLaborales(self):
		return self.horasLaborales

	def getExperiencia(self):
		return self.experiencia

	def programar(self, lenguaje):
		print "Yo programo en", lenguaje

		
