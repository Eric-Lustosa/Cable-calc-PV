class TrechoCabo:
    def __init__(
        self,
        tipo,  # "DC" ou "AC"
        origem,
        destino,
        corrente,
        tensao,
        comprimento,
        tipo_instalacao,
        numero_cabos,
        temperatura_solo,
        resistividade_solo,
        afastamento,
        disposicao,
        tipo_circuito="trifasico"  # só aplicável se tipo == "AC"
    ):
        self.tipo = tipo.upper()
        self.origem = origem
        self.destino = destino
        self.corrente = corrente
        self.tensao = tensao
        self.comprimento = comprimento
        self.tipo_instalacao = tipo_instalacao
        self.numero_cabos = numero_cabos
        self.temperatura_solo = temperatura_solo
        self.resistividade_solo = resistividade_solo
        self.afastamento = afastamento
        self.disposicao = disposicao

        # Se for AC, armazenar tipo_circuito ("monofasico" ou "trifasico")
        self.tipo_circuito = tipo_circuito.lower() if self.tipo == "AC" else None
