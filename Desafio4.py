faturamento_mensal_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 19849.53,
    "OUTROS": 19849.53,
}

faturamento_total = 0
for faturamento in faturamento_mensal_estado.values():
    faturamento_total += faturamento

percentual_faturamento_estado = {}
for estado,faturamento in faturamento_mensal_estado.items():
    percentual = 100*faturamento/faturamento_total

    percentual_faturamento_estado[estado] = round(percentual,2)

print(percentual_faturamento_estado)
   
   
