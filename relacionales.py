# == operador de comparacion (si son iguales, entonces haga...)
# != operador de comparacion (si son diferentes, entonces haga...)
# > operador de comparacion (si a es mayor que b, entonces haga...) No se recomiendan usar en cadenas estos operadores             
# < operador de comparacion (si a es menor que b, entonces haga...) No se recomiendan usar en cadenas estos operadores                         
# >= operador de comparacion (si a es mayor o igual que b, entonces haga...)Ni estos tampoco                         
# <= operador de comparacion (si a es menor o igual que b, entonces haga...)Ni estos tampoco                         

v = "hola"
f = "adios"

lista1 = ["hola", "adios", True]
lista2 = ["hola", "adios", False]


r = lista1 == lista2 #Compara si son iguales
print r