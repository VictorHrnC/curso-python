### FUNCIONES ###

#las funciones son basicamente operaciones que necesitaremos realizar varias veces dentro de nuestro codigo sumas restas, validaciones ifs, loops para encontrar x valor etc
#se utilizan como una buena practica de programacion para mantener un orden teniendo nuesto codigo en la rama de main mas limpio y facil de trabajar (o por lo menos asi lo veo yo)

#para definir una funcion devemos utilizar la palabra reservada def seguido del nombre de nuestra funcion con un (donde especificaremos los datos que trabajemos) en caso de
#no recibir valores se ejecutara lo que este dentro de la funcion

#ejemplo funcion de saludo por un print

def saludo():
    print("hola soy una funcion")

#las funciones las llamamos con su nombre de la siguiente manera

saludo()

#probando funciones con operadores 

def suma(x, y):
    return (x+y)

def resta(x, y):
    return (x-y)

def division(x, y):
    return (x/y)

def multiplicacion(x, y):
    return (x*y)
#funcion para saltar linea en terminal
def salto():
    cadena_saltos=print("*");print("*");print("*");print("*");print("*");print("*");print("*");print("*");print("*");print("*");print("*");print("*");print("*********************************************************************************")
    return(cadena_saltos)
#hagamoslo mas interactivo trabajemos con terminal :D
#debemos de ingresar numeros ya que utilizamos operadores aritmeticos en caso de la suma vamos a concatenar strings pero en el resto de operaciones esto nos dara errores
#para hacer esto mas completo deberiamos de aplicar todos los conocimientos hasta ahora ya sea while para hacer que llegue un valor que de verdad sea de tipo entero
#un if para que el valor del segundo numero sea mayor a 0 (por nuestra division)
#por lo cual para no enredar con tanto codigo al ser un curso para principiantes no se hara  
print("ingresa un numero")
valor=int(input())
print("ingresa otro numero")
dovalor= int(input())
resultado = suma(valor, dovalor)

#recordar que para un mejor trabajo con pyton utilizamos formatos para los strings asi nuestro programa sabe que estamos trabajando con numeros (revisar 04_stings line25)
#formatealos como tu gustes 

print("el resultado de la suma de %d + %d es: %d" %(valor,dovalor,resultado))
resultado = resta(valor, dovalor)
print("el resultado de la resta de %d + %d es: %d" %(valor,dovalor,resultado))
resultado = multiplicacion(valor, dovalor)
print("el resultado de la multiplicacion de %d + %d es: %d" %(valor,dovalor,resultado))
resultado = division(valor, dovalor)
print("el resultado de la division de %d + %d es: %d" %(valor,dovalor,resultado))

"""
veamos el caso de un login basico con un loop while, listas, variables 
utilicemos nuestro conocimiento (accede a los puntos si es que es necesario revisa ficheros)
interactuemos con la terminal
"""
userl=[]
userl2=[]
print("ingresa tu usuario para registrar")
userx=input()
userl.insert(0,userx)
print("ingresa tu contraseña para registrar")
contraseñax=input()
userl.insert(1,contraseñax)
salto()
print("registro exitoso")
print("ingrese su usuario para verificar")
user=input()
userl2.insert(0,user)
print("ingresa su contraseña para verificar")
contraseña=input()
userl2.insert(1,contraseña)
#luego veremos como llamar esta 
def validacion(user,usercompare):
    while user[0] == usercompare[0]:
        print("el valor ingresado no es valido, ingrese el valor")
        user=input()
        userl2.insert(0,user)
validacion(userl2,userl)
print("continuamos programando")