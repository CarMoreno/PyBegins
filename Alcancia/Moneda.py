class Moneda:
	#Una moneda tiene una denominacion, un pais donde fue creada esa moenad y un a;nio de fabricacion

	def __init__(self, denominacion=0, pais="*", yearFabrication="*"):
		self.denominacion = denominacion
		self.pais = pais
		self.yearFabrication = yearFabrication

	def getDenominacion(self):
		return self.denominacion

	def getPais(self):
		return self.pais

	def getYearFabrication(self):
		return self.yearFabrication

	def getInfoMoneda(self):
		print "Usted tiene una moneda de:", self.getDenominacion(), "\nSu moneda fue fabricada en:", self.getPais(), "\nSu moneda fue fabricada en el year de:", self.getYearFabrication()	

					