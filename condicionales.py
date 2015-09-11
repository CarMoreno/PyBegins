#encoding: utf-8

#El primer comentario es par aque reconzca caracteres especiales
edad = 15
mayoriaEdad =  18

#Estructura if else
if edad >= mayoriaEdad:
	print "eres mayor de edad :)"
	if True:
		print "Esto se ejecuta siempre que seas mayor de edad" #Se ejecuta siempre este if pues le pasamos un True	
else:
	print "No eres mayor de edad :("		

print "esto no hace parte del if"

#Estructura if, else if, else if, else if, ...., else if, else
if edad>=0 and edad<18:
	print "Eres un niño"
elif edad>=18 and edad<27:
	print "Eres un joven"
elif edad>=27 and edad<60:
	print "Eres un adulto"
else:
	print "Eres de la tercera edad"	

#La sentencia switch en Python NO EXISTE			
