# import nombreModulo
# obj = nombreModulo.nombreClase()
#obj2 = nombreModulo.nombreOtraClase()

# otra forma puede ser:
# from nombreModulo import nombreClase
# obj = nombreClase()

class Humano(object):

	def __init__(self, nombre, apellido, edad, comida):
		#Atributos
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad 
		self.comida = comida

	def getNombre(self):
		return self.nombre

	def getApellido(self):
		return self.apellido

	def getEdad(self):
		return self.edad

	def getComida(self):
	    return self.comida				


		#Metodos	
	def hablar(self, mensaje):#El atributo self hace referencia al objeto, no hay necesidad de mandar ese argumento cuando llamamos la funcion mas abajo, Python lo hace por si mismo. Lo importante son los argumentos que van despues del self
		#Si necesito la edad aca podemos hacer esto:
		#print self.edad #Llamamos la edad aca
		print self.nombre, "dice: ", mensaje

	def correr(self):
		print self.nombre, "esta corriendo"	

	def mayorDeEdad(self):
		edad = self.edad
		if edad >= 18:
			print "eres mayor de edad"
		else:
			print "No eres mayor de edad"
