# %%

def eh_par(numero: int):
    return numero % 2 == 0

for i in range(1, 100):
    if eh_par(i):
        print(f"{i} é par")
        continue
       
        print(f"{i} é impar")


# %%

import random


def recebe_numero():
    while True:
        try:
            numero_chute = int(input("Entre com seu numero da sorte (1 a 15): "))
            if 1 <= numero_chute <= 15:
                return numero_chute

        except ValueError as err:
            pass

        print("Entre com um número válido!")


numero_alvo = random.randint(1,15)
tentativas = 3

for i in range(0,tentativas):

    print(f"Você tem {tentativas-i} tentativas...")

    numero_chute = recebe_numero()

    if numero_chute == numero_alvo:
        print("Parabéns! Você é foda!")
        break

    elif numero_chute >  numero_alvo:
        print("Seu bosta! Errou! Chute algo menor!")

    else:
        print("Seu bosta! Errou! Chute algo maior!")

else:
    print("Suas tentativas acabaram! Nos vemos depois...")
    print(f"O numero era {numero_alvo}")


# novas alterações de teste

