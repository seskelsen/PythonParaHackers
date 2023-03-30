#trabalhando com arquivos

with open("code/arquivo.txt", "a") as arquivo:
    arquivo.write("TEXTO\n")

arquivo.close()


with open("code/arquivo.txt", "r") as arquivo:
    print(arquivo.read())

arquivo.close()

with open("code/arquivo.txt", "a") as arquivo:
    arquivo.writelines("TEXTO = 0010101101\n")

with open("code/arquivo.txt", "r") as arquivo:
    print(arquivo.read())

arquivo.close()