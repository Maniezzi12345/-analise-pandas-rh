print("iniciando...")
from dados.funcionarios import funcionarios
print("dados importados")
from pipeline.transformar import carregar_dados, filtrar_ativos, agrupar_por_depto, maior_folha
print("funções importadas")

df     = carregar_dados(funcionarios)
print("df criado")
ativos = filtrar_ativos(df)
print("ativos filtrados")
grupos = agrupar_por_depto(ativos)
print("agrupado")
maior  = maior_folha(grupos)
print("maior calculado")

print("=== RELATÓRIO DE FUNCIONÁRIOS ===")
print()
print(grupos.to_string(index=False))
print()
print(maior)