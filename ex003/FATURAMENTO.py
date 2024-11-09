#IMPORTAR ARQUIVO
import json

#CARREGAR DADOS DO ARQUIVO JSON
with open("faturamento.json") as file:
    dados = json.load(file)
faturamento_diario = dados["faturamento"]

#REMOVER DIAS SEM FATURAMENTO
faturamento_validado = [valor for valor in faturamento_diario if valor >0]

#CALCULANDO MENOR E MAIOR VALOR DE FATURAMENTO
menor_faturamento = min(faturamento_validado)
maior_faturamento = max(faturamento_validado)

#CALCULANDO A MÉDIA
MEDIA = sum(faturamento_validado) / len(faturamento_validado)

#DESTACAR DIAS COM FATURAMENTO ACIMA DA MÉDIA
SUPERIOR_A_MEDIA = sum(1 for valor in faturamento_validado if valor > MEDIA)

#IMPRIMIR OS RESULTADOS
print("Menor faturamento: ", menor_faturamento)
print("Maior faturamento: ", maior_faturamento)
print("Faturamento acima da média: ", SUPERIOR_A_MEDIA)

#FIM DO PROGRAMA

