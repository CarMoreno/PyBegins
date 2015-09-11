#Un decorador es una funcion que recibe otra, la funcion decorador define otra funcion que es la que va a decorar
#la que le envie (resta en este caso)

loggueado = False

def admin(f):
	def comprueba(*args, **kwargs):
		if loggueado:
			f(*args, **kwargs)

		else:
			print "No tiene los permisos para ejecutar",f.__name__
	return comprueba			

def decorador (funcion):
	def funcionDecorada(*args, **kwargs):
		print "Funcion ejecutada", funcion.__name__
		funcion(*args, **kwargs)
	return funcionDecorada	

#La mejor forma, es colocando encima de la funcion que queremos decorar @nombefuncion, con esto nos ahorramos
#escribir decorador(resta)(arg1,arg2)

@decorador
@admin
#estos decoradores se ejecutan de abajo hacia arriba, primero se ejecuta el decorador @admin, luego @decorador
def hablar():
	print "Puedo hablar"

hablar()



 #El nombre de la funcion decoradora
def resta(n,m):
	print n-m

#resta(4,3)
#Decorando
#print decorador #Me retorna una funcion
#print decorador(resta)(3,4)

