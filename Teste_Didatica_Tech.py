class DidaticaTech:
    def __init__(self, v=10, i=1):
        self.valor = v
        self.incremento = i
        self.valor_exponencial = v

    def incrementa(self):
        self.valor += self.incremento
        print(self.valor)

    def verifica(self):
        if self.valor > 12:
            print("É Maior")
        else:
            print("É menor")

    def exponencial(self, e):
        self.valor_exponencial = self.valor**e


class Calculos(DidaticaTech):

    def __init__(self, d=5, v=10, i=1):
        super().__init__(v, i)
        self.divisor = d

    def decrementa(self):
        self.valor -= self.incremento

    def divide(self):
        self.valor = self.valor/self.divisor





x = Calculos(d=10)
x.verifica()


