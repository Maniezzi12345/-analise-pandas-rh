import pandas as pd


def carregar_dados(funcionarios):
    df = pd.DataFrame(funcionarios)
    return df


def filtrar_ativos(df):
    return df[df["status"] == "ativo"]


def agrupar_por_depto(df):
    df_agrupado = df.groupby("depto").agg(
        quantidade=("nome", "count"),
        folha=("salario", "sum")
    ).reset_index()
    return df_agrupado


def maior_folha(df_agrupado):
    idx   = df_agrupado["folha"].idxmax()
    linha = df_agrupado.loc[idx]
    return f"Maior folha: {linha['depto']} — R$ {linha['folha']:.2f}"