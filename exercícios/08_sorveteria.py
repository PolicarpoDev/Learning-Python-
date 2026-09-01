print("=== SORVETERIA ===")

print("\nEscolha o tipo de sorvete:")
print("1 - Casquinha - R$ 1,00")
print("2 - Cascão - R$ 2,50")
print("3 - Cestinha - R$ 4,00")

tipo = int(input("Digite a opção: "))

if tipo == 1:
    valor_sorvete = 1.00
elif tipo == 2:
    valor_sorvete = 2.50
elif tipo == 3:
    valor_sorvete = 4.00
else:
    valor_sorvete = 0
    print("Opção inválida!")

print("\nEscolha o sabor:")
print("1 - Morango")
print("2 - Creme")
print("3 - Chocolate")

sabor = int(input("Digite a opção: "))

if sabor == 1:
    nome_sabor = "Morango"
elif sabor == 2:
    nome_sabor = "Creme"
elif sabor == 3:
    nome_sabor = "Chocolate"
else:
    nome_sabor = "Inválido"
    print("Sabor inválido!")

print("\nEscolha a cobertura:")
print("1 - Caramelo - R$ 1,50")
print("2 - Morango - R$ 1,50")
print("3 - Chocolate - R$ 1,50")
print("4 - Sem cobertura - R$ 0,00")

cobertura = int(input("Digite a opção: "))

if cobertura == 1:
    valor_cobertura = 1.50
elif cobertura == 2:
    valor_cobertura = 1.50
elif cobertura == 3:
    valor_cobertura = 1.50
elif cobertura == 4:
    valor_cobertura = 0.00
else:
    valor_cobertura = 0
    print("Cobertura inválida!")

total = valor_sorvete + valor_cobertura

print("\n=== PEDIDO ===")
print("Sabor:", nome_sabor)
print(f"Valor a ser pago: R$ {total:.2f}")