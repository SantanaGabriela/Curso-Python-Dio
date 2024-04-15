class Estudante:
    escola = "DIO"

    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula 
    
    def __str__(self) -> str:
        return f"{self.nome} -  {self.matricula} - {self.escola}"
    
def Mostrar_valores(*objs):
    for obj in objs:
        print(obj)
aluno_1 = Estudante("Guilherme",1)
aluno_2 = Estudante("Gio", 2)
Mostrar_valores(aluno_1, aluno_2)

