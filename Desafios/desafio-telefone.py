import re


 # TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
   
    padrao = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    
    # Verifica se o número de telefone corresponde ao padrão
    if re.match(padrao, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  


result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)