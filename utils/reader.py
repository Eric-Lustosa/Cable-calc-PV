import csv
import json
from models.cable import Cable
from models.trecho_cabo import TrechoCabo

def carregar_cabos_de_csv(caminho_csv):
    cabos = []
    with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cabo = Cable(
                fabricante=row["fabricante"],
                modelo=row["modelo"],
                secao_mm2=float(row["seção_mm2"]),
                resistividade_ohm_km=float(row["resistividade_ohm_km"]),
                isolamento=row["isolamento"],
                tipo_cabo=row["tipo_cabo"],
                capacidade_nominal_a=float(row["capacidade_nominal_a"])
            )
            cabos.append(cabo)
    return cabos

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
            tipo_circuito=t.get("tipo_circuito", "trifasico")
        )
        trechos.append(trecho)

    return queda_maxima_pct, trechos
