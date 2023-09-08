'''STRINGS'''
#los strings son cadenas de caracteres esto incluye letras numeros y caracteres !"#$%&/()==*"
#en pyton los podemos definir por comillas simples y dobles 
#definimos strings con variables asi es mas facil de llamarlas dentro de nuestro programa
er_str = "este es mi string"
do__str = "este es mi segundo string"
print(er_str)

#podemos utilizar operadores como vimos en operadores.py line 10
print(er_str + " " + do__str)

#existen strings con caracteres especiales que provocan ciertas funciones
#definamos un salto de linea entre el string
str_con_salto = "este es un string\ncon salto de linea"
print(str_con_salto)

#definamos un tab en nuestro string
str_con_tab = "\teste es un string con tabulacion" 
print(str_con_tab)

#al poner \\ en nuestos caracteres especiales vistos antes los anulamos
str_escapados = "\\t este string no tiene tabulacion \\n ni salto de linea"
print(str_escapados)

#formateo de un string con %. y {}
name, surname, age = "victor", "hernandez", 25
#con {}
print("mi nombre es {} {} y mi edad es {}".format(name,surname,age))
#con %
print("mi nombre es %s %s y mi edad es %d"%(name, surname, age))
#con{y nombres dentro}
print(f"mi nombre es {name} {surname} y mi edad es {age}")
#desempaquetando caracteres
#nos puede servir en caso de que queramos ver solo un caracter de un string definido
saludo = "hola"
a,b,c,d = saludo
print(a)
print(b)
print(c)
print(d)
#reversa a un string
reversaludo = saludo[::-1]
print(reversaludo)
#funciones
print(saludo.capitalize())
print(saludo.upper())
print(saludo.count("a"))
print(saludo.isnumeric())
print(saludo.lower())
print(saludo.upper().isupper())


