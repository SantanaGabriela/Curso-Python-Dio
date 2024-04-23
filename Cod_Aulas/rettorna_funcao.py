def Calculadora(operacao):
    def soma(a,b):
        return a+b
    
    def sub(a,b):
        return a-b
    
    def mul(a,b):
        return a*b
    
    def dev(a,b):
        return a/b
    
    match operacao:

        case "+":
            return soma
        
        case "-":
             return sub
    
        case "*":
             return mul
    
        case "/":
            return dev



print(Calculadora("+")(2,2))
print(Calculadora("-")(3,4))
print(Calculadora("*")(4,5))
print(Calculadora("/")(6,7))

