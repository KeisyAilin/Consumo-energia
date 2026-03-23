print("\n=== Calculadora de Consuno Elétrico ===\n")

Aparelho = input("Nome do aparelho: ")
Potencia = float(input("Potência do aparelho em Watts: "))
Tempo = float(input("tempo médio de uso diario em horas: "))

ConsumoMensal = (Potencia * Tempo * 30) / 1000
ValorFixo = 0.75
CustoEstimado  = ConsumoMensal * ValorFixo

print("\n" + "-"*40)
print(f"Aparelho: {Aparelho.upper()}")
print("-"*40)
print(f"O consumo mensal é: {ConsumoMensal:.2f} kWh/mês")
print(f"O custo estimado é de: {CustoEstimado:.2f} por mês")