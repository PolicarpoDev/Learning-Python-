print("=== SORVETERIA ===")

print("\n1 - Casquinha - R$ 1,00")
print("2 - Cascão - R$ 2,50")
print("3 - Cestinha - R$ 4,00")

tipo = int(input("Escolha o tipo de sorvete: "))

if tipo == 1:
    valor = 1.00
elif tipo == 2:
    valor = 2.50
elif tipo == 3:
    valor = 4.00
else:
    print("Opção inválida!")
    valor = 0


print("\n1 - Morango")
print("2 - Creme")
print("3 - Chocolate")

sabor = int(input("Escolha o sabor: "))

if sabor < 1 or sabor > 3:
    print("Sabor inválido!")


print("\n1 - Caramelo - R$ 1,50")
print("2 - Morango - R$ 1,50")
print("3 - Chocolate - R$ 1,50")
print("4 - Sem cobertura")

cobertura = int(input("Escolha a cobertura: "))

if cobertura >= 1 and cobertura <= 3:
    valor += 1.50
elif cobertura != 4:
    print("Cobertura inválida!")


print(f"\nValor a pagar: R$ {valor:.2f}")