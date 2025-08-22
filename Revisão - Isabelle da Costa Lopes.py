class joia:
    def __init__(self,quilates, preco, cor, nome, ip ):
        self.nome = nome
        self.quilates = quilates
        self.preco = preco
        self.cor = cor
        self.__ip = ip

    def __str__(self):
        return f"Nome: {self.nome}, Cor: {self.cor}, Quilates: {self.quilates}, Preço: R${self.preco}."

p = joia ("12", "9540,00", "Rosa", "Diamante", "6279019")
print(p)
