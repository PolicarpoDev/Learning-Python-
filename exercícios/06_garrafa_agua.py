# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$ 1,50
# Se o cliente escolher água mineral com gás, será cobrado R$ 2,50

texto = """ 
Escolha o tipo de água que deseja comprar:
(1) Água mineral natural
(2) Água mineral com gás
"""

opcao = input(texto) 

conta = 0
if opcao =="1":
    conta = 1.50
elif opcao =="2":
    conta = 2.50

if conta == 0:
    print("Opção inválida. Por favor, escolha 1 ou 2.")
else:
    print(f"Sua conta deu : R$ {conta:.2f}")
