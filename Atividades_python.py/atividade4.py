import random

numero_gerado = random.randint(1, 100)

tentativas = 0

while True:
    palpite = int(input("Tente adivinhar o número entre 1 e 100: "))

    tentativas += 1

    if palpite < numero_gerado:
        print("O número é maior. Tente novamente.")
    elif palpite > numero_gerado:
        print("O número é menor. Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número {numero_gerado} em {tentativas} tentativas.")
        break