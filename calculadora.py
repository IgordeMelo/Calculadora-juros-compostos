def calcular_juros_compostos(principal: float, taxa_mensal: float, meses: int, aporte_mensal: float = 0.0) -> dict:
    """
    ...
    """
    montante_principal = principal * (1 + taxa_mensal) ** meses

    if taxa_mensal > 0:
        montante_aportes = aporte_mensal * (((1 + taxa_mensal) ** meses - 1) / taxa_mensal)
    else:
        montante_aportes = aporte_mensal * meses

    montante_final = montante_principal + montante_aportes
    total_investido = principal + (aporte_mensal * meses)
    total_juros = montante_final - total_investido

    return {
        "montante_final": round(montante_final, 2),
        "total_investido": round(total_investido, 2),
        "total_juros": round(total_juros, 2)
    }

# a partir daqui, SEM indentação (fora da função):
if __name__ == "__main__":
    resultado = calcular_juros_compostos(
        principal=1000,
        taxa_mensal=0.01,
        meses=12,
        aporte_mensal=200
    )
    print(resultado)

   