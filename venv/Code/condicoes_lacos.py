'''
#exemplo de laço for
for numero in range(0,50,10):
    print(numero)
'''
'''
lista = ["alho", "cebola", "tomate", "batata", "cenoura",1,2,3,4,5,6,7,8,9,10]
for numero in lista:
    print(numero)
'''
'''
texto = "Python para hackers"
for letra in texto:
    print(letra)
print(len(texto))
'''

#while
criterio_parada = 0
criterio_parada_dois = 0

while criterio_parada != 10:
    print(criterio_parada)
    if criterio_parada == 6:
        print("seis")
    if criterio_parada == 9:
        criterio_parada_dois += 1
    if criterio_parada_dois == 3:
        print("Fim do programa")
        break
    elif criterio_parada == 9:
        criterio_parada = 0
    else:
        criterio_parada += 1

