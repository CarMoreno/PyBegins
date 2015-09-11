class Prueba:
	def __init__(self):
		#atributos
		self.__atributoPrivate = "Soy atributo privado"
		self.atributoPublico = "Soy atributo publico"

	#metodos
	def metodoPubico(self):
		print "Soy un metodo publico"
	def __metodoPrivado(self):
		print "Soy un metodo privado"
	#Para accder a un metodo privado de la clase debemos hacerlo con los getters
	def getAtrprivate(self):
		return self.__atributoPrivate
	#para cambiar el valor de un atributo privado dentro de la clase, usamos los setters
	def setAtrprivate(self, atributoPrivate):
		self.__atributoPrivate = atributoPrivate	


obj = Prueba()
obj.metodoPubico()
obj.setAtrprivate("Soy un atributo privado, me han modificado")
print obj.getAtrprivate()
print obj.atributoPublico
#print obj.__atributoPrivate #El objeto de esa clase no tiene acceso al atributo ni metodo privado

				