# %%


A = input("Entre com a 1º Nota: ")
B = input("Entre com a 2º Nota: ")
C = input("Entre com a 3º Nota: ")
D = input("Entre com a 4º Nota: ")

notas = [float(A), float(B), float(C), float(D)]

media = sum(notas) / len(notas)
minimo = min(notas)
maximo = max(notas)

metricas = [media, minimo, maximo]

print(notas)
print(metricas)

# %%


notas = [float(input(f"Entre com a {i+1}º Nota: ")) for i in range(4)]

media = sum(notas) / len(notas)
minimo = min(notas)
maximo = max(notas)

metricas = [media, minimo, maximo]

print(notas)
print(metricas)



# %%

A = input("Entre com a temperatura do 1º dia: ")
B = input("Entre com a temperatura do 2º dia: ")
C = input("Entre com a temperatura do 3º dia: ")
D = input("Entre com a temperatura do 4º dia: ")

temperaturas = [A, B, C, D]

