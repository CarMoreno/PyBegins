from Humano import Humano
from IngSistemas import IngSistemas
from LicDerecho import LicDerecho

class main(object):

	print "-------------INGENIERO DE SISTEMAS-------------"
	ingS = IngSistemas("Carlos", "Moreno", 24, "Helado", 2500000, "8 horas diarias", "1 anio de experiencia")
	ingS.correr()
	ingS.hablar("Yo soy un ingeniero")
	ingS.programar("Python")
	ingS.getExperiencia()
	ingS.mayorDeEdad()
	print "Yo soy", ingS.getNombre()
	print "Me gusta mucho el/la", ingS.getComida()
	print "-------------LICENCIADO EN DERECHO-------------"
	licD = LicDerecho("Fulano", "De tal", 23, "Chocolate", "UTP", "Derecho Administrativo", 15)
	licD.correr()
	licD.hablar("Yo soy un Licenciado en Derecho")
	licD.mostrarUniversidad()
	licD.mayorDeEdad()
	print "Me gusta mucho el/la", licD.getComida()


