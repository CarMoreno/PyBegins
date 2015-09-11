diccionario ={
	"animales":["perro", "gato", "oso", "caballo"],
	"saludo": "hola",
	"year": 2015
}
otroDiccionario = diccionario.copy()#copia el diccionario a la variable otro diccionario
year = diccionario.pop("year", "No se encontro la clave dentro del diccionario") #Me saca el valor de la clave que le paso en los parentesis
#diccionario.clear() #me retorna un diccionario vacio
#diccionario["comida"] = ["arroz", "carne", "papas"]#agrego un nuevo elemento al dicc
del diccionario["animales"]
print year
print "saludo" in diccionario #Verificamos si una clave pertenece a un diccionario
print diccionario.items() #Devuelve una lista de tuplas, con el par clave,valor. No hay un orden
print diccionario.keys() #Devuelve una lista con todoas las claves del diccionario
print diccionario.values() #Devuelve una lista con todoas los valores del diccionario
print otroDiccionario