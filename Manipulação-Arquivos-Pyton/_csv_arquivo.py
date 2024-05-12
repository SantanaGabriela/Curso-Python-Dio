import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open (ROOT_PATH / "usuario.csv", "w", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])
        escritor.writerow(["01", "Gabriela"])
        escritor.writerow(["02", "Eduardo"])
except IOError as exc:
    print(f'Erro ao criar arquivo. {exc}')