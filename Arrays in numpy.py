import numpy as np

altura_peso = np.array([[1.74,91.40],
                [1.80,88.70],
                [1.78,87.30],
                [1.68,62.70],
                [1.78,81.60]])

print("El mínimo es: " ,altura_peso.min())
print("El maximo es: " ,altura_peso.max())

print("El mínimo está en la posición: " ,altura_peso.argmin())
print("El máximo está en la posición: " ,altura_peso.argmax())

print("El promedio es: ",altura_peso.mean(),"\n")

print("Las dimenciones del arreglo son ", altura_peso.ndim,"\n")

#ahora volvemos a hacer las consultas, pero esta vez según la dimensión

print("La altura mínima es: " ,altura_peso.min(axis=0))
print("La altura máxima es: " ,altura_peso.max(axis=0))

print("La altura mínima está en la posición: " ,altura_peso.argmin(axis=0))
print("La altura máxima está en la posición: " ,altura_peso.argmax(axis=0))

print("El promedio de alturas es: ",altura_peso.mean(axis=0), "\n")


#ahora cambiamos los ejes

altura_peso = altura_peso.transpose()
print("El nuevo arreglo es: ","\n",altura_peso,"\n")

print("La altura mínima es: " ,altura_peso.min(axis=1))
print("La altura máxima es: " ,altura_peso.max(axis=1))

print("La altura mínima está en la posición: " ,altura_peso.argmin(axis=1))
print("La altura máxima está en la posición: " ,altura_peso.argmax(axis=1))

print("El promedio de alturas es: ",altura_peso.mean(axis=1), "\n")


"""
Unión y separación de arrays en numpy

"""


import numpy as np

altura = np.array([1.74,1.8,1.78,1.68,1.78])

peso = np.array([81.4,88.7,87.3,62.7,81.6])

print(np.stack((altura,peso),axis=0),"\n")
print(np.stack((altura,peso),axis=1),"\n")

# Claramente agrupar por el eje 1 es más conveniente, ahora probamos concatenar


print(np.concatenate((altura,peso)),"\n") #Simplemente concatena, no es útil aquí porque son datos distintos

#como no nos sirve, probemos a separarlo

union = np.stack((altura,peso),axis=0)
print(union,type(union),"\n")


separados = np.split(union,2)
print(separados,type(separados),"\n")

print("Ahora la separación se hará despues de unir en dimención 1")
union = np.stack((altura,peso),axis=1)
print(union,type(union),"\n")


separados = np.split(union,5)
print("como podemos ver, ahora tenemos 5 arrays distintos: ",separados,type(separados))







"""
Unión y separación de arrays en numpy 2

"""


import numpy as np

arreglo1=np.array([1,2,3,4,5])
arreglo2=np.array([11,12,13,14,15])

print("las dos listas sumadas son: ",np.add(arreglo1,arreglo2),"\n")

print("las dos listas restadas son: ",np.subtract(arreglo1,arreglo2),"\n")

print("las dos listas divididas son: ",np.divide(arreglo1,arreglo2),"\n")

print("las dos listas potenciadas son: ",np.multiply(arreglo1,arreglo2),"\n")

print("las dos listas potenciadas son: ",np.power(arreglo1,arreglo2),"\n")

print("cada elemento de la primera lista al cubo: ",np.power(arreglo1,3),"\n","\n","\n")

altura = np.array([1.74, 1.8, 1.78, 1.68, 1.78, 1.7, 1.74, 1.74, 1.73, 1.79, 
           1.78, 1.72, 1.65, 1.78, 1.7, 1.68, 1.79, 1.68, 1.82, 1.72,
           1.75, 1.66, 1.67, 1.79, 1.75, 1.65, 1.78, 1.73, 1.71, 1.81,
           1.73, 1.71, 1.68, 1.74, 1.75, 1.68, 1.74, 1.81, 1.73, 1.82,
           1.8, 1.67, 1.73, 1.7, 1.73, 1.7, 1.81, 1.81, 1.76, 1.82, 1.68,
           1.74, 1.65, 1.8, 1.78, 1.7, 1.68, 1.78, 1.79, 1.73, 1.64, 1.67,
           1.69, 1.74, 1.76, 1.66, 1.66, 1.73, 1.79, 1.81, 1.78, 1.63,
           1.76, 1.72, 1.71, 1.7, 1.62, 1.8, 1.75, 1.8, 1.78, 1.78, 1.76,
           1.65, 1.65, 1.68, 1.74, 1.75, 1.69, 1.75, 1.7, 1.83, 1.64, 1.7,
           1.69, 1.69, 1.64, 1.69, 1.77, 1.8, 1.78, 1.69, 1.7, 1.7, 1.7,
           1.63, 1.73, 1.84, 1.66, 1.78, 1.8, 1.79, 1.78, 1.74, 1.77,
           1.73, 1.77, 1.76, 1.75, 1.8, 1.75,  1.8, 1.79, 1.71, 1.73,
           1.59, 1.76, 1.75, 1.71, 1.76, 1.8, 1.68, 1.74, 1.77, 1.73,
           1.68, 1.63, 1.67])

peso = np.array([81.4, 88.7, 87.3, 62.7, 81.6, 80.9, 74.6, 84.7, 76.7, 88.3,
         84.6, 74, 57.7, 84.1, 79.7, 63.8, 88.4, 71.2, 87.1, 67, 80.7,
         74.7, 60.5, 85.9, 72.4, 59.7, 87.3, 85.7, 64.1, 91.9, 82.8, 75.7,
         60.2, 73.1, 74.7, 65.9, 80.9, 91.3, 76, 86.8, 80.7, 74.2, 83.1,
         77.8, 84.5, 58.8, 89.5, 87, 84, 89.9, 56.5, 80.2, 61.8, 86.3,
         82.6, 69.4, 65.8, 79.3, 88.1, 78.5, 69.1, 62.5, 74, 74.4, 87.6,
         59.6, 61.4, 83.2, 89.2, 89.2, 103.7, 67.9, 85.4, 69.5, 75.7, 
         83.9, 59.5, 87.9, 82.6, 88.1, 86.2, 88.9, 84.4, 58.4, 61.5, 69.2,
         84.2, 78, 81.1, 81.5, 74.7, 90.4, 59.2, 79.3, 65.1, 93, 60.5,
         76.4, 98.8, 89.1, 88.9, 61.1, 76.6, 86, 75.5, 66.9, 79.4, 87.9,
         72.3, 93.8, 89, 90.7, 86.7, 77.6, 85.1, 91.8, 103.2, 91.1, 67,
         86.9, 78.7, 87.1, 85.5, 69.8, 75, 53.9, 99, 93.7, 88, 79.4, 87.6,
         60.4, 82.7, 90.6, 79.8, 61.2, 62.5, 59.7])

def C_imc(pe,al):
    imc_C = np.divide(pe,(np.multiply(al,al)))
    print(imc_C,"\n")
    

C_imc(peso,altura)

#se pueden usar funciones universales, pero también podemos convertir operaciones normales en una universal:
    
def UC_imc(peso,altura):
    return peso/(altura*altura)

#y ahora la volvemos universal:
    
UniversalIMC= np.frompyfunc(UC_imc, 2, 1)
print("Esta es la versión transformada en universal:\n”,UniversalIMC(peso,altura))
