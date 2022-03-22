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

text = "Python Java Go Kotlin C C# PHP Lua Go".split()

print(f"Antes da listcomp: {text}")
text = [item.lower() for item in text] # upper(): elementos em caixa alta, lower(): elementos em caixa baixa
print(f"Depois da listcomp: {text}")



