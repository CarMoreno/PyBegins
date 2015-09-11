#s = "0.12345"
#paises = "Colombia & Argentina & Estados Unidos & Chile & Venezuela"

#t = ("H","O","L","A")
#separador = "--"

#print len(s) #Me da la longitud de la cadena
#========================================================
#print s.count("o") #count(valor, inicio, fin), los dos ultimos args son opcionales. Cuenta cuntas veces se encuntra un caracter dentro de la cadena
#========================================================
# print s.count("5", 0, 1) #Cada letra de la cadena s tendra un indice como si fuera una lista. Los espacion tambien contaran como un caracter. Me va a buscar cuantas veces se esncutnra la letra o en la palabra la parte de la cadena que va desde el indice 0 hasta el indice 3 (hola)
# print s.count("5", 0, 2)
# print s.count("5", 0, 3)
# print s.count("5", 0, 4)
# print s.count("5", 1, 5)
# print s.lower()#Convierte la cadena en minusculas
# print s.upper()#convierte la cadena en mayusculas
# print s.replace("o", "*") #replace(valorAcambiar, nuevo, repetciones) #Me reemplazara el caracter o cadena viejo por uno nuevo las veces que yo le diga
# print s.replace("o", "*", 1) #Solo lo cambiara en la primera o.
# print s.replace("mundo", "universo")
# print paises.split("&") #split(separador, maxSplit)el maxSplit permite limitar el numero de veces que se va a separar la cadena
# print s.find("a") #find(valor, inicio, fin) busca un caracter y regresa el indice de el mismo
# print separador.join(t); #Retorna una cadena cuyos carecteres estaran separados por el separador
pseudoCadenas = ["0.11788","0.17788", "0.77881", 
				"0.22222", "0.11111", "0.00000",
				"0.12222", "0.00007", "0.10000",
				"0.33311", "0.00022", "0.22555",
				"0.22124", "0.41700", "0.24577",  
				"0.85376", "0.41727", "0.80969",
				"0.00034", "0.30004", "0.34000"]

# for i in pseudoCadenasEnteras:
# 	item = str(float(i)*100000)
# 	pseudoCadenas.append(item)

# print pseudoCadenas					
# entero = str(int(float(s)*100000))
# print type(entero)



# # pseudoCadenas = ["10321"]
todosDiferentes = 0 #d2stintos
unPar = 0 #solo un par
dosPares = 0 #dos pares de digitos
tercia = 0 #tres digitos iguales
full = 0 #tres digitos iguales y un par
poquer = 0 #4 digitos iguales
quintilla = 0 #5 digitos iguales
for j in pseudoCadenas:
		#los cinco digitos son iguales
		if j.count("0",2,7) == 5 or j.count("1",2,7) == 5 or j.count("2",2,7) == 5 or j.count("3",2,7) == 5 or j.count("4",2,7) == 5 or j.count("5",2,7) == 5 or j.count("6",2,7) == 5 or j.count("7",2,7) == 5 or j.count("8",2,7) == 5 or j.count("9",2,7) == 5:
			quintilla += 1
#  		#cuatro digitos iguales	
		elif j.count("0",2,6) == 4 or j.count("1",2,6) == 4 or j.count("2",2,6) == 4 or j.count("3",2,6) == 4 or j.count("4",2,6) == 4 or j.count("5",2,6) == 4 or j.count("6",2,6) == 4 or j.count("7",2,6) == 4 or j.count("8",2,6) == 4 or j.count("9",2,6) == 4:
					poquer += 1
		
		elif j.count("0",3,7) == 4 or j.count("1",3,7) == 4 or j.count("2",3,7) == 4 or j.count("3",3,7) == 4 or j.count("4",3,7) == 4 or j.count("5",3,7) == 4 or j.count("6",3,7) == 4 or j.count("7",3,7) == 4 or j.count("8",3,7) == 4 or j.count("9",3,7) == 4:	
			poquer += 1

# 		# #tres digitos iguales y un par
		elif j.count("0",2,5) == 3 and (j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2): 
			full += 1
		elif j.count("1",2,5) == 3 and (j.count("0",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2): 
			full += 1
		elif j.count("2",2,5) == 3 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2): 
			full += 1
		elif j.count("3",2,5) == 3 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2): 
			full += 1
		elif j.count("4",2,5) == 3 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2): 
			full += 1
		elif j.count("5",2,5) == 3 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2): 
			full += 1
		elif j.count("6",2,5) == 3 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2): 
			full += 1
		elif j.count("7",2,5) == 3 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2): 
			full += 1
		elif j.count("8",2,5) == 3 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("9",5,7) == 2): 
			full += 1
		elif j.count("9",2,5) == 3 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2): 
			full += 1								
# 	 	#==============
	 	elif j.count("0",2,4) == 2 and (j.count("1",4,7) == 3 or j.count("2",4,7) == 3 or j.count("3",4,7) == 3 or j.count("4",4,7) == 3 or j.count("5",4,7) == 3 or j.count("6",4,7) == 3 or j.count("7",4,7) == 3 or j.count("8",4,7) == 3 or j.count("9",4,7) == 3): 
			full += 1	
	 	elif j.count("1",2,4) == 2 and (j.count("0",4,7) == 3 or j.count("2",4,7) == 3 or j.count("3",4,7) == 3 or j.count("4",4,7) == 3 or j.count("5",4,7) == 3 or j.count("6",4,7) == 3 or j.count("7",4,7) == 3 or j.count("8",4,7) == 3 or j.count("9",4,7) == 3): 
			full += 1
		elif j.count("2",2,4) == 2 and (j.count("0",4,7) == 3 or j.count("1",4,7) == 3 or j.count("3",4,7) == 3 or j.count("4",4,7) == 3 or j.count("5",4,7) == 3 or j.count("6",4,7) == 3 or j.count("7",4,7) == 3 or j.count("8",4,7) == 3 or j.count("9",4,7) == 3): 
			full += 1
		elif j.count("3",2,4) == 2 and (j.count("0",4,7) == 3 or j.count("1",4,7) == 3 or j.count("2",4,7) == 3 or j.count("4",4,7) == 3 or j.count("5",4,7) == 3 or j.count("6",4,7) == 3 or j.count("7",4,7) == 3 or j.count("8",4,7) == 3 or j.count("9",4,7) == 3): 
			full += 1
		elif j.count("4",2,4) == 2 and (j.count("0",4,7) == 3 or j.count("1",4,7) == 3 or j.count("2",4,7) == 3 or j.count("3",4,7) == 3 or j.count("5",4,7) == 3 or j.count("6",4,7) == 3 or j.count("7",4,7) == 3 or j.count("8",4,7) == 3 or j.count("9",4,7) == 3): 
			full += 1			 	 	
		elif j.count("5",2,4) == 2 and (j.count("0",4,7) == 3 or j.count("1",4,7) == 3 or j.count("2",4,7) == 3 or j.count("3",4,7) == 3 or j.count("4",4,7) == 3 or j.count("6",4,7) == 3 or j.count("7",4,7) == 3 or j.count("8",4,7) == 3 or j.count("9",4,7) == 3): 
			full += 1
		elif j.count("6",2,4) == 2 and (j.count("0",4,7) == 3 or j.count("1",4,7) == 3 or j.count("2",4,7) == 3 or j.count("3",4,7) == 3 or j.count("4",4,7) == 3 or j.count("5",4,7) == 3 or j.count("7",4,7) == 3 or j.count("8",4,7) == 3 or j.count("9",4,7) == 3): 
			full += 1
		elif j.count("7",2,4) == 2 and (j.count("0",4,7) == 3 or j.count("1",4,7) == 3 or j.count("2",4,7) == 3 or j.count("3",4,7) == 3 or j.count("4",4,7) == 3 or j.count("5",4,7) == 3 or j.count("6",4,7) == 3 or j.count("8",4,7) == 3 or j.count("9",4,7) == 3): 
			full += 1
		elif j.count("8",2,4) == 2 and (j.count("0",4,7) == 3 or j.count("1",4,7) == 3 or j.count("2",4,7) == 3 or j.count("3",4,7) == 3 or j.count("4",4,7) == 3 or j.count("5",4,7) == 3 or j.count("6",4,7) == 3 or j.count("7",4,7) == 3 or j.count("9",4,7) == 3): 
			full += 1
		elif j.count("9",2,4) == 2 and (j.count("0",4,7) == 3 or j.count("1",4,7) == 3 or j.count("2",4,7) == 3 or j.count("3",4,7) == 3 or j.count("4",4,7) == 3 or j.count("5",4,7) == 3 or j.count("6",4,7) == 3 or j.count("7",4,7) == 3 or j.count("8",4,7) == 3): 
			full += 1					
					
# 		#tres digitos iguales
		elif j.count("0",2,5) == 3 or j.count("1",2,5) == 3 or j.count("2",2,5) == 3 or j.count("3",2,5) == 3 or j.count("4",2,5) == 3 or j.count("5",2,5) == 3 or j.count("6",2,5) == 3 or j.count("7",2,5) == 3 or j.count("8",2,5) == 3 or j.count("9",2,5) == 3:
			tercia += 1
		elif j.count("0",4,7) == 3 or j.count("1",4,7) == 3 or j.count("2",4,7) == 3 or j.count("3",4,7) == 3 or j.count("4",4,7) == 3 or j.count("5",4,7) == 3 or j.count("6",4,7) == 3 or j.count("7",4,7) == 3 or j.count("8",4,7) == 3 or j.count("9",4,7) == 3:
			tercia += 1 
		elif j.count("0",3,6) == 3 or j.count("1",3,6) == 3 or j.count("2",3,6) == 3 or j.count("3",3,6) == 3 or j.count("4",3,6) == 3 or j.count("5",3,6) == 3 or j.count("6",3,6) == 3 or j.count("7",3,6) == 3 or j.count("8",3,6) == 3 or j.count("9",3,6) == 3:
			tercia += 1

# 		#dos pares de digitos
		elif j.count("0",2,4) == 2 and (j.count("1",4,6) == 2 or j.count("2",4,6) == 2 or j.count("3",4,6) == 2 or j.count("4",4,6) == 2 or j.count("5",4,6) == 2 or j.count("6",4,6) == 2 or j.count("7",4,6) == 2 or j.count("8",4,6) == 2 or j.count("9",4,6) == 2) :
			dosPares += 1
		elif j.count("1",2,4) == 2 and (j.count("0",4,6) == 2 or j.count("2",4,6) == 2 or j.count("3",4,6) == 2 or j.count("4",4,6) == 2 or j.count("5",4,6) == 2 or j.count("6",4,6) == 2 or j.count("7",4,6) == 2 or j.count("8",4,6) == 2 or j.count("9",4,6) == 2) :
			dosPares += 1
		elif j.count("2",2,4) == 2 and (j.count("0",4,6) == 2 or j.count("1",4,6) == 2 or j.count("3",4,6) == 2 or j.count("4",4,6) == 2 or j.count("5",4,6) == 2 or j.count("6",4,6) == 2 or j.count("7",4,6) == 2 or j.count("8",4,6) == 2 or j.count("9",4,6) == 2) :
			dosPares += 1
		elif j.count("3",2,4) == 2 and (j.count("0",4,6) == 2 or j.count("1",4,6) == 2 or j.count("2",4,6) == 2 or j.count("4",4,6) == 2 or j.count("5",4,6) == 2 or j.count("6",4,6) == 2 or j.count("7",4,6) == 2 or j.count("8",4,6) == 2 or j.count("9",4,6) == 2) :
			dosPares += 1
		elif j.count("4",2,4) == 2 and (j.count("0",4,6) == 2 or j.count("1",4,6) == 2 or j.count("2",4,6) == 2 or j.count("3",4,6) == 2 or j.count("4",4,6) == 2 or j.count("6",4,6) == 2 or j.count("7",4,6) == 2 or j.count("8",4,6) == 2 or j.count("9",4,6) == 2) :
			dosPares += 1
		elif j.count("5",2,4) == 2 and (j.count("0",4,6) == 2 or j.count("1",4,6) == 2 or j.count("2",4,6) == 2 or j.count("3",4,6) == 2 or j.count("5",4,6) == 2 or j.count("6",4,6) == 2 or j.count("7",4,6) == 2 or j.count("8",4,6) == 2 or j.count("9",4,6) == 2) :
			dosPares += 1
		elif j.count("6",2,4) == 2 and (j.count("0",4,6) == 2 or j.count("1",4,6) == 2 or j.count("2",4,6) == 2 or j.count("3",4,6) == 2 or j.count("4",4,6) == 2 or j.count("5",4,6) == 2 or j.count("7",4,6) == 2 or j.count("8",4,6) == 2 or j.count("9",4,6) == 2) :
			dosPares += 1
		elif j.count("7",2,4) == 2 and (j.count("0",4,6) == 2 or j.count("1",4,6) == 2 or j.count("2",4,6) == 2 or j.count("3",4,6) == 2 or j.count("4",4,6) == 2 or j.count("5",4,6) == 2 or j.count("6",4,6) == 2 or j.count("8",4,6) == 2 or j.count("9",4,6) == 2) :
			dosPares += 1
		elif j.count("8",2,4) == 2 and (j.count("0",4,6) == 2 or j.count("1",4,6) == 2 or j.count("2",4,6) == 2 or j.count("3",4,6) == 2 or j.count("4",4,6) == 2 or j.count("5",4,6) == 2 or j.count("6",4,6) == 2 or j.count("7",4,6) == 2 or j.count("9",4,6) == 2) :
			dosPares += 1
		elif j.count("9",2,4) == 2 and (j.count("0",4,6) == 2 or j.count("1",4,6) == 2 or j.count("2",4,6) == 2 or j.count("3",4,6) == 2 or j.count("4",4,6) == 2 or j.count("5",4,6) == 2 or j.count("6",4,6) == 2 or j.count("7",4,6) == 2 or j.count("8",4,6) == 2) :
			dosPares += 1								
# 		# #==================
		elif j.count("0",3,5) == 2 and (j.count("1",4,7) == 2 or j.count("2",4,7) == 2 or j.count("3",4,7) == 2 or j.count("4",4,7) == 2 or j.count("5",4,7) == 2 or j.count("6",4,7) == 2 or j.count("7",4,7) == 2 or j.count("8",4,7) == 2 or j.count("9",4,7) == 2) :
			dosPares += 1
		elif j.count("1",3,5) == 2 and (j.count("0",4,7) == 2 or j.count("2",4,7) == 2 or j.count("3",4,7) == 2 or j.count("4",4,7) == 2 or j.count("5",4,7) == 2 or j.count("6",4,7) == 2 or j.count("7",4,7) == 2 or j.count("8",4,7) == 2 or j.count("9",4,7) == 2) :
			dosPares += 1
		elif j.count("2",3,5) == 2 and (j.count("0",4,7) == 2 or j.count("1",4,7) == 2 or j.count("3",4,7) == 2 or j.count("4",4,7) == 2 or j.count("5",4,7) == 2 or j.count("6",4,7) == 2 or j.count("7",4,7) == 2 or j.count("8",4,7) == 2 or j.count("9",4,7) == 2) :
			dosPares += 1
		elif j.count("3",3,5) == 2 and (j.count("0",4,7) == 2 or j.count("1",4,7) == 2 or j.count("2",4,7) == 2 or j.count("4",4,7) == 2 or j.count("5",4,7) == 2 or j.count("6",4,7) == 2 or j.count("7",4,7) == 2 or j.count("8",4,7) == 2 or j.count("9",4,7) == 2) :
			dosPares += 1
		elif j.count("4",3,5) == 2 and (j.count("0",4,7) == 2 or j.count("1",4,7) == 2 or j.count("2",4,7) == 2 or j.count("3",4,7) == 2 or j.count("4",4,7) == 2 or j.count("6",4,7) == 2 or j.count("7",4,7) == 2 or j.count("8",4,7) == 2 or j.count("9",4,7) == 2) :
			dosPares += 1
		elif j.count("5",3,5) == 2 and (j.count("0",4,7) == 2 or j.count("1",4,7) == 2 or j.count("2",4,7) == 2 or j.count("3",4,7) == 2 or j.count("5",4,7) == 2 or j.count("6",4,7) == 2 or j.count("7",4,7) == 2 or j.count("8",4,7) == 2 or j.count("9",4,7) == 2) :
			dosPares += 1
		elif j.count("6",3,5) == 2 and (j.count("0",4,7) == 2 or j.count("1",4,7) == 2 or j.count("2",4,7) == 2 or j.count("3",4,7) == 2 or j.count("4",4,7) == 2 or j.count("5",4,7) == 2 or j.count("7",4,7) == 2 or j.count("8",4,7) == 2 or j.count("9",4,7) == 2) :
			dosPares += 1
		elif j.count("7",3,5) == 2 and (j.count("0",4,7) == 2 or j.count("1",4,7) == 2 or j.count("2",4,7) == 2 or j.count("3",4,7) == 2 or j.count("4",4,7) == 2 or j.count("5",4,7) == 2 or j.count("6",4,7) == 2 or j.count("8",4,7) == 2 or j.count("9",4,7) == 2) :
			dosPares += 1
		elif j.count("8",3,5) == 2 and (j.count("0",4,7) == 2 or j.count("1",4,7) == 2 or j.count("2",4,7) == 2 or j.count("3",4,7) == 2 or j.count("4",4,7) == 2 or j.count("5",4,7) == 2 or j.count("6",4,7) == 2 or j.count("7",4,7) == 2 or j.count("9",4,7) == 2) :
			dosPares += 1
		elif j.count("9",3,5) == 2 and (j.count("0",4,7) == 2 or j.count("1",4,7) == 2 or j.count("2",4,7) == 2 or j.count("3",4,7) == 2 or j.count("4",4,7) == 2 or j.count("5",4,7) == 2 or j.count("6",4,7) == 2 or j.count("7",4,7) == 2 or j.count("8",4,7) == 2) :
			dosPares += 1									
# 		# #==============================
# 		#0,2-->3,5
		elif j.count("0",2,4) == 2 and (j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2) :
			dosPares += 1
		elif j.count("1",2,4) == 2 and (j.count("0",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2) :
			dosPares += 1
		elif j.count("2",2,4) == 2 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2) :
			dosPares += 1
		elif j.count("3",2,4) == 2 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2) :
			dosPares += 1
		elif j.count("4",2,4) == 2 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2) :
			dosPares += 1
		elif j.count("5",2,4) == 2 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2) :
			dosPares += 1
		elif j.count("6",2,4) == 2 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2) :
			dosPares += 1
		elif j.count("7",2,4) == 2 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2) :
			dosPares += 1
		elif j.count("8",2,4) == 2 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("9",5,7) == 2) :
			dosPares += 1
		elif j.count("9",2,4) == 2 and (j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2) :
			dosPares += 1	
		
# 		#Exactamente un par
		elif j.count("0",2,4) == 2 or j.count("1",2,4) == 2 or j.count("2",2,4) == 2 or j.count("3",2,4) == 2 or j.count("4",2,4) == 2 or j.count("5",2,4) == 2 or j.count("6",2,4) == 2 or j.count("7",2,4) == 2 or j.count("8",2,4) == 2 or j.count("9",2,4) == 2:
			unPar += 1
		elif j.count("0",3,5) == 2 or j.count("1",3,5) == 2 or j.count("2",3,5) == 2 or j.count("3",3,5) == 2 or j.count("4",3,5) == 2 or j.count("5",3,5) == 2 or j.count("6",3,5) == 2 or j.count("7",3,5) == 2 or j.count("8",3,5) == 2 or j.count("9",3,5) == 2:
			unPar += 1
		elif j.count("0",4,6) == 2 or j.count("1",4,6) == 2 or j.count("2",4,6) == 2 or j.count("3",4,6) == 2 or j.count("4",4,6) == 2 or j.count("5",4,6) == 2 or j.count("6",4,6) == 2 or j.count("7",4,6) == 2 or j.count("8",4,6) == 2 or j.count("9",4,6) == 2:
			unPar += 1
		elif j.count("0",5,7) == 2 or j.count("1",5,7) == 2 or j.count("2",5,7) == 2 or j.count("3",5,7) == 2 or j.count("4",5,7) == 2 or j.count("5",5,7) == 2 or j.count("6",5,7) == 2 or j.count("7",5,7) == 2 or j.count("8",5,7) == 2 or j.count("9",5,7) == 2:
			unPar += 1

		#diferentes
		else:
			todosDiferentes += 1
	

print "todos iguales", quintilla
print "4 iguales", poquer
print "tres iguales y un par", full
print "tres iguales solamente", tercia
print "dos pares", dosPares
print "un par solamente", unPar
print "todos diferentes", todosDiferentes