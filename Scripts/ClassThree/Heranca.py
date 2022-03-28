class Veiculo:
    def __init__(self, tipo, marca, modelo):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo

class Moto(Veiculo):
    def __init__(self, tipo, marca, modelo, cilindrada):
        super().__init__(tipo, marca, modelo)
        self.cilindrada = cilindrada

v = Veiculo('Carro', "FIAT", "Sedan")
m = Moto("Moto", "Yamaha", "YBR", "125")
print(f"\nVeiculo\n-{v.marca}\n-{v.modelo}\n-{v.tipo}")
print(f"\nMoto\n-{m.marca}\n-{m.modelo}\n-{m.tipo}\n-{m.cilindrada}")