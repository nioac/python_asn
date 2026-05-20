
# %%

palavra = input("Digite uma palavra: ")

contador = 0

for letra in palavra:
    if letra.lower() == "a":
        contador = contador + 1

print("A letra 'a' aparece", contador, "vezes.")


# %%

soma = 0

for i in range(4):

    altura = (input("Digite uma altura {i}: "))
    soma += float(altura)

print("A soma das alturas é:", soma)

# %%

soma = 0

while True:
    saldo = input("Digite o saldo em conta ou aperte Enter para parar: ")

    if saldo == "":
        break

    # saldo = float(saldo)
    soma += float(saldo)

print("A soma dos saldos é:", soma)


# %%

soma = 0
extrato = []
contador = 1

while True:
    saldo = input("Digite o saldo em conta ou aperte Enter para parar: ")

    if saldo == "":
        break

    saldo = float(saldo)

    extrato.append(saldo)
    soma = soma + saldo

print("\nEXTRATO:")

for valor in extrato:
    print("Lançamento", contador, "- R$", valor)
    contador = contador + 1

print("\nTotal: R$", soma)

# %%

soma = 0
extrato = []

while True:
    saldo = input("Digite o saldo em conta ou aperte Enter para parar: ")

    if saldo == "":
        break

    saldo = float(saldo)

    extrato.append(saldo)
    soma = soma + saldo

print("\nEXTRATO DOS VALORES DIGITADOS:")

for valor in extrato:
    print("R$", valor)

print("\nSoma total dos saldos: R$", soma)