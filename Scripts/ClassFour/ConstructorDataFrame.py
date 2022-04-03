import pandas as pd

listNames = 'Tiago João Lucas Bia Ana'.split()

listCpfs = '''111.111.111-11 
    222.222.222-22 333.333.333-33 
    444.444.444-44 555.555.555-55
    '''.split()

listEmail = '''one@gmail.com two@gmail.com 
    three@gmail.com four@gmail.com 
    five@gmail.com'''.split()

listIdade = [32, 22, 25, 29, 38]

print(pd.DataFrame(listNames, columns=['nomes'], index=listCpfs))

# Usando a função Zip() para Criar tuplas compostas por valores contidos nas listas

dados = list(zip(listNames, listEmail, listCpfs, listIdade))
print(pd.DataFrame(dados, columns=['Nomes', 'E-mails', 'CPF', 'Idade']))

# Construtor DataFrame com dicionário de dados

dadosDicionario = {
    'nomes' : 'Tiago João Lucas Bia Ana'.split(),
    'emails' : '''one@gmail.com two@gmail.com 
        three@gmail.com four@gmail.com 
        five@gmail.com'''.split(),
    'CPF' : '''111.111.111-11 
        222.222.222-22 333.333.333-33 
        444.444.444-44 555.555.555-55
        '''.split(),
    'idades' : [32, 22, 25, 29, 38]

}
print("\nDados com dicionário\n")
print(pd.DataFrame(dadosDicionario))

# Seleção de colunas em um DataFrame

print("\nSeleção de colunas com dados em dicionário\n")
dfDadosDicionario = dadosDicionario['idades']
print("Tipo de dado: ", type(dfDadosDicionario))