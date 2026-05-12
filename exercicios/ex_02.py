
# %%
nome = input("Ola, qual é o seu nome? ")

nome = nome.title().strip(" ")

print(f"""
Olá, {nome}! Seja bem-vindo(a) à nossa história interativa.""")
print(f"Que bom estar aqui, {nome}! Vamos começar a nossa aventura juntos!", sep="\n\n")
print(f"Oi, {nome}! Estou animado para compartilhar esta história com você.", sep=" ")


# %%

numero = input("Digite um número para escolher o caminho da história: ")

numero = float(numero)

raiz = numero ** (1/2)

msg = f"a raiz de {numero} é {raiz}"
print(msg)

# %%

numero = input("Digite um número para escolher o caminho da história: ")
numero = float(numero)

dobro = numero * 2

msg = f"O dobro de {numero} é {dobro}"
print(msg)