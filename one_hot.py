import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

imoveis = pd.read_csv("imoveis_tratado.csv")
codificado = pd.get_dummies(imoveis, columns=["tipo", "bairro"], drop_first=True, dtype=int)
print(imoveis.shape, "->", codificado.shape)
print([c for c in codificado.columns if c.startswith("tipo_")])
print("soma por linha:", todas.sum(axis=1).unique())