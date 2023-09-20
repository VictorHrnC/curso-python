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
