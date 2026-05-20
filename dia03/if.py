# %%

print(1 == 1)
print(1 == 2)
print(1 != 2)
print(1 == 1)       
print(1 != 1)
print(1 > 0)    
print(1 < 2)
print(1 >= 1)   
print(1 <= 1)
print(1 > 2)    
print(1 < 0)
print(1 >= 2)

1==1
1!=2
1==1  

# %%


idade = 15

if idade < 18:
    print("Thau, você é menor de idade.") 

elif idade == 18:
    print("Parabéns, você acaba de se tornar maior de idade!")  

elif idade > 18:
    print("Você é maior de idade.")
    print("Pode votar e dirigir.")

elif idade >=70:
    print("Você é maior de idade.")
    print("Pode votar e dirigir.")
    print("Mas não pode dirigir, pois tem mais de 70 anos.")    

else:
    print("Você é maior de idade.")
    print("Pode votar e dirigir.")

print("Obrigado por usar nosso sistema de verificação de idade.")


# %%

agua = (input("Você que água com ou sem gás? "))

if agua == "sem":
    print("Vai custar R$1,50")
    quantidade = int(input("Quantas garrafas de água você deseja comprar? "))
    print(f"O total a pagar é R${quantidade * 1.50}")

else:
    print("Vai custar R$2,50")
    quantidade = int(input("Quantas garrafas de água você deseja comprar? "))
    print(f"O total a pagar é R${quantidade * 2.50}")   


# %%

tipo = input("""
=== Bem-vindo à Sorveteria do Paulo! ===
Escolha o Tipo de sorvete:
1 - Casquinha  (R$1,00)
2 - Cascão     (R$2,50)
3 - Cestinha   (R$4,00)
"""
)

if tipo == "1":
    nome_tipo = "Casquinha"
    preco_tipo = 1.00
elif tipo == "2":
    nome_tipo = "Cascão"
    preco_tipo = 2.50
elif tipo == "3":
    nome_tipo = "Cestinha"
    preco_tipo = 4.00
else:
    print("Opção inválida. Encerrando.")
    exit()

sabor = input("""
Escolha o sabor (1/2/3):
1 - Morango
2 - Creme
3 - Chocolate
"""
)

if sabor == "1":
    nome_sabor = "Morango"
elif sabor == "2":
    nome_sabor = "Creme"
elif sabor == "3":
    nome_sabor = "Chocolate"
else:
    print("Opção inválida. Encerrando.")
    exit()

print("\nCobertura:")
print("  1 - Caramelo   (R$1,50)")
print("  2 - Morango    (R$1,50)")
print("  3 - Chocolate  (R$1,50)")
print("  4 - Sem cobertura (R$0,00)")
cobertura = input("Escolha a cobertura (1/2/3/4): ").strip()

if cobertura == "1":
    nome_cobertura = "Caramelo"
    preco_cobertura = 1.50
elif cobertura == "2":
    nome_cobertura = "Morango"
    preco_cobertura = 1.50
elif cobertura == "3":
    nome_cobertura = "Chocolate"
    preco_cobertura = 1.50
elif cobertura == "4":
    nome_cobertura = "Sem cobertura"
    preco_cobertura = 0.00
else:
    print("Opção inválida. Encerrando.")
    exit()

total = preco_tipo + preco_cobertura

print("\n=== Resumo do pedido ===")
print(f"  Tipo:      {nome_tipo}       (R${preco_tipo:.2f})")
print(f"  Sabor:     {nome_sabor}")
print(f"  Cobertura: {nome_cobertura}  (R${preco_cobertura:.2f})")
print(f"\n  Total a pagar: R${total:.2f}")
print("========================")





# %%




# %%





# %%





# %%