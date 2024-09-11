import math

from falsa_posicao import FalsaPosicao
from newton_raphson import newtonRaphson
from bisseccao import Bisseccao


print("Escolha um método:")
print("1. Método Bissecção")
print("2. Método Falsa Posição")
print("3. Método de Newton")

escolha = int(input("Digite o número correspondente ao método desejado: "))
if escolha == 1 :
   
   Bisseccao.calcular(0,(math.pi/25))
elif escolha == 2:
    FalsaPosicao.calcular(0,(math.pi/25))
else:
    newtonRaphson.calcular(math.pi/25)



def consumo_total_litros_mes(tipo_imovel, quartos, andares=1, dias_mes=30):
  """
  Calcula o consumo total de água em um mês para um apartamento ou casa.

  Args:
      tipo_imovel (str): Tipo de imóvel ('apartamento' ou 'casa').
      quartos (int): Número de quartos no imóvel.
      andares (int): Número de andares (para apartamentos, por padrão é 1 para casas).
      dias_mes (int): Número de dias no mês (padrão = 30).

  Returns:
      float: Consumo total de água em m³ por mês.
  """
  if tipo_imovel == 'apartamento':
      consumo_por_pessoa = 150
      pessoas = (2 * quartos) + 2  
  elif tipo_imovel == 'casa':
      consumo_por_pessoa = 200  
      pessoas = 2 * quartos  
      raise ValueError("Tipo de imóvel inválido. Escolha 'apartamento' ou 'casa'.")

  consumo_diario = pessoas * consumo_por_pessoa

  consumo_diario_com_reserva = 1.2 * consumo_diario

  consumo_total_dia = consumo_diario_com_reserva * andares
  consumo_total_mes = consumo_total_dia * dias_mes

  consumo_total_m3_mes = consumo_total_mes / 1000

  return consumo_total_m3_mes

# Exemplo de uso:
tipo_imovel = input("Digite o tipo de imóvel ('apartamento' ou 'casa'): ").lower()
quartos = int(input("Digite o número de quartos: "))

if tipo_imovel == 'apartamento':
  andares = int(input("Digite o número de andares: "))
else:
  andares = 1  # Para casas, por padrão, será 1 andar

dias_mes = int(input("Digite o número de dias no mês: "))

# Calcular o consumo mensal
consumo_total_m3_mes = consumo_total_litros_mes(tipo_imovel, quartos, andares, dias_mes)

print(f"Consumo total de água em {tipo_imovel} por mês: {consumo_total_m3_mes:.2f} m³")