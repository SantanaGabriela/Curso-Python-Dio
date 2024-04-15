class Animal:
    def __init__(self, nro_patas) :
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {','.join ([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        

class Mamifero(Animal):
     def __init__(self, cor_pelo, **kw) :
        
        #chamando o construtor da classe pai - usa-se super().__init__(atributos)
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
     def __init__(self, cor_bico,**kw) :
       
        #chamando o construtor da classe pai - usa-se super().__init__(atributos)
        super().__init__(**kw)
        


class Gato(Mamifero):
    pass

class Ornitorrinco (Mamifero, Ave):
    pass


gato = Gato(nro_patas= 4, cor_pelo="preta")
print(gato)

ornitorrinco = Ornitorrinco (nro_patas= 2, cor_pelo="Vermeleho", cor_bico="Laranja")
print(ornitorrinco)