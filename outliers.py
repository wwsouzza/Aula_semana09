import pandas as pd
import numpy as np

imoveis = pd.read_csv("imoveis_limpo.csv")


# Revelando os dadaso estatisiticos dos imóveis
print(imoveis.shape)
cols = ["area_m2" , "quartos" , "idade_anos" , "preco"]
print(imoveis[cols].describe(). round(1))


# Função para calcular os limites inferior e superior de outliers usando o método do IQR
def limites_iqr(serie, k=1.5):
    q1, q3 = serie.quantile([0.25, 0.75])
    iqr = q3 - q1
    return q1 - k * iqr, q3 + k * iqr


for col in ["area_m2", "quartos", "idade_anos", "preco"]:
    baixo, alto = limites_iqr(imoveis[col])
    n = ((imoveis[col] < baixo) | (imoveis[col] > alto)).sum()
    print(f"{col:11s} {n:3d} fora de [{baixo:,.0f}; {alto:,.0f}]")

# Calculando o z-score para a coluna "area_m2" e identificando outliers com |z| > 3
z = (imoveis["area_m2"] - imoveis["area_m2"].mean()) / imoveis["area_m2"].std()
print("desvio padrão:", imoveis["area_m2"].std().round(1))
print((z.abs() > 3).sum(), "com |z| > 3")
print(z.sort_values().tail(3).round(2).tolist())


# Calculando o z-score para a coluna "area_m2" sem o maior erro e identificando outliers com |z| > 3
sem_erro = imoveis[imoveis[ "area_m2"] < 2000]["area_m2"]
z2 = (sem_erro - sem_erro.mean()) / sem_erro.std()
print((z2.abs() > 3).sum(), "com |z| > 3 sem o maior erro" )
print("desvio padrão:" , sem_erro.std(). round(1))

imoveis["preco_m2"] = imoveis["preco"] / imoveis["area_m2"]
suspeitos = imoveis[(imoveis["area_m2"] > 600) | (imoveis["preco"] < 50_000) | (imoveis["quartos"] > 10)]
print(suspeitos[["id_anuncio", "tipo", "area_m2", "quartos", "preco", "preco_m2"]].round(0))