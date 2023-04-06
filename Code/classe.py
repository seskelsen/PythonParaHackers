class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def printarnomecompleto(self):
        return self.nome + " " + self.sobrenome

info_pessoa = Pessoa("Sigmar", "Eskelsen")

print(info_pessoa.printarnomecompleto())
print(info_pessoa.nome)
