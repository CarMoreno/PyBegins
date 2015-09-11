class Humano:

	def __init__(self, edad, comida):
		#Atributos
		self.edad = edad 
		self.comida = comida

		#Metodos	
	def hablar(self, mensaje):#El atributo self hace referencia al objeto, no hay necesidad de mandar ese argumento cuando llamamos la funcion mas abajo, Python lo hace por si mismo. Lo importante son los argumentos que van despues del self
		#Si necesito la edad aca podemos hacer esto:
		#print self.edad #Llamamos la edad aca
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

#Pruebas			
pedro = IngSistemas() #Estas clases heredan de humano el metodo __init(self)__ por eso debemos de mandar los atributos edad y comida asi estemos instanciando desde las subclases
raul = LicDerecho(25, "Pescado")

raul.estudiarCaso("Pedro")
pedro.programar("Python")

pedro.hablar("Hola Raul")
raul.hablar("Hola Pedro")
