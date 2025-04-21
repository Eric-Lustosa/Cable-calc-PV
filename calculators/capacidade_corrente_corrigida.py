def calcular_capacidade_corrigida(cabo, tipo_instalacao, numero_cabos, fatores_instalacao, fatores_agrupamento):
    """
    Aplica os fatores de correção à capacidade nominal do cabo.
    """
    f_instalacao = fatores_instalacao.get(tipo_instalacao.lower(), 1.0)
    f_agrupamento = fatores_agrupamento.get(numero_cabos, 1.0)

    capacidade_corrigida = cabo.capacidade_nominal_a * f_instalacao * f_agrupamento
    return capacidade_corrigida
