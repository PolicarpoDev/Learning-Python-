idades = [28, 42, 43, 35, 39, 28, 38, 42, 34]

print(idades)

#teo = ["Téo", "Calvo", 32, True, "Casado", 2342.98]

#print(teo)

#type (teo)

#print(teo[2])

#print(teo[5])

#print(teo[0])

print("soma idades: ", sum(idades))

print("qtde idades ", len(idades))

print("media idades: ", sum(idades)/ len(idades))

print("menor idade: ", min(idades))

print("maior idade: ", max(idades))

teo = ["Téo Calvo", 
       32, 
       True, 
       "Casado", 
       ["estagiário", "ds junior", "ds pl", "ds sr", "head"], 
       [1500, 4000, 4550, 6500, 10000],
       ["Ana", "Maria", "Claudia"]] 

print("Tamanho do téo:", len(teo))

print(teo[4][0])

exs = teo[4]
primeira_ex = exs[0]
print(primeira_ex)

tamanho = len(teo)
pos = tamanho - 1
teo[pos]

teo[pos][len(exs) - 1]

teo[-1][-1]

teo[0:4]

teo[4][3:5]

teo[4][-2:]

#primeiros 4 elementos
teo[:4]

#teo [ start : stop]

salarios = teo[5]
salarios [::-1]

#teo [ start : stop : step]