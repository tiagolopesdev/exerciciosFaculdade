qnt_faltas = int(input("Qnt faltas:"))
media = float(input("Digite a média final:"))

if qnt_faltas <= 5 and media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado!")