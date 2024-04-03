"""
Abstraction
"""

from abc import ABC,abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractclassmethod
    def realizar_actividad(self):
        pass
    
    def presentarse(self):
        print(f"hola, me llamo {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def realizar_actividad(self):
        print(f"estoy estudiando {self.actividad}")

P1= Estudiante("Alan",28,"Masculino","Programación")


P1.realizar_actividad()
P1.presentarse()

"""
Decoradores
"""

def decorador(funcion):
    def modificacion():
        print("aqui agrego algo antes de ejecutar la función")
        funcion()
        print("aquí agrego algo depués de ejecutar la función")
    return modificacion
    

def ejemplo():
    print("Función base se ejecuta")


"""
Duner_Methods
"""

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"hola, gracias al método __str__ no te doy la dirección de memoria, sino que te digo que me llamo {self.nombre} y tengo {self.edad} años"

    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre,nuevo_valor)

P1= Persona("Alan",28)

AlanFuturo = (P1+P1)
print(AlanFuturo.edad)

"""
Herencia Múltiple
"""

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def saludar(self):
        print(f"Hola! soy {self.nombre}, tengo {self.edad} años y soy {self.nacionalidad}")

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        print(f"mi habilidad es {self.habilidad}")
    

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,puesto, salario):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.puesto = puesto
        self.salario = salario
    def presentarse(self):
        print (f"hola, mi nombre es {self.nombre} y") , f"{super().mostrar_habilidad()}"
        
    
P1 = Persona("Simón",32,"Mexicano")
P2 = Persona("Leónidas",1320,"Espartano")
P3 = EmpleadoArtista("Bartolomé",89,"Estadounidense","bailar","Doctor",89233)



P3.mostrar_habilidad()
P3.presentarse()
P1.saludar()
P2.saludar()

herencia = issubclass(EmpleadoArtista,Persona)
print(herencia)

isinstancia = isinstance(P3,Persona)
print(isinstancia)

