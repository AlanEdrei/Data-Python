lista = [1,2,3,4,5,6,7,8,9]

def busqueda_I (lista,x):
    bajo = 0
    alto = len(lista)-1
    centro = (alto + bajo)//2
    while bajo <= alto:
        if lista[centro] == x:
            return centro
        elif lista[centro] < x:
            bajo = centro+1
        else:
            alto = centro -1
        centro = (alto + bajo)//2
    return "No encontrado"
