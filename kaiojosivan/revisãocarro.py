class carro:
    def __init__(self, ano, vel, mod):
        self.Ano = ano
        self.Velocidade = vel
        self.Modelo = mod
    def acelerar(self, velacel):
        self.Velocidade += velacel
    def infor(self):
        print("o carro é do modelo", self.Modelo)
        print("foi fabricado em", self.Ano )
        print("e está a", self.Velocidade, "km por hora")
        
meucarro = carro(2007, 20, "toyota")

meucarro.acelerar(20)
meucarro.infor()