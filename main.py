from utils.reader import carregar_cabos_de_csv
from utils.fatores import carregar_fatores_de_csv
from calculators.capacidade_corrente_corrigida import calcular_capacidade_corrigida
from calculators.voltage_drop import calcular_queda_tensao_dc
from cable_selector.cable_selector import sugerir_cabo_dc  # novo nome da pasta

# === Entradas do projeto ===
corrente_circuito = 60
comprimento = 1000
tensao_nominal = 1500
queda_maxima = 1.5
tipo_instalacao = "eletroduto_no_solo"
numero_cabos = 3
temperatura_solo = 30                    # °C
resistividade_solo = 1.5                 # K·m/W
afastamento = "10cm"                     # string igual ao CSV
disposicao = "horizontal"                # string igual ao CSV

# === Carregar dados ===
cabos = carregar_cabos_de_csv("data/cables.csv")
fatores_instalacao = carregar_fatores_de_csv("data/fatores_instalacao.csv", "tipo_instalacao", "fator")
fatores_agrupamento = carregar_fatores_de_csv("data/fatores_agrupamento.csv", "numero_cabos", "fator")
fatores_temp = carregar_fatores_de_csv("data/fatores_temperatura.csv", "temperatura", "fator")
fatores_resist = carregar_fatores_de_csv("data/fatores_resistividade_solo.csv", "resistividade_km_per_w", "fator")
fatores_afast = carregar_fatores_de_csv("data/fatores_afastamento.csv", "afastamento", "fator")
fatores_disp = carregar_fatores_de_csv("data/fatores_disposicao.csv", "disposicao", "fator")


# === Filtrar cabos que atendem à corrente corrigida e à queda de tensão ===
cabos_validos = []

for cabo in sorted(cabos, key=lambda c: c.secao_mm2):
    capacidade_corrigida = calcular_capacidade_corrigida(
    cabo,
    tipo_instalacao,
    numero_cabos,
    temperatura_solo,
    resistividade_solo,
    afastamento,
    disposicao,
    fatores_instalacao,
    fatores_agrupamento,
    fatores_temp,
    fatores_resist,
    fatores_afast,
    fatores_disp
)


    #Texto teste para bott.dev

    if capacidade_corrigida < corrente_circuito:
        continue  # Não atende à capacidade

    delta_v = calcular_queda_tensao_dc(cabo, corrente_circuito, comprimento)
    delta_v_pct = (delta_v / tensao_nominal) * 100

    if delta_v_pct > queda_maxima:
        continue  # Não atende à queda de tensão

    cabos_validos.append((cabo, capacidade_corrigida, delta_v, delta_v_pct))
    break  # pega apenas o menor cabo que atende aos dois critérios

# === Mostrar o resultado ===
print("==== RESULTADO ====")
print(f"Corrente do circuito: {corrente_circuito} A")
print(f"Comprimento (ida): {comprimento} m")
print(f"Tensão nominal: {tensao_nominal} V")
print(f"Queda de tensão máxima permitida: {queda_maxima}%")
print(f"Tipo de instalação: {tipo_instalacao.replace('_', ' ').title()}")
print(f"Cabos no mesmo eletroduto/vala: {numero_cabos}")
print("--------------------")

if cabos_validos:
    cabo, capacidade, queda_v, queda_pct = cabos_validos[0]
    print(f"✅ Cabo sugerido: {cabo.modelo} ({cabo.secao_mm2} mm²)")
    print(f"Capacidade corrigida: {capacidade:.1f} A")
    print(f"Queda de tensão: {queda_v:.2f} V ({queda_pct:.2f}%)")
else:
    print("❌ Nenhum cabo atende simultaneamente à corrente e à queda de tensão.")
