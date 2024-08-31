import json

with open('faturamento.json', 'r') as file:
    data = json.load(file)

valores = [entry['valor'] for entry in data]

menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
