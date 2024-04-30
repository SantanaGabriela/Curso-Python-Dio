from datetime import datetime, date, time
import pytz


data = datetime.now(pytz.timezone("Europe/Oslo"))
print(data)
data_2 = datetime.now(pytz.timezone("America/Sao_Paulo"))
print(data_2)