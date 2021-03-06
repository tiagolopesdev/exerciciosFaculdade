# text = "Aprendendo Python na disciplina de linguagem de progrmação"

# print(f"Tamanho do texto: {len(text)}")
# print(f"Python no texto: {'Python' in text}")
# print(f"Quantidade de y no texto: {text.count('a')}")
# print(f"As 5 primeiras letra são: {text[0:10]}")

#-------------
# Uso do meétodo split()

# text = "Aprendendo, Python, na disciplina de linguagem de progrmação"

# print(f"texto: {text}")
# print(f"Tamanho do texto: {len(text)}\n")

# worlds = text.split(',')
# print(f"Palavras: {worlds}")
# print(f"Tamanho das palavras: {len(worlds)}")

#-------------
# Listas

# vogais = ['a', 'e', 'i', 'o', 'u']

# for vogal in vogais:
#     print(f"Posição: {vogais.index(vogal)}, valor: {vogal}")

# text = "Python Java Go Kotlin C C# PHP Lua Go".split()

# print(f"Antes da listcomp: {text}")
# text = [item.lower() for item in text] # upper(): elementos em caixa alta, lower(): elementos em caixa baixa
# print(f"Depois da listcomp: {text}")

#-------------
# Funções map() e filter()

# text = "Python Java Go Kotlin C C# PHP Lua Go".split()

# newList = map(lambda x: x.upper(), text)
# print(f"Nova lista: {newList}")

# newList = list(newList)
# print(f"Agora sim, nova lista: {newList}")

# numbers = list(range(0,21))

# numbersPar = list(filter(lambda x: x % 2 == 0, numbers))
# print(f"Números pares: {numbersPar}")

#-------------
# Utilizando NumPy

# import numpy as np

# matriz_1_1 = np.array([1,2,3])
# matriz_2_2 = np.array([[1,2],[3,4]])
# matriz_3_2 = np.array([[1,2],[3,4],[5,6]])
# matriz_2_3 = np.array([[1,2,3],[4,5,6]])
# print(type(matriz_1_1))
# print(f"\nMatriz_1_1: {matriz_1_1}")
# print(f"Matriz_2_2: {matriz_2_2}")
# print(f"\nMatriz_3_2: {matriz_3_2}")
# print(f"\nMatriz_2_3: {matriz_2_3}")


#-------------
# Algoritmos de busca

# names = "joão tiago ana carol juca bia eduardo geovana lucas".split()
# print(f"Contem o nome joão:{'joão' not in names}")
# print(f"Contem o nome carol:{'carol' not in names}")

# def searchLinear(lista, valor):
#     for elemento in lista:
#         if valor == elemento:
#             return True
#     return False

# import random
# lista = random.sample(range(100),5)
# print(sorted(lista))
# searchLinear(lista, 13)

# name = 'tiago'
# resultado = name.index('a')
# print(resultado)

# def executar_busca_binaria(lista, valor):
#     minimo = 0
#     maximo = len(lista) - 1
#     while minimo <= maximo:
#         meio = (minimo + maximo) // 2
#         if valor < lista[meio]:
#             maximo = meio - 1
#         elif valor > lista[meio]:
#             minimo = meio + 1
#         else:
#             return True
#     return False

# lista = list(range(1, 50))
# print(f"\n{lista}")
# print(f"\n{executar_busca_binaria(lista=lista, valor=10)}")
# print(f"\n{executar_busca_binaria(lista=lista, valor=20)}")


#-------------
# Algoritmos de ordenação

list = [10, 34, 2, 7, -5]

print(f"\nLista: {list}")

listaOrdenadaOne = sorted(list)
listaOrdenadaTwo = list.sort()

print(f"ListaOrdenada com sorted: {listaOrdenadaOne}")
print(f"ListaOrdenada com sort: {listaOrdenadaTwo}")

