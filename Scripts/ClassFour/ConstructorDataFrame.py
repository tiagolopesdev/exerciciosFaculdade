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