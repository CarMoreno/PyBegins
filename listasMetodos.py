lista = [1, 1, 2, 6]
# elemento = "dos"
# otraLista = [2,4,"cinco","adios"]
# #PRUEBAS

# lista.append("Nuevo Elemento") #Asi se agrega un nuevo elemento a la lista
# lista.insert(0, "Hellow world") # En el primer indice del arreglo me agregaara el elemento "hellow world" y me correra los otros elementos
# lista.extend(otraLista )#aca puede ir una tupla o una cadena. extend() Une una lista con otra variable que sea iterable
# #lista.pop(1) #saca de la lista un elemento que coincide con el indice dado entre los parentesis, cuando lo necesitamos por ejemplo para alamacenarlo en una variable o cualquier cosa
# lista.reverse()#Me cambia el orden de la lista ["hi,3,"dos",1]
# lista.remove("hi") #Borra un elemento de una lista (no se le pasa un indice, sino el elemento como tal)
# print elemento in lista  #devuelve true si el elemento esta en la lista y false en caso contrario
#print lista.index(elemento) #me devuelve el indice del elemento que le paso en los parentesis, si el elemento no esta en la lista, me saldra un error
# print lista
# print lista.count(1) #Me imprimer el numero de veces que se ecuntra un elemento dentro de una lista




# if elemento in lista:
# 	print "el elemento ", elemento, " esta en la lista y su indice es: ", lista.index(elemento)
# else:
# 	print "El elemento no esta en la lista"	
#Arreglo que tiene 3 items entre 0 y 0.1, 2 items entre 0.4 y 0.5, y 3 items entre 0.2 y 0.3 

def countSeq(src):
  last = src[0]
  count = 0
  current = 1
  while current < len(src):
    if src[current] != last:
      count += 1
      last = src[current]
    current += 1
  return count + 1 # last


# corridas = []
# for i in xrange(0, len(lista)):#Para cada elemento de mi vector de numeros aleatorios no repetidos
# 	if lista[i] < lista[i+1]:
# 		corridas.append(1)
# 	elif lista[i] > lista[i+1]:
# 		corridas.append(0)
# 	else:
# 		print "Vaya, son iguales !, ESTO NUNCA DEBE PASAR"
# print corridas	

#-------------------------------------------------------------------------------------------------------------
# 	def getaAbs(self):#Me retorna el numero de corridas dentro del arreglo
# 		corridas = self.getCorridas()

# 		last = corridas[0]
# 		aAbs = 0
# 		current = 1
# 		while current < len(corridas):
# 			if corridas[current] != last:
# 				aAbs += 1
# 				last = corridas[current]
# 				current += 1
# 		return aAbs + 1 # last

# 	def pruebaCorrida(self):
# 		aAbs = self.getaAbs()#Obtengo el numero de corridas del arreglo
# 		media = (2*len(self.nuemros) - 1)*1.0 / 3
# 		varianza = (16*len(self.nuemros) - 29)*1.0 / 90
# 		zAbs = (aAbs - media)*1.0 / sqrt(varianza)

# 		if zAbs >= -1.96 and zAbs <= 1.96:
# 			QtGui.QMessageBox.information(self, "Informacion de Corrida", 
# 						"""Prueba de Corrida dice:

# Usando Alpha = 0.05, la prueba de Corrida encontro que usted hizo 
# una buena eleccion, no hay evidencia para rechazar la hipotesis de independencia.""", QtGui.QMessageBox.Ok)
# 		else:
# 			QtGui.QMessageBox.information(self, "Informacion de Corrida", 
# 						"""Prueba de Corrida dice:

# Usando Alpha = 0.05, la prueba de Corrida encontro que usted hizo 
# una mala eleccion, hay evidencia para rechazar la hipotesis de independencia.""", QtGui.QMessageBox.Ok)	
