import random

chaves = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?!#@"

def senhas():
    while True:
        senha_len = int(input('Digite um numero: '))
        for i in range(0, 1):
            senha = ""
            for i in range(0, senha_len):
                senha1 = random.choice(chaves)
                senha += senha1
            print('Esta foi a senha gerada:', senha)
