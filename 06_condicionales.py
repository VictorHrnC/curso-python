### CONDICIONALES  ###

#los condicionales como dice el mismo titulo son un tipo de validacion o funcion que nos permite hacer algo bajo ciertas condiciones
#nos permite hacer una validacion de datos (en caso de un login)

#veremos ejemplos sencillos
#cambiar los valores para ver resultados

condicion = True #false

if condicion: #no necesitamos poner == true el programa asume que para pasar a la linea que esta abajo nuestra condiion debe ser verdadera (en caso que estemos trabajando con valores booleanos)
    print("se ejecuta la condicion del if")

print("seguimos programando")

#veamos el caso en de un login
#interactuamos con la terminal
user=[]
user_comprovacion=[]
print("ingresa tu nombre:")
nombre=input()
user.insert(0,nombre)  
print("ingresa una contraseña")
contraseña=input()
user.insert(1,contraseña)
cadena_saltos=print("*");print("*");print("*");print("*");print("*");print("*");print("*");print("*");print("*");print("*");print("*");print("*");print("*********************************************************************************")
cadena_saltos
print("entrando al login")
print("ingrese su nombre")
nombre_comprovacion = input()
user_comprovacion.insert(0,nombre_comprovacion)
print("ingresa una contraseña")
contraseña_comprovacion=input()
user_comprovacion.insert(1,contraseña_comprovacion)

if user[0] == user_comprovacion[0] and user[1] == user_comprovacion[1]:
    print("ingreso exitoso")
elif user[0] == user_comprovacion[0] and user[1] != user_comprovacion[1]:
    print("clave invalida")
elif user[0] != user_comprovacion[0] and user[1] == user_comprovacion[1]:
    print("usuario no valido")

print("seguimos programando...")
