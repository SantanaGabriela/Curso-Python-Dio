saldo = 2000
saque = 2100

status = "SUCESSO" if saldo >= saque else "FALHA"

print(f"{status} ao realizar o saque! ")

