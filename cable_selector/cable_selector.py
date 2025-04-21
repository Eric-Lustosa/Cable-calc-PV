from calculators.voltage_drop import calcular_queda_tensao_dc

def sugerir_cabo_dc(cabos, corrente, comprimento_m, tensao_nominal_v, queda_tensao_max_percentual):
    """
    Retorna o menor cabo DC que atende à queda de tensão máxima permitida.
    """
    cabos_dc = sorted(
        [c for c in cabos if c.tipo_cabo.upper() == "DC"],
        key=lambda c: c.secao_mm2
    )

    for cabo in cabos_dc:
        delta_v = calcular_queda_tensao_dc(cabo, corrente, comprimento_m)
        delta_v_percentual = (delta_v / tensao_nominal_v) * 100

        if delta_v_percentual <= queda_tensao_max_percentual:
            return cabo, delta_v, delta_v_percentual

    return None, None, None  # Nenhum cabo atende aos critérios
