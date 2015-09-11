class Humano:

	def __init__(self, edad, comida):
		#Atributos
		self.edad = edad 
		self.comida = comida

		#Metodos	
	def hablar(self, mensaje):
		print mensaje
	def mayorDeEdad(self):
		edad = self.edad
		if edad >= 18:
			print "eres mayor de edad"
		else:
			print "No eres mayor de edad"

class IngSistemas(Humano):#Esta clase hereda los metodos y atributos de la super clase persona, la clase de la cuale heredan se la pone entre parentesis
	def __init__(self):#Podemos crear otro metodo init en una subclase, este tendra mas importancia que el de la super clase cuando instanciemos de la clase ingSistemas
		print "Soy el constructor de la clase ing de sistemas"

	def programar(self, lenguaje):
		print "Yo programo en", lenguaje

class LicDerecho(Humano):#Esta clase hereda los metodos y atributos de la super clase persona, la clase de la cuale heredan se la pone entre parentesis
	def estudiarCaso(self, de):
		print "Debo estudiar el caso", de		

class Estudioso(IngSistemas, LicDerecho):#El orden en que pongo las clases de las cuales heredan es muy importante, ya que mi clase Estudioso va a tomar el __init(self)__ de la primera clase que yo ponga dentro de los parentiesis, en este case, me toma el init de la clase IngSistemas
	pass #Con esta palabra reservada de Python decimos que la clase Estudioso no va a tener ni metodos ni atributos propios. Algo asi como pasa...no hay nada que ver, va a heredar de la clase IngSistemas, LicDerecho y tambien de Humano (debido a que las dos anteriores lo hacen)

#Pruebas			
pepe = Estudioso()
pepe.hablar("Hola, yo soy pepe")
pepe.programar("JavaScript")
pepe.estudiarCaso("Ana")