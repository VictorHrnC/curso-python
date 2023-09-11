    ### LISTAS ###
#LAS LISTAS ES UN CONJUNTO DE VARIABLES GRACIAS A PYTHON (DINAMICA) QUE NOS PERMITE ALMACENAR MAS DE 1 ELEMENTO
#DEFINIENDO UNA LISTA 

lista = list()
otra_lista  = []

lista = [25,35,18,25,14,24]

print(lista)
print(len(lista))

otra_lista = [25,1.83,"victor","hernandez"]

print(otra_lista[0])
print(otra_lista[3])
print(otra_lista[-2])
print(otra_lista[-3])


#agregar mas datos a una lista (va a agregar al final de a lista)
otra_lista.append("HMcaditor")
print(otra_lista)

#para insertar datos en una posicion deseada utilizamos insert.
otra_lista.insert(1,"purple")
print(otra_lista)

#eliminar valores de lista con pop 
lista.pop()
print(lista)

#almacenar valores eliminados con pop en otra lista
#definir una lista para almacenar valores eliminados
pop_list = []


#vamos a decir que nuestra lista adquiere el valor de lo que eliminamos
pop_list=[lista.pop()]


#imprimimos nuestra lista nueva 
print(lista)


#imprimimos nuestra lista de valores eliminados
print(pop_list)


#para agregar mas valores tenemos que avisarle al programa que nuestro nuevo valor de la lista de cosas eliminadas sera esa lista + el nuevo elemento eliminado
pop_list=pop_list+[lista.pop()]
print(lista)
print(pop_list)


#recordar que podemos hacer una copia de la lista definiendo una lista y haciendo una copia de ella con el comando .copy()
copia_lista=[]
copia_lista=otra_lista.copy()


"""esto nos sirve demaciado recordar que pyton es de tipado dinamico eso quiere decir que si en algun punto que estemos trabajando con otra persona y este dice que *otra_lista* 
ahora es un valor x, o decide eliminar los datos de la lista nosotros podemos acceder a la lista desde nuestra lista copiada, recordar que la lista copiada sera en el punto que hagamos la copia
"""
###caso en que cambiamos a int *puede ser cualquier valor no solo un entero* (quitar los # para comprobar)
# otra_lista=24
# print(otra_lista)
# print(copia_lista)
# ###

###caso en que eliminamos la lista (quitar los # para comprobar)
#otra_lista.clear()
# print(otra_lista)
# print(copia_lista)
# ###


###
# las tuplas son basicamente listas que no podemos modificar
###

tupla_de_lista= tuple(lista)
print(tupla_de_lista)
print(type(tupla_de_lista ))

###
# los sets son listas que no llevan un orden
# otra caracteristica importante es que no aceptan valores repetidos###

set = set()
setgundo = {}

setgundo = {"hola", "soy","set",2,"no", "lista"}

print(setgundo)

#verificando adicion de un valor existente
setgundo.add("hola")

print(setgundo)


setgundo.pop()
print(setgundo)

#comprobar si existe un dato en el set

print("hola" in  setgundo)


### Dicts ###

###
# un dict o diccionario es una lista que se relaciona mucho con un set siendo a diferencia de el set, ordenada y a diferencia de las listas este tipo de dato necesita
# que definamos con una credencial(lo que nosotros queramos nombrar) antes de el valor
# podemos agregar mas de 1 valor en estos###


er_dict = dict()
do_dict = {}

do_dict = {"nombre":"victor","apellido":"hernandez","edad":25,}
print(do_dict)

#introducioendo diferentes listas en dicts

lenguajes_set = ["javascrip", "python", "css", "c++"]

er_dict = do_dict.copy()

er_dict["lenguajes"]= lenguajes_set

print(er_dict)

#eliminar un elemento de un dict con del

do_dict["elemento"] = "elementoeliminado"

print(do_dict)

del do_dict["elemento"]

print(do_dict)
