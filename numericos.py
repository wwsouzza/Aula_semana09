import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def limites_iqr(serie, k=1.5):
    """Devolve os limites inferior e superior pelo método do IQR."""
    q1, q3 = serie.quantile([0.25, 0.75])
    iqr = q3 - q1
    return q1 - k * iqr, q3 + k * iqr


def _tratar(df):
    """Remove erros de digitação e marca preços atípicos reais."""
    # 1. Regras de negócio para remover erros
    erros = (
        (df["area_m2"] > 2000)
        | (df["preco"] < 10_000)
        | (df["quartos"] > 10)
    )
    df = df[~erros].copy()

    # 2. Sinalizar preços atípicos com IQR
    baixo, alto = limites_iqr(df["preco"])
    df["preco_atipico"] = (df["preco"] > alto) | (df["preco"] < baixo)

    return df.reset_index(drop=True)


def preparar_numericos(caminho):
    df = pd.read_csv(caminho)
    df_tratado = _tratar(df)

    # 3. Salvar imoveis_tratado.csv (antes de escalar)
    df_tratado.to_csv("imoveis_tratado.csv", index=False)

    # 4. Divisão Treino / Teste (80/20, random_state=42)
    train, test = train_test_split(df_tratado, test_size=0.2, random_state=42)

    colunas_escalar = ["area_m2", "quartos", "idade_anos"]

    # 5. StandardScaler com FIT APENAS no treino para evitar vazamento (data leakage)
    scaler = StandardScaler()
    scaler.fit(train[colunas_escalar])

    # Aplicar a transformação em ambos os conjuntos
    train_scaled = train.copy()
    test_scaled = test.copy()

    train_scaled[colunas_escalar] = scaler.transform(train[colunas_escalar])
    test_scaled[colunas_escalar] = scaler.transform(test[colunas_escalar])

    return train_scaled, test_scaled


if __name__ == "__main__":
    caminho_csv = "imoveis_limpo.csv"
    train, test = preparar_numericos(caminho_csv)

    colunas = ["area_m2", "quartos", "idade_anos"]

    # Impressões finais exigidas
    print(f"Tamanho Treino: {len(train)} | Tamanho Teste: {len(test)}")
    print("\nMédia das colunas escaladas no TREINO (esperado ~ 0):")
    print(train[colunas].mean().round(4))
    print("\nMédia das colunas escaladas no TESTE:")
    print(test[colunas].mean().round(4))