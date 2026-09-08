# Faça um programa que receba 4 alturas usando um laço
# de repetição e realize a soma dessas alturas.

soma = 0
qtde_entradas = 4

for i in range(qtde_entradas):
    altura = float(input("Entre com a altura: "))
    soma += altura

print("Soma das altura: ", soma)
    