from utils.reader import carregar_cabos_de_csv
from utils.fatores import carregar_fatores_de_csv
from calculators.capacidade_corrente_corrigida import calcular_capacidade_corrigida
from selectors.cable_selector import sugerir_cabo_dc

# === Dados de entrada ===
corrente_circuito = 60
comprimento = 1000
tensao_nominal = 1500
queda_maxima = 1.5
tipo_instalacao = "eletroduto_no_solo"
numero_cabos = 3

# === Carregar dados ===
cabos = carregar_cabos_de_csv("data/cables.csv")
fatores_instalacao = carregar_fatores_de_csv("data/fatores_instalacao.csv", "tipo_instalacao", "fator")
fatores_agrupamento = carregar_fatores_de_csv("data/fatores_agrupamento.csv", "numero_cabos", "fator")

# === Filtrar cabos que suportam a corrente corrigida ===
cabos_filtrados = []
for cabo in cabos:
    capacidade_corrigida = calcular_capacidade_corrigida(
        cabo,
        tipo_instalacao,
        numero_cabos,
        fatores_instalacao,
        fatores_agrupamento
    )
    if capacidade_corrigida >= corrente_circuito:
        cabos_filtrados.append(cabo)

# === Buscar cabo com menor queda de tensão dentre os que atendem à corrente ===
from selectors.cable_selector import sugerir_cabo_dc

cabo_ideal, queda_v, queda_pct = sugerir_cabo_dc(
    cabos_filtrados,
    corrente_circuito,
    comprimento,
    tensao_nominal,
    queda_maxima
)

# === Saída ===
print("==== RESULTADO ====")
print(f"Corrente do circuito: {corrente_circuito} A")
print(f"Tipo de instalação: {tipo_instalacao.replace('_', ' ').title()}")
print(f"Cabos por eletroduto/vala: {numero_cabos}")
print(f"Queda de tensão máxima permitida: {queda_maxima}%")
print("--------------------")

if cabo_ideal:
    print(f"Cabo sugerido: {cabo_ideal.modelo} ({cabo_ideal.secao_mm2} mm²)")
    print(f"Queda de tensão: {queda_v:.2f} V ({queda_pct:.2f}%)")
else:
    print("❌ Nenhum cabo atende aos critérios definidos.")
