#encoding: latin1
from Moneda import Moneda
from Persona import Persona
from Alcancia import Alcancia
class Ventana:
	persona = Persona()
	opcion = 0
	menu = {
		1: "Crear Moenda",
		2: "Ingresar Monedas",
		3: "Consultar Monedas",
		4: "Cuanto dinero tienes?",
		5: "Eliminar Moenda",
		6: "Generar Información",
		7: "Salir"
	}
	def __init__(self):
		pass

	# def mostrarEncabezado(self):
		

	def menu(self):
		print "-------------BIENVENIDO A SU ALCANCIA PORTATIL-------------\n======Creado por Carlos Andres Moreno======, \ncomo un ejercicio para aprender el lenguaje Python\n===email: carlosandresmorenovelez@gmail.com===\n\n"
		print """
		   ===MENU===
		1: Crear Moenda
		2: Ingresar Monedas
		3: Consultar Monedas
		4: Cuanto dinero tienes?
		5: Eliminar Moenda
		6: Generar Información,
		7: Salir\n"""
		opcion = int(raw_input("Que desea hacer?: "))

		if opcion == 1:
			print "Estas creando una moneda"
			denominacion = int(raw_input("Ingresa denominacion de la moneda: (100, 200, 500 o 1000): "))
			pais = (raw_input("Ingresa denominacion el pais donde se hizo tu moneda: "))
			yearFabrication = (raw_input("Ingresa el year de fabricacion de tu moneda: "))
			moneda = Moneda(denominacion, pais, yearFabrication)
			print "Moneda creada con exito !!!\n debe de ingresar su moneda a su alcancia antes de crear otra moneda"
		elif opcion == 2:
			desicion = raw_input("Quieres ingresar una moneda a tu alcancia? y/n: ")
			desicion.lower()
			if desicion == "y":
				self.persona.ingresarMoneda(moneda)
			else:
				"paila ya dijo que si"









	

