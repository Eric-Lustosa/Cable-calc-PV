def calcular_capacidade_corrigida(
    cabo,
    tipo_instalacao,
    numero_cabos,
    temp_solo,
    resist_terminca_solo,
    afastamento,
    disposicao,
    fatores_instalacao,
    fatores_agrupamento,
    fatores_temp,
    fatores_resist_solo,
    fatores_afastamento,
    fatores_disposicao
):
    f_instalacao = fatores_instalacao.get(tipo_instalacao.lower(), 1.0)
    f_agrupamento = fatores_agrupamento.get(numero_cabos, 1.0)
    f_temp = fatores_temp.get(temp_solo, 1.0)
    f_resist = fatores_resist_solo.get(resist_terminca_solo, 1.0)
    f_afast = fatores_afastamento.get(afastamento.lower(), 1.0)
    f_disp = fatores_disposicao.get(disposicao.lower(), 1.0)

    capacidade_corrigida = (
        cabo.capacidade_nominal_a *
        f_instalacao *
        f_agrupamento *
        f_temp *
        f_resist *
        f_afast *
        f_disp
    )

    return capacidade_corrigida
