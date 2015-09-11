#Declaracion de variables tipo cadena
cads = 'Cadena con comillas simples' #esto es una cadena con comillas simples
cadd = " Cadena con comillas dobles" #esto es una cadena con comillas dobles
minombre = "Carlos \n Andres \n Moreno \n Velez"
tabulacion = "***** \n\t ***** "#Primero espaciamos y luego  tabulamos  

cadc = """ Cada linea 1 
			linea 2
			linea 3
			linea 4
			.
			.
			.
			linea """ #Esto es una cadena entre comillas triples, podemos hacer saltos de linea y tabulaciones sin necesidad de usar \n y \t

repeticion = "repite " * 4 #Se repetira la cadena 4 veces

#********************************************************************************************************************
#***************************************BOOLEANOS*****************************************************************************

bT = True
bF = False

bAnd = bT and bF
bOr = bT or bF
bNot = not bT




#********************************************************************************************************************
#***************************************PRUEBAS**********************************************************************
#print type(cads) #la funcion type me permite saber el tipo de variable que esta entre los parentesis.
# print minombre
# print tabulacion
# print cadc
# print repeticion
# print cads + cadd #Asi se concatenan cadenas en python
print bT #Se muestra la variable bT
print bAnd
print bOr
print bNot



