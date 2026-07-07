from dados.funcionarios import funcionarios
from pipeline.transformar import (
    carregar_dados,
    filtrar_ativos,
    agrupar_por_depto,
    maior_folha,
    salario_medio_por_depto,
    funcionario_maior_salario,
    abaixo_da_media,
    ranking_salario,
    contar_por_status,
    top_3_salarios
)

# pipeline
df     = carregar_dados(funcionarios)
ativos = filtrar_ativos(df)
grupos = agrupar_por_depto(ativos)
maior  = maior_folha(grupos)
medio  = salario_medio_por_depto(ativos)
top    = funcionario_maior_salario(ativos)
abaixo = abaixo_da_media(ativos)
ranking = ranking_salario (ativos)
status = contar_por_status(df)
top3 = top_3_salarios(df)
# relatório
print("=== RELATÓRIO DE FUNCIONÁRIOS ===")
print()
print(grupos.to_string(index=False))
print()
print(maior)
print()
print("=== SALÁRIO MÉDIO POR DEPTO ===")
print(medio.to_string(index=False))
print()
print(f"Funcionário top: {top['nome']} — R$ {top['salario']:.2f} — {top['depto']}")
print()
print()
print("=== FUNCIONÁRIOS ABAIXO DA MÉDIA ===")
print(abaixo[["nome", "depto", "salario"]].to_string(index=False))

print()
print("=== RANKING DE SALÁRIOS ===")
print(ranking[["nome", "depto", "salario"]].to_string(index=False))

print()
print("=== FUNCIONÁRIOS POR STATUS ===")
print(status.to_string(index=False))

print()
print("=== TOP 3 SALÁRIOS ===")
print(top3[["nome", "depto", "salario"]].to_string(index=False))