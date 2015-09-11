#Las listas son colecciones ordenadas y es lo equivalente a los arreglos o vectores en otros lenguajes de programacion
#Las listas pueden tener numeros, cadenas, booleanos o incluso otras listas
# l = [2, "tres", True, ["Carlos", "Moreno", 10]]
# l2 = l[1] #Accedemos al elemento cuyo indice es el 1 ("tres")
# l3 = l[3][0] #Accedemos al elemento de indice 3, pero como este es una lista, podemos acceder tambien al elemento de indice 0 de esta ("Carlos")
# l4 = l[0:3] #hace una lista que empieza desde el indice 0, y tendra los 3 primeros elementos l[indice:numeroElementos]
# #Vamos a cambiar el contenido del elemento cuyo indice es 1
# l5 = l[0:3:2]#hace una lista que empieza desde el indice 0, participaran los 3 primeros elementos, pero hara un salteado de uno en uno. Es decir, esta lista contendra uno si y uno no (salteados de uno en uno) l[indice:numeroElementos:salto+1]
# l[1] = 12

# l[1:2] = ["Hola", 123] #cambiamos el contenido de el indice que empieza en uno y participa tambien el elemento despues del de indice 1
# cambio = l[1]
# l = "0.41355"
# diferentes = 0
# if l[2] != l[3] and l[3] != l[4] and l[4] != l[5]and l[5] != l[6]:
#   diferentes += 1 
# print diferentes        
#**********************************************PRUEBAS***************************************************************
a = 0
l = []
for i in range(9):
	a = 0.1
	l.append(a)

print l	