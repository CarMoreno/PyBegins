# s = (1,2,3,4)

# def sumar(n,m):
# 	return n+m

# respuesta = reduce(sumar, s)
# print respuesta

# #Reduce recibe una funcion y un objto iterable, la funcion debera tratar a cada uno de los elementos dentro
# #del obj iterable, en este caso los sumaremos. Lo que hay que entender es que reduce me permite realizar accines
# #que haya escrito en una funcion aparte, acciones que afectaran a los elementos de un obejto iterable

import sys
class Generador:

	def __init__(self, parent = None):
		self.numeros = [1,2,11,2,33] #Definimos un array donde se guardaran los aleatorios generados
		self.FO = [] #Definimos el vector de Frecuencias obtenidas

	def frecuenciasObtenidas(self):
		contador1 = 0
		contador2 = 0
		contador3 = 0
		contador4 = 0
		contador5 = 0
		contador6 = 0
		contador7 = 0
		contador8 = 0
		contador9 = 0
		contador10 = 0
		for i in self.numeros:
			i = i/10000.0 #Esto es para que caigan en el rango estipulado
			print i
			if i >= 0 and i < 0.1:
				contador1 += 1
			if i >= 0.1 and i < 0.2:
				contador2 += 1
			if i >= 0.2 and i < 0.3:
				contador3 += 1
			if i >= 0.3 and i < 0.4:
				contador4 += 1
			if i >= 0.4 and i < 0.5:
				contador5 += 1
			if i >= 0.5 and i < 0.6:
				contador6 += 1
			if i >= 0.6 and i < 0.7:
				contador7 += 1
			if i >= 0.7 and i < 0.8:
				contador8 += 1
			if i >= 0.8 and i < 0.9:
				contador9 += 1
			if i >= 0.9 and i < 1:
				contador10 += 1
		
		self.FO.append(contador1)
		self.FO.append(contador2)
		self.FO.append(contador3)
		self.FO.append(contador4)
		self.FO.append(contador5)
		self.FO.append(contador6)
		self.FO.append(contador7)
		self.FO.append(contador8)
		self.FO.append(contador9)
		self.FO.append(contador10)
		print "VECTOR DE FRECUENCIAS", self.FO
		#return self.FO
										
	# -------------------------------------Pruebas de uniformidad-------------------------------------
	def chiCuadrado(self):
		print "soy el vector de frecuencias obtenidas", self.FO

if __name__ == '__main__':
	gen = Generador()
	gen.frecuenciasObtenidas()
	gen.chiCuadrado()			