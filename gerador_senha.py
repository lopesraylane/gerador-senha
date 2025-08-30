import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

print("Bem-vinda ao Gerador de Senhas!")
tamanho = input("Digite o tamanho da senha desejada (ex: 12): ")

if tamanho.isdigit():
    senha_gerada = gerar_senha(int(tamanho))
    print(f"Sua senha segura é: {senha_gerada}")
else:
    print("Por favor, digite um número válido.")
