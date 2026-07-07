from dados.funcionarios import funcionarios
from pipeline.transformar import (
    carregar_dados,
    filtrar_ativos,
    agrupar_por_depto,
    maior_folha,
    salario_medio_por_depto,
    funcionario_maior_salario
)

# pipeline
df     = carregar_dados(funcionarios)
ativos = filtrar_ativos(df)
grupos = agrupar_por_depto(ativos)
maior  = maior_folha(grupos)
medio  = salario_medio_por_depto(ativos)
top    = funcionario_maior_salario(ativos)

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