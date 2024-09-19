# programa_principal.py

# Importa a função media_aritmetica do módulo calculo_media
from calculo_media import media_aritmetica

# Leitura dos valores do usuário
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))

# Calcula a média usando a função importada
media = media_aritmetica(a, b)

# Exibe o resultado
print("A média aritmética entre" ,a, "e" ,b, "é" ,media)
