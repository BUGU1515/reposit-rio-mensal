import random

numero_gerado = random.randint(1, 100)

tentativas = 0

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número gerado entre 1 e 100.")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_gerado:
        print("O número é maior. Tente novamente!")
    elif palpite > numero_gerado:
        print("O número é menor. Tente novamente!")
    else:
        print(f"Parabéns! Você acertou o número {numero_gerado}!")
        print(f"Você precisou de {tentativas} tentativas.")
        break