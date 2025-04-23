import random
import time

separador = "---------------------------------------------------------------"

def monitorar():
  while True:
    qualidade = obter_qualidade()
    controlar_sensor(qualidade)
    time.sleep(10)

def controlar_sensor(qualidade):
  if qualidade > 50:
    print(f"Tome cuidado: Qualidade {qualidade:}(IQA) começou a ficar prejudicial.")
    print(separador)
  else:
    print(f"O ar está com qualidade excelente: Qualidade {qualidade:}(IQA) não está prejudicial")
    print(separador)

def obter_qualidade():
  qualidade = random.randint(0, 150)
  return qualidade

monitorar()