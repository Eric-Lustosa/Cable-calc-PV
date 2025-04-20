from utils.reader import carregar_cabos_de_csv
from selectors.cable_selector import sugerir_cabo_dc

# Carregar todos os cabos do arquivo CSV
cabos = carregar_cabos_de_csv("data/cables.csv")

# === Dados de entrada do sistema ===
corrente = 60                # Corrente em Amperes
comprimento = 1000           # Comprimento do cabo (apenas ida), em metros
tensao_nominal = 1500        # Tensão nominal do sistema em Volts
queda_maxima = 1.5           # Queda de tensão máxima permitida, em %

# Buscar o menor cabo que atenda à condição de queda de tensão
cabo_ideal, queda_v, queda_pct = sugerir_cabo_dc(
    cabos,
    corrente,
    comprimento,
    tensao_nominal,
    queda_maxima
)

# Mostrar resultado
print("==== RESULTADO ====")
print(f"Corrente: {corrente} A")
print(f"Comprimento (ida): {comprimento} m")
print(f"Tensão nominal: {tensao_nominal} V")
print(f"Queda máxima permitida: {queda_maxima}%")
print("--------------------")

if cabo_ideal:
    print(f"Cabo sugerido: {cabo_ideal.modelo} ({cabo_ideal.secao_mm2} mm²)")
    print(f"Resistividade: {cabo_ideal.resistividade_ohm_km:.5f} Ω/km")
    print(f"Queda de tensão: {queda_v:.2f} V ({queda_pct:.2f}%)")
else:
    print(" Nenhum cabo atende aos critérios definidos.")
