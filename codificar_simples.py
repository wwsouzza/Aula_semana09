import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder

imoveis = pd.read_csv("imoveis_tratado.csv")

print(imoveis.select_dtypes(exclude=["number", "bool"]).columns.tolist())

sim_nao = { "Sim": 1, "Não": 0}
for col in ["aceita_pet" , "mobiliado" ]:
 imoveis[col] = imoveis[col]. map(sim_nao)
imoveis[["idade_ausente" , "preco_atipico" ]] = imoveis[[ "idade_ausente" ,
"preco_atipico" ]].astype( int)
print(imoveis[[ "aceita_pet" , "mobiliado" , "idade_ausente" ]].head(4))
print(imoveis["aceita_pet" ].isna().sum(), "sem correspondência" )

ordem = {"Ruim": 0, "Regular": 1, "Bom": 2, "Ótimo": 3}
imoveis["condicao_num"] = imoveis["condicao"].map(ordem)
print(imoveis[["condicao", "condicao_num"]].drop_duplicates().sort_values("condicao_num"))
print(imoveis["condicao_num"].isna().sum(), "sem correspondência")

from sklearn.preprocessing import OrdinalEncoder
enc = OrdinalEncoder(categories=[[ "Ruim", "Regular", "Bom", "Ótimo"]])
valores = enc.fit_transform(imoveis[[ "condicao"]])
print(enc.categories_)
print(valores[:5].ravel())
