class Humano:

	def __init__(self, edad, comida):
		#Atributos
		#self.edad = 25 #Estos atributos son estaticos, cuando yo cree un objeto humano la edad y la comida siempre seran las mismas
		#self.comida = "Carne"
		self.edad = edad #con esto conseguimos que la edad y la comida sea dinamica, es decir que toma valores que yo le mande al objeto AL MOMENTO DE CREARLO
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



#Pruebas
pedro = Humano(23, "Arroz")
raul = Humano(18, "Carne")

print "Soy Pedro y tengo ", pedro.edad, " y me gusta el ", pedro.comida
print "Soy Raul y tengo ", raul.edad, " y me gusta la ", raul.comida
print "-------------------------------------------------------------"
pedro.hablar("Hola Raul")
raul.hablar("Hola Pedro")
pedro.mayorDeEdad()
raul.mayorDeEdad()
