#Esata funcion recibe como paramentro a otra, y la retorna

def prueba(f):#Aca resiviremos una definion de una funcion
	return f() #Aqui estamos regresando el valor de la funcion por enviar

def porEnviar():
	return 2+2

#print prueba(porEnviar)	#Debemos de escribir el nombre de la funcion sin parentesis porque debemos enviarle a prueba una deinicion de funcion, si le ponemos los parentesis le estariamos en viando un 4, en vez de una definicion de funcion	
def seleccion(operacion):
	def suma(n,m):
		return n + m
	def multi(n,m):
		return n*m	

	if operacion == "suma":
		return suma
	elif operacion == "multi":
		return multi

funcionGuardada = seleccion("suma")#Como opercion es igual a "suma" entonces le pasamos a una variable, toda la defincion de la funcion suma, conviertirndo a la variable en una funcion
print funcionGuardada(4,5)	
