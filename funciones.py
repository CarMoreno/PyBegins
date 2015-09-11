def miFuncion(num1, num2):
	print num1 + num2

def otraFuncion(num1=4, num2=3):
	print num1 + num2

def funcionQueRetorna(num1, num2):
	return num1 - num2


miFuncion(5,1)
otraFuncion() #Si no le mando ningun argumento a esta funcion, se tomaran los que tiene [por default cuando definimos la misma
otraFuncion(3,10) #Si le enviamos argumentos a la funcion, entonces se tomaran los enviados y se ignoraran los que definimos por default
otraFuncion(12) #Aca solo enviamos el primer argumento a la funcion, por lo que el segundo argumento sera el que definimos anteriormente por default
resta = funcionQueRetorna(10,2)
print resta