from random import randint

class Tragamonedas:
    def __init__(self,id,premio):
        self.id = id
        self.premio = premio
        self.monedas = 0
        self.jackpots = 0
    
    def jugar(self):
        monedas += 1
        numeros = [randint(0, 9),randint(0, 9),randint(0, 9)]
        mensaje = ""
        if numeros[0] == numeros[1]and numeros[1] == numeros[2]:
            self.jackpots += 1
            mensaje = "Felicidades!! Ganaste: " , self.premio
        else:
            mensaje = "Mejor suerte la próxima"
        return numeros, mensaje
        
tragaA = Tragamonedas(1, 100000)
tragaB = Tragamonedas(2, 500)

for i in range(100):
    print(tragaA.jugar())
    print(tragaB.jugar())

"""
Encapsulamiento
"""

class Cuenta:
    def __init__(self,nombre,direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.__balance = 0.00
        
    def retirar(self,monto):
        if monto > 0:
            if monto <= self.__balance:
                self.__balance -= monto
            
            else:
                print("No hay saldo suficiente")
        else:
            print("Muy listo... Pero no.")
    
    def depositar(self,monto):
        self.__balance += monto

"""
Atributos clase y objeto
"""

class Vehiculo:    
    folio = 0    
    COLORES = ("BLANCO","ROJO","VERDE")
    
    def __init__(self,serie,color):
        Vehiculo.folio +=1
        self.serie = Vehiculo.folio
        self.set_color(color)
    
    def __str__(self):
        return str(self.serie) + " " + self.color

    def set_color(self,color):
        color = color.upper().strip()
        if color in Vehiculo.COLORES:
            self.color = color
        else:
            self.color = Vehiculo.COLORES[0] #default
        

au1 = Vehiculo("","rojo")
au2 = Vehiculo("","azul")

print(au1)
print(au2)

"""
Herencia y Polimorfismo

"""

class Producto:
    
    def __init__(self,id, descripcion,costo):
        self.id = id
        self.descripcion = descripcion
        self.costo = costo
        
    
    def qr(self):
        return "%s \n %s \n %0.2f \n" % (self.id,
                                        self.descripcion,
                                        self.costo)
    

class Perecedero(Producto):
    def __init__(self,id,descripcion,costo,fechaCad):
        super().__init__(id,descripcion,costo)
        self.fechaCad = fechaCad
    
    def qr(self):
        return super().qr() +"%s \n" % (self.fechaCad)
    
    
class Electronico(Producto):
    def __init__(self,id,descripcion,costo,marca):
        super().__init__(id,descripcion,costo)
        self.marca = marca
        
    def qr(self):
        return super().qr() + "%s \n" % (self.marca)




p = Producto("pro","Prueba",100.10)
per = Perecedero("F","fsfd",322,"Marzo")
ele = Electronico("Fef","fsdfs",2291,"LG")
print(p.qr())
print(per.qr())
print(ele.qr())
