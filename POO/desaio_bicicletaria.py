class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
       self.cor = cor
       self.modelo = modelo
       self.ano = ano
       self.valor = valor

    def buzinar(self):
        print("Plim plimmm")

    def parar(self):
        print("parando a bicicleta")
        print("Bicicleta parada")

    def correr(self):
        print("Vruumm")

    

b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)   
b1.buzinar()
b1.parar()
b1.correr()




