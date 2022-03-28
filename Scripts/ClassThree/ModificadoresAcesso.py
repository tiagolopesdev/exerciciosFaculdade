class People():
    nome = ''
    idade = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def andar(self):
        print("Andando")
    
    def __ligar(self):
        print("Em ligação")

class Functionary(People):
    ocupacao = 'Desemprego'
    salario = 0

    def __init__(self, nome, idade, ocupacao, salario):
        super().__init__(nome, idade)
        self.ocupacao = ocupacao
        self.salario = salario

    def trabalho(self):
        print("Funcionário está trabalhando.")
        self.andar
    
    def ligacao(self):
        self.__ligar()
        print("Funcionário está em ligação")

functionaryOne = Functionary("Tiago", 19, "Developer", 1000)

functionaryOne.trabalho()
functionaryOne.ligacao()
