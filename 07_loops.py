### LOOPS ###
### los loops o bucles o ciclos, son aquellos que nos permiten repetir cierta parte de nuestro codigo
# hasta que se cumpla nuestra condicion, hasta que se recorra lo que hayamos definido en nuestro loop###

# WHILE

condicion = 0

while condicion < 10:
    print(condicion)
    condicion += 5 #si no pusieramos esta operacion el print se ejecutaria infinitas veces con 0

print("seguimos programando...")

while condicion <=100:
    print(condicion)
    condicion *= 2
else: #los else son opcionales nos serviria para mostrar un mensaje que salimos de nuestro bucle
    print("salimos del loop while")
print("el valor de tu condicion es: " + str(condicion))


# FOR

#con el loop del for podemos listar un conunto de elementos 
#definiendo una de las listas que se vieron anteriormente 

lista = [25,35,18,25,14,24]

#podemos cin un iterador x recorrerla facilmente nombrando cada uno de los elementos sin necesidad de acceder con lo que seria lista[0] , lista[1] etc

for x in lista:
    print(x)