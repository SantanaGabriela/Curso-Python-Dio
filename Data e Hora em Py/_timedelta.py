from datetime import timedelta, datetime, date, time

tipo_carro= 'M' #P,M,G

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'p':
    data_estimada= data_atual + timedelta(minutes=tempo_pequeno) 
    print(f'O carro chegou {data_atual} e ficará pronto as {data_estimada}')
elif tipo_carro == "M":
     data_estimada= data_atual + timedelta(minutes=tempo_medio) 
     print(f'O carro chegou {data_atual} e ficará pronto as {data_estimada}')
else:
     data_estimada= data_atual + timedelta(minutes=tempo_grande) 
     print(f'O carro chegou {data_atual} e ficará pronto as {data_estimada}')



print(date.today() - timedelta(days = 1))
# para quando quiser manuplar horas, precisa usar o datatime e depois solicitar a saída do time
resultado = datetime(2024,4,29,10,19,20) - timedelta(hours=1)
print(resultado.time())
print(resultado.date())
