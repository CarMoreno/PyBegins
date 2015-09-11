def operador(n,m):
	if n == None:
		n = 0
	elif m == None:
		m = 0	
	return n+m


l1 = [1,2,3,4,5]
t1 = (9,8,7,6,)
t2 = (2,3,4)

lr = map(operador, l1, t1)#la funcion map recibe una funcion y dos objetos de secuencia, Los usa para armar una lista dependiendo de los procedimientos que se encuntre dentro de la funcion recibida, en este caso, sumara cada elemento de los dos objetos l1 y t1, y los guardara en una lista 
print "soy l1", l1
print "soy t1", t1
print "soy lr, ya he pasado por map", lr