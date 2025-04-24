from calculators.capacidade_corrente_corrigida import calcular_capacidade_corrigida
from calculators.voltage_drop import calcular_queda_tensao


def dimensionar_trecho(
    trecho,
    lista_cabos,
    fatores_instalacao,
    fatores_agrupamento,
    fatores_temp,
    fatores_resist_solo,
    fatores_afastamento,
    fatores_disposicao,
    queda_maxima_pct
):
    """
    Retorna o menor cabo que atende à capacidade corrigida e à queda de tensão permitida para o trecho fornecido.
    """
    cabos_ordenados = sorted(lista_cabos, key=lambda c: c.secao_mm2)

    for cabo in cabos_ordenados:
        # Ignorar cabo se tipo não for compatível (ex: DC vs AC)
        if cabo.tipo_cabo.upper() != trecho.tipo.upper():
            continue

        # Calcular capacidade corrigida
        capacidade_corrigida = calcular_capacidade_corrigida(
            cabo,
            trecho.tipo_instalacao,
            trecho.numero_cabos,
            trecho.temperatura_solo,
            trecho.resistividade_solo,
            trecho.afastamento,
            trecho.disposicao,
            fatores_instalacao,
            fatores_agrupamento,
            fatores_temp,
            fatores_resist_solo,
            fatores_afastamento,
            fatores_disposicao
        )

        if capacidade_corrigida < trecho.corrente:
            continue

        # Calcular queda de tensão
        queda_v = calcular_queda_tensao_dc(cabo, trecho.corrente, trecho.comprimento)
        queda_pct = (queda_v / trecho.tensao) * 100

        if queda_pct > queda_maxima_pct:
            continue

        # Encontrou cabo ideal
        return {
            "trecho": trecho,
            "cabo": cabo,
            "queda_v": queda_v,
            "queda_pct": queda_pct,
            "capacidade_corrigida": capacidade_corrigida
        }

    # Nenhum cabo atende
    return None
