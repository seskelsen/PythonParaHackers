#funcoes em python
def printar():
    print("Essa frase foi printada por uma função - printar()")

def entrada():
    nome = "Arnaldo"
    return nome

def func_final(nome):
    print("*" + nome)

printar()

entrada()

func_final(entrada())