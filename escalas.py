import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

imoveis = pd.read_csv("imoveis_tratado.csv")
colunas = ["area_m2", "quartos", "idade_anos", "preco"]

# 1. Mostrar o mínimo e máximo das colunas
print("--- Mínimo e Máximo ---")
print(imoveis[colunas].agg(["min", "max"]).round(0))

cols_num = ["area_m2", "quartos", "idade_anos", "preco"]
a = imoveis.loc[ 0, cols_num].astype( float)
b = imoveis.loc[ 1, cols_num].astype( float)
dif2 = (a - b) ** 2
print((100 * dif2 / dif2. sum()).round(2))

# 2. Aplicar os três scalers às 4 colunas
minmax = MinMaxScaler()
standard = StandardScaler()
robust = RobustScaler()

df_minmax = pd.DataFrame(
    minmax.fit_transform(imoveis[colunas]), columns=colunas
)
df_standard = pd.DataFrame(
    standard.fit_transform(imoveis[colunas]), columns=colunas
)
df_robust = pd.DataFrame(
    robust.fit_transform(imoveis[colunas]), columns=colunas
)

# 3. Confirmar que MinMax vai de 0 a 1 e StandardScaler dá média 0

print("\n--- MinMaxScaler (Min / Max) ---")
print(df_minmax.agg(["min", "max", "std"]).round(2))

print("\n--- StandardScaler (Média / Desvio Padrão) ---")
print(df_standard.agg(["mean", "std"]).round(2))

print("\n--- RobustScaler (Mediana / Mín / Máx) ---")
print(df_robust.agg(["mean", "std", "min", "max"]).round(2))
