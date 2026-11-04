import pandas as pd
import numpy as np

imoveis = pd.read_csv("imoveis_bruto.csv", na_values=["N/D", "?", "s/i"])
imoveis["bairro"] = imoveis["bairro"].str.strip().str.title()
imoveis["idade_anos"] = imoveis["idade_anos"].replace(-1, np.nan)
imoveis = imoveis.drop_duplicates(subset=[c for c in imoveis.columns if c != "id_anuncio"])

imoveis["idade_ausente"] = imoveis["idade_anos"].isna()
for col in ["area_m2", "idade_anos"]:
            imoveis[col] = imoveis[col].fillna(imoveis.groupby("tipo")[col].transform("median"))
for col in ["distancia_praia_km"]:
            imoveis[col] = imoveis[col].fillna(imoveis.groupby("bairro")[col].transform("median"))
imoveis["condicao"] = imoveis["condicao"].fillna(imoveis["condicao"].mode()[0])

print(imoveis[["area_m2", "idade_anos", "distancia_praia_km","condicao"]].isna().sum())
