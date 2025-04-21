import csv
from models.cable import Cable

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
                capacidade_nominal_a=float(row["capacidade_nominal_a"])  # <- novo campo
            )
            cabos.append(cabo)
    return cabos