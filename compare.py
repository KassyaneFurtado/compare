import pandas as pd

tabela1 = pd.read_csv("PCUNB1.csv") #planilha para comparar
tabela2 = pd.read_csv("PCU.csv") #planilha para comparar
print(tabela1)
print(tabela2)

#comparar uma coluna com a outra
tabela3 = pd.merge(tabela1, tabela2, on="PRONTUARIO")
print(tabela3)
tabela3.to_csv("PCUREDCAP.csv", index=False)