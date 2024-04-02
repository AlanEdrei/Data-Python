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
