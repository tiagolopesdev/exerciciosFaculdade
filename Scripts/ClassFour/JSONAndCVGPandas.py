import pandas as pd

result = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json").head()
print("Resultado com JSON:")
print(result)