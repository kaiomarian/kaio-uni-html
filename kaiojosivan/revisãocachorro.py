class animal:
    def __init__(self, n, i):
        self.nome = n
        self.idade = i

    def fazer_som(self):
        print(self.nome, "faz um som.")

    def imprimir_imformacoes(self):
        print(self.nome, "é um animal de", self.idade, "anos de idade")
class cachorro(animal):
    def __init__(self, n, i):
        self.nome = n
        self.idade = i

    def fazer_som(self):
        print(self.nome, "late")



meuanimal = animal("caliborn", 67)
meucachorro = cachorro("calliope", 41)

meuanimal.fazer_som()
meuanimal.imprimir_imformacoes()

print()

meucachorro.fazer_som()
meucachorro.imprimir_imformacoes()