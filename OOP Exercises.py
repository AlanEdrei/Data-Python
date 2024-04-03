class Estudiante:
    def __init__(self, nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"el estudiante {self.nombre} está estudiando")


estudiante1 = Estudiante(input("nombre "),input("edad "),input("grado "))

estudiante1.estudiar()

"""
2
"""

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def consulta(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self,nombre, edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
    def año(self):
        print(f"Estoy en {self.grado} grado")

E1 = Estudiante("Pepito",23,"Quinto")
E1.consulta()
E1.año()

"""
Fusion
"""

class Personaje():
    def __init__(self,nombre,poder):
        self.nombre=nombre
        self.poder = poder
    
    def __add__(self,otro):
        nuevo_nivel = ((self.poder + otro.poder)/2)**2
        return Personaje(self.nombre + otro.nombre,nuevo_nivel)

Goku = Personaje("Goku",9000)
Vegueta = Personaje("Vegueta",8000)

Gogeta = Goku + Vegueta

print(Gogeta.poder)

"""
encapsulation
"""

class Persona:
     def __init__(self,nombre,edad):
         self.__nombre = nombre
         self.edad = edad
    
     def get_nombre(self):
         return self.__nombre

     def set_nombre(self,nombreNuevo):
         self.__nombre = nombreNuevo

P1 = Persona("Alan","18")

print(P1.get_nombre())
P1.set_nombre("Edrei")
print(P1.get_nombre())

#con DECORADOR = @property:

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.edad = edad

    #Las siguientes propiedades nos van a permiir acceder y modificar nombre como si no fueran privado
           
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo):
        self.__nombre=nuevo
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre


P1 = Persona("Juancho","18")
print(P1.nombre)

P1.nombre = "Pedrito Sola"
print(P1.nombre)
print(P1.__dict__)

del P1.nombre
print(P1.__dict__)


