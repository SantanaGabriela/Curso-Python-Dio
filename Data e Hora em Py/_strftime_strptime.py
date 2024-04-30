from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2024-04-29 21:07"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

#formatando para PT-br / de datetime para str
print(data_hora_atual.strftime(mascara_ptbr))
#formatando para EN/ de str para datetime
print(datetime.strptime(data_hora_str, mascara_en))

