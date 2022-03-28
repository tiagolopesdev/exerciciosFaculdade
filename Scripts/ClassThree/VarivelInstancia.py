class televisao:
    def __init__(self):
        self.volume = 10
    
    def aumentarVolume(self):
        self.volume +=1
    
    def diminuirVolume(self):
        self.volume -=1

tv = televisao()
print(f"\nVolume ao ligar televisao: {tv.volume}")
tv.aumentarVolume()
print(f"\nVolume atual: {tv.volume}")