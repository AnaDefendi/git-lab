def calcular_bonus(valor, tipo_cliente = "comum"):
    if tipo_cliente == "premium":
        return valor * 2
    return valor * 3
    