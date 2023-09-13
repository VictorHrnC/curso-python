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