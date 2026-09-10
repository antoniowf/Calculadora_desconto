
class Regra:
    """Calcula o desconto de uma compra conforme o seu valor.

    Aplica 5% para compras inferiores a R$ 200,00, 10% para compras entre
    R$ 200,00 e R$ 299,99 e 15% para compras a partir de R$ 300,00.
    """

    desc_a = 5 #compra < 200
    desc_b = 10 # compra >= 200 and compra < 300
    desc_c = 15 # compra >= 300
    
    def __init__(self, compra= 0, desconto = 0):
        self.compra = compra
        self.desconto = desconto
            
    def calcular_desconto(self):
        if self.compra < 200:
            self.desconto = self.compra * (self.desc_a / 100)
            return self.desconto
        elif self.compra >= 200 and self.compra < 300:
            self.desconto = self.compra * (self.desc_b / 100)
            return self.desconto
        elif self.compra >= 300:
            self.desconto = self.compra * (self.desc_c / 100)
            return self.desconto
        else:
            return 0
        
    def valorDescontoAplicado(self):
        valor_final = (self.compra - self.desconto)
        return valor_final



print(f"Bem vindo a plataforma de compras CLI")
compra = float(input("Insira o valor da sua compra: R$"))
compra = Regra(compra)
desconto = compra.calcular_desconto()
desconto_aplicado = compra.valorDescontoAplicado()
print(f"Sua compra recebeu um desconto de R${desconto:.2f}\nTotal: R${desconto_aplicado:.2f}")

while True:
    continua = input("Gostaria de calcular outra compra? S/N ").lower()
    if continua == "s":
        compra = float(input("Insira o valor da sua compra: R$"))
        compra = Regra(compra)
        desconto = compra.calcular_desconto()
        desconto_aplicado = compra.valorDescontoAplicado()
        print(f"Sua compra recebeu um desconto de R${desconto:.2f}\nTotal: R${desconto_aplicado:.2f}")
    else:
        break