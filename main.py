from utils.reader import carregar_cabos_de_csv
from utils.fatores import carregar_fatores_de_csv
from calculators.capacidade_corrente_corrigida import calcular_capacidade_corrigida
from calculators.voltage_drop import calcular_queda_tensao_dc

# === Dados de entrada ===
corrente_circuito = 60            # A
comprimento = 1000                # m (ida)
tensao_nominal = 1500             # V
queda_maxima = 1.5                # %
tipo_instalacao = "eletroduto_no_solo"
numero_cabos = 3

# === Carregar dados ===
cabos = carregar_cabos_de_csv("data/cables.csv")
fatores_instalacao = carregar_fatores_de_csv("data/fatores_instalacao.csv", "tipo_instalacao", "fator")
fatores_agrupamento = carregar_fatores_de_csv("data/fatores_agrupamento.csv", "numero_cabos", "fator")

# === Filtrar os cabos por ambos os critérios ===
cabos_validos = []

for cabo in sorted(cabos, key=lambda c: c.secao_mm2):
    # 1. Verifica a capacidade corrigida
    capacidade_corrigida = calcular_capacidade_corrigida(
        cabo,
        tipo_instalacao,
        numero_cabos,
        fatores_instalacao,
        fatores_agrupamento
    )

    if capacidade_corrigida < corrente_circuito:
        continue  # cabo não serve

    # 2. Verifica a queda de tensão
    delta_v = calcular_queda_tensao_dc(cabo, corrente_circuito, comprimento)
    delta_v_pct = (delta_v / tensao_nominal) * 100

    if delta_v_pct > queda_maxima:
        continue  # também não serve

    # 3. Se passou nos dois, é o primeiro válido (menor seção que atende)
    cabos_validos.append((cabo, capacidade_corrigida, delta_v, delta_v_pct))
    break

# === Resultado final ===
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
