# %% 

arquivo = "data.csv"

with open(arquivo) as open_file:
    data = open_file.readlines()

for linha in data:
    print(data)

# %%

dados = dict()

chaves = data[0].strip("\n").split(";")
for c in chaves:
    dados[c] = []

dados
# %%

nome = "Souza araujo"
nome.split(" ")
