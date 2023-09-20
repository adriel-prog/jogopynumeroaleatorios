import random


def main():
    numero_secreto = random.randint(1, 100)

    tentativas = 10

    contador_tentativas = 0

    while contador_tentativas < tentativas:
        numero_adivinhado = int(input("Digite um numero entre 1 e 100: "))

        if numero_adivinhado == numero_secreto:
            print("Parabéns! Você acertou o numero secreto!")
            break
        else:
            if numero_adivinhado > numero_secreto:
                print("O numero secreto é menor.")
            else:
                print("O numero secreto é maior.")

        contador_tentativas += 1

    if contador_tentativas == tentativas:
        print("Você perdeu! O numero secreto era {}.".format(numero_secreto))


if __name__ == "__main__":
    main()
