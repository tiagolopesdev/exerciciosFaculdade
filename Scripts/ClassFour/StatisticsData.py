import pandas as pd

seriesDados = pd.Series([10.2, -1, None, 15, 23.4])

print('Quantidade de linhas = ', seriesDados.shape)
print('Qual o menor valor?', seriesDados.min()) 
print('Qual o maior valor?', seriesDados.max()) 
print('Tipo de dados', seriesDados.dtypes)
print('Qual a média aritmética?', seriesDados.mean())
print('Os valores são únicos?', seriesDados.is_unique)
print('Qual o desvio padrão?', seriesDados.std())
print('Existem valores nulos?', seriesDados.hasnans)
print('Qual a mediana?', seriesDados.median())
print('Quantos valores existem?', seriesDados.count())