class animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = int((idade))
    def fazer_som (self):
        print(' %s faz um som' % self.nome)
    def info(self):
        print(" seu animal se chama %s, e tem %i anos" %(self.nome, self.idade))
class cachorro(animal):
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def fazer_som(self):
        print (" %s late" % self.nome)
    def info(self):
        print(" seu cachorro se chama %s, e tem %i anos" %(self.nome, self.idade))

meuanimal = animal("caliborn", 18)
meuanimal.info()
meuanimal.fazer_som()


