import random
listas_carro=["ford","bmw","mercedes","renault","ferrari"]
""""
lista_marca=[]
for marca in lista_marca:
    if marca[0]=="f":
        lista_marca.append(marca)
"""
lista_marca=[marca for marca in listas_carro if marca[0]=="f"]
print(lista_marca)
lista_numeros=[random.randint(1,100) for i in range(10)]
print(lista_numeros)