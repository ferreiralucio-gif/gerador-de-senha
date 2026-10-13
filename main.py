import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

tamanho = int(input("Digite o comprimento da senha: "))

senha = ""

for _ in range(tamanho):
  senha += random.choice(caracteres)

print(f"Sua senha gerada é: {senha}")