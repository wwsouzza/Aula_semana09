import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

imoveis = pd.read_csv("imoveis_tratado.csv")
X = imoveis.drop(columns=["preco", "id_anuncio", "preco_atipico"])
y = np.log1p(imoveis["preco"])
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_treino.shape, X_teste.shape)


def montar_prep():
    """Monta o ColumnTransformer: escala, ordinal, One-Hot e binárias."""
    numericas = ["area_m2", "quartos", "banheiros", "vagas", "idade_anos", "distancia_praia_km"]
    binarias = ["aceita_pet", "mobiliado", "idade_ausente"]
    return ColumnTransformer([
        ("num", StandardScaler(), numericas),
        ("ord", OrdinalEncoder(categories=[["Ruim", "Regular", "Bom", "Ótimo"]]), ["condicao"]),
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["tipo", "bairro"]),
        ("bin", OrdinalEncoder(categories=[["Não", "Sim"], ["Não", "Sim"], [False, True]]), binarias),
    ])

prep = montar_prep()
Xt_treino = prep.fit_transform(X_treino)
Xt_teste = prep.transform(X_teste)
print(Xt_treino.shape, "|", Xt_teste.shape)

# 7. Obter nomes das colunas geradas
nomes_colunas = prep.get_feature_names_out()

# Impressão dos resultados
print(f"Shape X_train transformado: {Xt_treino.shape}")
print(f"Shape X_test transformado:  {Xt_teste.shape}")
print("\nPrimeiras 10 colunas geradas no pipeline:")
print(nomes_colunas[:10])