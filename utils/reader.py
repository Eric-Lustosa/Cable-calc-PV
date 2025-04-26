import json
from models.trecho_cabo import TrechoCabo

def carregar_projeto_json(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)

    queda_maxima_pct = dados["queda_maxima_pct"]
    trechos = []

    for t in dados["trechos"]:
        trecho = TrechoCabo(
            tipo=t["tipo"],
            origem=t["origem"],
            destino=t["destino"],
            corrente=t["corrente"],
            tensao=t["tensao"],
            comprimento=t["comprimento"],
            tipo_instalacao=t["tipo_instalacao"],
            numero_cabos=t["numero_cabos"],
            temperatura_solo=t["temperatura_solo"],
            resistividade_solo=t["resistividade_solo"],
            afastamento=t["afastamento"],
            disposicao=t["disposicao"],
            tipo_circuito=t.get("tipo_circuito", "trifasico")  # padrão trifásico se não informado
        )
        trechos.append(trecho)

    return queda_maxima_pct, trechos
