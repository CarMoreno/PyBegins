def filtro (elem):
	# if elem % 2 == 0:
	# 	return elem
	if elem == "r":
		return elem


l = [1,2,3,4,5,6,7,8,9,10,11,12]
nombre = "Carlos Andres Moreno Velez"
lr = filter(filtro, nombre)#Segun el tipo de objeto iterable que le pasemos a filter, asi sera el tipo del objeto que nos dara como resultado

print "Soy nombre ", nombre
print "He pasado por filter, ahora soy lr ", lr

#Filter recibe una funcion y un objeto iterable, lo que hace filter es que en base a la funcion dada
#(que debe de tener una condicion), me va a construir una lista solamente con aquellos elementos que pasen
#la condicion de la funcion que recibe