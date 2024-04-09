consumo = float(input("Infome o consumo médio mensal de dados: "))

def recomendar_plano(consumo):
    if consumo <= 10:
        print("Plano Essencial Fibra - 50Mbps")
    elif (consumo > 10 and consumo <=20):
        print("Plano Prata Fibra - 100Mbps")
    else:
        print("Plano Premium Fibra - 300Mbps")
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
recomendar_plano(consumo)
