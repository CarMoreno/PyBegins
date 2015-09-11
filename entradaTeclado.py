

try:
	valor = raw_input("Introduce un numero: ")
	valor = int(valor) #paso el numero de str a int
except:
	print "Eso no es un numero"
else:
	print valor		