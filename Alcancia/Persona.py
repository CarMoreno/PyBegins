from Moneda import Moneda

class Persona:
	monedas = []

	def __init__ (self):
		pass		

	def getMonedas(self):
		return monedas
			
	def agregarMoneda(self, moneda):
		self.monedas.append(moneda)
		return self.monedas

	def eliminarMoneda(self, denominacion):
			for mon in self.monedas:
				if denominacion == mon.getDenominacion():
					self.monedas.remove(mon)
				else:
					"No tienes una moneda de",denominacion,"en tu alcancia"		

	def consultarMonedaPorDeno(self, denominacion):
		contador = 0
		for mon in self.monedas:
			if denominacion == mon.getDenominacion():
				contador = contador + 1
			else:
				"No tienes moendas de esa denominacion"
		print "Tienes", contador, "monedas de", denominacion
					
	def consultarSaldo(self):
		total = 0
		for mon in self.monedas:
			total += mon.getDenominacion()
		print "Tienes en la alcancia",total,"pesos"	


	def darInfo(self):
		indice = 0
		for mon in self.monedas:
			print "Moneda", indice, " Moneda de:", mon.getDenominacion(), "\n\t  Hecha en:", mon.getPais(), "\n\t  En el year", mon.getYearFabrication(),"\n"
			indice = indice + 1	




	