def calcular_queda_tensao_dc(cabo, corrente, comprimento_m):
    """
    Calcula a queda de tensão em V para sistema DC com ida e volta.
    Usa resistência em ohm/km, já considerando a seção.
    """
    comprimento_km = comprimento_m / 1000
    delta_v = 2 * corrente * cabo.resistividade_ohm_km * comprimento_km
    return delta_v