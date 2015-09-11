#Los diccionarios no cuentan con un indice como las tuplas o listas, cuentan con una clave
#Los pares que se muestran son clave:valor
d = {
	"nombre": "Carlos",
	"apellido": "Moreno",
	"edad": 19,
	"lenguajes":["Phyton", "Javascript", "Css", "Html", True]
}
d["nombre"] = "Carlos Andres"

#En los diccionarios podemos modificar el valor de una clave, pero no podemos modificar la clave

print d["lenguajes"] #Asi accesamos un elemento dentro de un diccionarios
print d["nombre"] #Las CLAVES pueden ser tambien numericas