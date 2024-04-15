class Passaro:
    def voar(self):
        print("voando..")

class Pardal(Passaro):
    def voar(self):
     super().voar()

class Avestruz(Passaro):
   def voar(self):
      print("Avestrux não pode voar")

#um método da classe Passaro
def  plano_voo(obj):
   obj.voar


p1 =  Pardal
p2 = Avestruz

plano_voo(p1)
plano_voo(p2)

