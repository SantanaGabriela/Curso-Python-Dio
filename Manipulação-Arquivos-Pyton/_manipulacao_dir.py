import os
import shutil
from pathlib import Path

#comando usado para indicar a pasta que deseja criar o arquivo
ROOT_PATH = Path(__file__).parent


#os.mkdir(ROOT_PATH / "novo diretório")

arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

#renomeando arquivo
os.rename(ROOT_PATH/ 'novo.txt', ROOT_PATH/'alterado.txt')

#removendo arquivo
os.remove(ROOT_PATH/"alterado.txt")

#movendo arquivo

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")