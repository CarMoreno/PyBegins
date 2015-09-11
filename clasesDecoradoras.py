# def decorador (funcion):
# 	def funcionDecorada(*args, **kwargs):
# 		print "Funcion ejecutada", funcion.__name__
# 		funcion(*args, **kwargs)
# 	return funcionDecorada	


class Decorador:
	def __init__(self, funcion):
		self.funcion = funcion

	def __call__(self, *args, **kwargs):#esta hara las veces de funcion decoradora
		print "Funcion ejecutada", self.funcion.__name__	
		self.funcion(*args, **kwargs)



@Decorador
def resta(n,m):
	print n-m	

resta (3,1)	