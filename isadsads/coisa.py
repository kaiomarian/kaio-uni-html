class carro:
    def __init__ (self, modelo, ano, velocidade):
        self.mod = modelo
        self.an = ano
        self.vel = velocidade

    def acelerar(self):
        self.vel = self.vel + int(input('o quanto você quer acelerar '))

        return self.vel
    def info(self):
        print ("o seu",self.mod,"é de",self.an,"e está se movendo á",self.vel,"Km/h")

    
    
    
carr3o = carro("toyota", 2007, 23)
carr3o.acelerar()
carr3o.info()
        
        