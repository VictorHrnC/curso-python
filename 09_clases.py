### CLASES ###

# las clases son aquellas entidades que son muy utilizadas en el ambito de OOP (programacion orientada a objetos) ya que es desde aqui donde a un objeto se le asignan caracteristicas
# cuando estuve en la universidad se hablo y se enfocaron demaciado en esto ya que en la mayoria de lenguajes que trabajan con OOP se trabajan de forma similar
# al venir de un lenguaje como java estoy un poco familiarizado con clases por ende se igual de herencias, encapsulamiento y demaces.

# para definir una clase debemos ocupar la palabra reservada por el lenguaje "class" acompañado de el nombre de nuestra clase
# definimos los valores con el def __init__ al hacer tab escribiendo "def ini" se nos completara y se nos rellenara el codigo  *maravillas de la tegnologia*
# si nos damos cuenta de como definimos una clase es similar a las funciones lo que debemos hacer es darle valores para definir a nuestra clase
"""COMO YO VEO LAS CLASES
        mi vision de las clases es simple es un constructor de todo lo que nos rodea, todo lo que esta anuesto al rededor fue creado de cierta forma, con funciones y con atributos
        hable arriba de que vi herencias lo que entre especies que existen en el mundo real ocurre 
        ej: un pato y un pingüino son de la clase ave (los define que su estructura osea) tienen: alas,plumas,pico,2patas
            un pato tiene una funcion que nuestro amigo pingüino no tiene la cual seria volar() pero este tiene una funcion que seria deslizar_por_hielo() 
"""
# al contrario de las funciones variables y demas estructuras las clases se definen en CamelCase (EsDecirTodoJuntoConUnaMayusculaCadaPalabraNuevaQueEscribamos) !evitar las clases con
# nombres tan largos para que al llamarlos no sea tan engorroso


from enum import Enum
import keyboard


class Persona():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


# almacenemos valores dentro de nuestra variable
# al hacerla de tipo persona lo que hacemos es darle los valores que le asignamos en nuestra clase
# con la funcion
mi_persona = Persona("victor", "hernandez", 25)
print(mi_persona.name)
print(mi_persona.surname)
print(mi_persona.age)

# otra forma de definir una persona con los valores dentro de nuestro constructor
# recordar que lo que almacenamos son variables


class OtraPersona():
    def __init__(self):
        self.name = "Camila"
        self.surname = "Matamala"
        self.age = 29


mi_otra_persona = OtraPersona()
print(f"{mi_otra_persona.name} {mi_otra_persona.surname} {mi_otra_persona.age} ")

# veamos una forma de encapsular nombres en una propiedad
# dentro de fullname guardamos los datos de nombre y apellido podemos acceder con otra funcion para ver los datos es como tenerlos en privado pero no es el caso


class Person():
    def __init__(self, name, surname, age):
        self.fullname = f"{name} {surname}"
        self.age = age

    def caminar(self):
        print(f"{self.fullname} va caminando ")


person = Person("solange", "hernandez", 35)
print(person.fullname, person.age)
person.caminar()

# creacion de una clase con un elemento vacio o asignado
# lo que hacemos es = el valor de uno de los elementos de nuestro avion puede ser de algun valor predeterminado o vacio
# de esta forma en caso de que creemos un avio de tipo avion esto no nos dara un error


class Avion():
    # probar eliminar el ="" de tamaño para ver como en el objeto avion_1 se cae el problema
    def __init__(self, tipo, motor, capacidad, tamaño=""):
        self.tipo = tipo
        self.motor = motor
        self.capacidad = capacidad
        self.tamaño = tamaño
        self.descripcion = f"{tipo} {motor} {capacidad} {tamaño}"


avion_1 = Avion("airbus319", "turbofan", 155,)

avion_2 = Avion("airbus321", "turbofan", 210, "45m")

print("se a creado un avion "+avion_1.descripcion)
print("se a creado un avion "+avion_2.descripcion)

""" hagamoslo dinamico
    haremos una clase OtherPerson() y veamos que podemos hacer con ella
    revisar lineas de codigo cuidadosamente hare comentarios para que vean como es que se esta trabajando para que no se pierdan
    debemos de instalar el teclado con el pip desde nuestra bash de git con el comando pip install keyboard en caso de no haber instalado el pip desde un comienzo debemos de 
    agregarlo con una modificacion a nuestro python (seria como reinstalar pero le damos a modificar)
    recordad agregar los packages de librerias ahi estan las librerias para importar el keyboard
"""

# definimos nuestra clase OtherPerson


class OtherPerson():
    def __init__(self, name="", surname="", age=""):
        self.fullname = f"{name} {surname}"
        self.name = name
        self.surname = name
        self.age = age
# le damos funciones que esta OtherPerson puede realizar

    def caminar(self):
        print(f"{self.fullname} esta caminando")

    def saltar(self):
        print(f"{self.fullname} esta saltando")

    def correr(self):
        print(f"{self.fullname} esta corriendo")

# haremos una clase con una funcion para elegir que queremos hacer con nuestra persona
# recordar que python no tiene la funcion de enum en el core por eso lo debemos de importar
# por el formato de python los imports se fueron al principio


class selec(Enum):
    caminar = 1
    saltar = 2
    corer = 3

# haremos una funcion para acceder a nuestra eleccion con un parametro que sera de clase selec (esta es una clase que viene creada dentro de el core de python)


def eleccion(eleccion: selec):
    match eleccion:
        case selec.caminar:
            OtherPerson.caminar()
        case selec.saltar:
            OtherPerson.saltar()
        case selec.corer:
            OtherPerson.correr()


# definimos una lista persona para almacenar los valores que seran entregados a nuestro objeto my_person
# creamos variables para insertar dentro de la lista, llamamos a la popiedad insert()
persona = []
print("ingrese un nombre")
nombre = input()
persona.insert(0, nombre)
print("ingrese un apellido")
apellido = input()
persona.insert(1, apellido)
print("ingrese la edad")
edad = input()
persona.insert(2, edad)
# en este lugar haremos que nuestra lista persona con los valores que me des desde la terminal pasen a nuestro objeto que es de tipo OtherPerson
my_person = OtherPerson(persona[0], persona[1], persona[2])
# haremos nuestros prints para interactuar en la terminal
print("preciona w para caminar")
print("preciona *espacio* para saltar")
print("preciona *tab* para correr")
print("preciona *esc* para salir")
# con un while de tipo true para que siempre se mantenga iniciada la interaccion
while (True):
    event = keyboard.read_event()
    if event.name == "esc":
        break
    elif event.event_type == keyboard.KEY_DOWN:
        if event.name == "w":
            my_person.caminar()
        elif event.name == "tab":
            my_person.correr()
        elif event.name == "space":
            my_person.saltar()
