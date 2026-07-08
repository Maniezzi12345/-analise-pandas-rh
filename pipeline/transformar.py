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

def salario_medio_por_depto(df):
    return df.groupby("depto")["salario"].mean().reset_index()

def funcionario_maior_salario(df):
    idx = df["salario"].idxmax()
    return df.loc[idx]


# Vamos implementar uma função com funcionarios abaixo da media geral 

def abaixo_da_media(df):
    media = df["salario"].mean()
    return df[df["salario"] < media]

def ranking_salario(df):
    return df.sort_values("salario",ascending=False)

def contar_por_status(df):
    return df.groupby("status")["nome"].count().reset_index()

def top_3_salarios(df):
    return df.sort_values("salario", ascending=False).head(3)

def depto_mais_funcionarios(df):
    grupo = df.groupby("depto")["nome"].count().reset_index()
    grupo.columns = ["depto", "quantidade"]
    return grupo.sort_values("quantidade", ascending=False).head(1)

def funcionario_por_depto_e_status(df):
    return df.groupby(["depto", "status"])["nome"].count().reset_index()

def media_salarial_ativos_por_depto(df):
    ativos = df[df["status"] == "ativo"]
    resultado = ativos.groupby("depto")["salario"].mean().reset_index()
    resultado = resultado.sort_values("salario", ascending=False)

    return resultado


def funcionarios_acima_de(df, valor):
    return df[df["salario"] > valor].sort_values("salario", ascending=False)

def resumo_geral(df):
        return {
            "total":       df["nome"].count(),
            "media":       df["salario"].mean(),
            "maior":       df["salario"].max(),
            "menor":       df["salario"].min(),
            "folha_total": df["salario"].sum()
        }



# WHERE   → df[df["col"] == valor]
# GROUP BY → .groupby("col")
# SELECT  → ["col"]
# AVG     → .mean()
# ORDER BY → .sort_values("col", ascending=False)
# LIMIT   → .head(n)