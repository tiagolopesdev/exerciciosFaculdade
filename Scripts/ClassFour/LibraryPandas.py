import pandas as pd

pd.Series(data=5)

listNames = 'Tiago João Lucas Bia Ana'.split()

# Cria uma serie com um dicionário
dados = {
    'nome1': 'Howard',
    'nome2': 'Ian',
    'nome3': 'Peter',
    'nome4': 'Jonah',
    'nome5': 'Kellie',
}
pd.Series(dados) 

cpfs = '''111.111.111-11 
    222.222.222-22 333.333.333-33 
    444.444.444-44 555.555.555-55
    '''.split()

print("\n")

seriesDados = pd.Series(listNames, index=cpfs)
print(f"Pessoa localizada: {seriesDados.loc['111.111.111-11']}")


