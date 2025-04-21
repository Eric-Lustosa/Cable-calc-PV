import csv

def carregar_fatores_de_csv(caminho_csv, chave_coluna, valor_coluna):
    fatores = {}
    with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            chave = row[chave_coluna]
            valor = float(row[valor_coluna])
            # converte número de cabos para int, se possível
            try:
                chave = int(chave)
            except ValueError:
                chave = chave.lower()
            fatores[chave] = valor
    return fatores
