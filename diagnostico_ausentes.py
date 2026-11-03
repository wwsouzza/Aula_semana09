import pandas as pd
import numpy as np

imoveis = pd.read_csv("imoveis_bruto.csv")
print(imoveis.shape)
print(imoveis[["area_m2", "idade_anos", "preco"]].dtypes)

ausentes = imoveis.isna(). sum()
print(ausentes[ausentes > 0])

pct = (imoveis.isna().mean() * 100).round(1)
print(pct[pct > 0])

print(imoveis["condicao"].value_counts(dropna=False).tail(4))
print(imoveis["idade_anos"].min())
print(imoveis["area_m2"][pd.to_numeric(imoveis["area_m2"], errors="coerce").isna()].value_counts())

nao_informado = ["N/D", "?", "s/i"]
imoveis = pd.read_csv("imoveis_bruto.csv", na_values=nao_informado)
imoveis["idade_anos"] = imoveis["idade_anos"].replace(-1, np.nan)
print(imoveis["area_m2"].dtype)
print(imoveis.isna().sum()[lambda s: s > 0])

ausente_idade = imoveis[ "idade_anos"].isna().groupby(imoveis[ "tipo"]).mean()
print((ausente_idade * 100).round(1))