#tranalhanfo com listas
#item = ["palmito", "cenoura", "beterraba", "trigo", "sal"]
#-------------------------------------------
#vai até um item antes do limite
#print(item[1:3])
#print(item[1:-1])
#-------------------------------------------
#insere no final da lista
#item.append("batata")
#-------------------------------------------
#insere em uma posição específica, desde que não ultrapasse o limite
#item.insert(10, "morango")
#print(item)
#print("Onde está o morango? ", item.index("morango"))
#print("Onde está o sal? ", item.index("sal"))
#-------------------------------------------
#"pop" remove um item da lista se nao informado o indice, remove o ultimo
#pode remover por indice ou por valor. aceita indice negativo
#item.append("1212")
#print(item)
#item.pop()
#print(item)
#-------------------------------------------
#ordenar a lista
#item.sort()
#print(item)
#-------------------------------------------
""" 
lista = list()
lista.append("alho")
#imprime a quantidade de itens na lista
print("A lista possui %d elemento(s)" % (len(lista))) 
"""
#trabalhando com tuplas
tupletmp = ("alho", "cebola", "tomate", "batata", "cenoura")
#tupletmp = tuple(item)
print(tupletmp)
print(tupletmp[1])