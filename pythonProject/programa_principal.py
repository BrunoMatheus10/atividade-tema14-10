# programa_principal.py

# Importa a função area_triangulo do módulo calculo_area
from calculo_area import area_triangulo

# Leitura dos valores do usuário
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

# Calcula a área usando a função importada
area = area_triangulo(base, altura)

# Exibe o resultado
print(f"A área do triângulo com base {base} e altura {altura} é {area}")
