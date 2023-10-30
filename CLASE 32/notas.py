Class Persona:
    def __init__(self, nombre, apellido, edad=0): #La edad indica que es opcional
        self.__nombre = nombre #__ --> Indica atributo privado
        self.__apellido = apellido
        self.__edad = edad
        #self._metodo = metodo  _ --> Indica atributo protegido
    

# Atributos protegidos accesibles solo de la misma clase o subclase
class Alumno:
    def __init__ (self, nombre):
        self._nombre = nombre


@property #Decorador. Equivalente de un getter
def nombre(self):
    return self._nombre
@nombre.setter
def nombre(self, nuevoNombre):
    self._nombre = nuevoNombre

yo = Alumno("Dahyana Romero")
yo.nombre
nombre

yo = Alumno ("Dahyana A ROMERO")
yo.nombre

# Atributos privados
class Estudiante:
    __nombreEscuela = "XZY Colegio" #Metodo de clase: definido en la clase

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def __mostrar(self): #Metodo privado
        print("Este metodo es privado")

est = Estudiante("Juan", 20)
#no va a acceder a ninguno porque son privados
est.__nombreEscuela
est.__nombre
est.__mostrar()

est._Estudiante__nombre = "Pedro" #Forma de acceder a at privados, modificar consultar
est._Estudiante__mostrar()
