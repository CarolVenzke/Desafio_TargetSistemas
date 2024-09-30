def faturamento_diario(faturamentos):    
    if not faturamentos:
        return "A lista de faturamentos está vazia."

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)

    media_mensal = sum(faturamentos) / len(faturamentos)

    dias_acima_media = sum(1 for faturamento in faturamentos if faturamento > media_mensal)

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_media": dias_acima_media
    }

faturamentos = [2000, 1000, 2400, 3600, 1700, 3200, 2900, 3000, 1500, 4000]
resultado = faturamento_diario(faturamentos)

print(f"Menor Faturamento: {resultado['menor_faturamento']}")
print(f"Maior Faturamento: {resultado['maior_faturamento']}")
print(f"Número de Dias Acima da Média: {resultado['dias_acima_media']}")
