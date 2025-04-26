def calcular_queda_tensao(cabo, corrente, comprimento_m, tipo_sinal="DC", tipo_circuito="trifasico"):
    """
    Calcula a queda de tensão para sistemas DC ou AC.

    tipo_sinal: "AC" ou "DC"
    tipo_circuito (se AC): "monofasico" ou "trifasico"
    """
    comprimento_km = comprimento_m / 1000
    r = cabo.resistividade_ohm_km

    if tipo_sinal.upper() == "DC":
        return 2 * corrente * r * comprimento_km

    if tipo_circuito == "trifasico":
        return (3 ** 0.5) * corrente * r * comprimento_km
    else:  # monofásico
        return 2 * corrente * r * comprimento_km
