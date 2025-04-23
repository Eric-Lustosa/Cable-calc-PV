from utils.reader import carregar_cabos_de_csv
from utils.fatores import carregar_fatores_de_csv
from calculators.dimensionamento import dimensionar_trecho
from models.trecho_cabo import TrechoCabo

# === Entradas do sistema ===

queda_maxima_pct = 1.5

# Exemplo de sistema: Inversor string COM combiner AC
trechos = [
    TrechoCabo("DC", "string", "inversor", 10, 600, 30, "eletroduto_no_solo", 2, 30, 1.5, "sem_afastamento", "horizontal"),
    TrechoCabo("AC", "inversor", "combiner_box_ac", 25, 230, 50, "eletroduto_no_solo", 3, 30, 1.5, "10cm", "horizontal"),
    TrechoCabo("AC", "combiner_box_ac", "trafo", 120, 400, 80, "direto_no_solo", 4, 30, 2.0, "20cm", "trifolio"),
]

# === Carregar dados dos cabos ===
cabos = carregar_cabos_de_csv("data/cables.csv")

# === Carregar fatores de correção ===
fatores_instalacao = carregar_fatores_de_csv("data/fatores_instalacao.csv", "tipo_instalacao", "fator")
fatores_agrupamento = carregar_fatores_de_csv("data/fatores_agrupamento.csv", "numero_cabos", "fator")
fatores_temp = carregar_fatores_de_csv("data/fatores_temperatura.csv", "temperatura", "fator")
fatores_resist = carregar_fatores_de_csv("data/fatores_resistividade_solo.csv", "resistividade_km_per_w", "fator")
fatores_afast = carregar_fatores_de_csv("data/fatores_afastamento.csv", "afastamento", "fator")
fatores_disp = carregar_fatores_de_csv("data/fatores_disposicao.csv", "disposicao", "fator")

# === Executar dimensionamento trecho a trecho ===

print("==== DIMENSIONAMENTO DO SISTEMA ====")

for i, trecho in enumerate(trechos):
    resultado = dimensionar_trecho(
        trecho=trecho,
        lista_cabos=cabos,
        fatores_instalacao=fatores_instalacao,
        fatores_agrupamento=fatores_agrupamento,
        fatores_temp=fatores_temp,
        fatores_resist_solo=fatores_resist,
        fatores_afastamento=fatores_afast,
        fatores_disposicao=fatores_disp,
        queda_maxima_pct=queda_maxima_pct
    )

    print(f"\nTrecho {i + 1}: {trecho.origem} → {trecho.destino} ({trecho.tipo})")
    print("📥 Entradas:")
    print(f"  - Corrente: {trecho.corrente} A")
    print(f"  - Tensão: {trecho.tensao} V")
    print(f"  - Comprimento (ida): {trecho.comprimento} m")
    print(f"  - Método de instalação: {trecho.tipo_instalacao.replace('_', ' ').title()}")
    print(f"  - Nº de cabos agrupados: {trecho.numero_cabos}")
    print(f"  - Temperatura do solo: {trecho.temperatura_solo} °C")
    print(f"  - Resistividade térmica do solo: {trecho.resistividade_solo} K·m/W")
    print(f"  - Afastamento: {trecho.afastamento}")
    print(f"  - Disposição: {trecho.disposicao}")
    print(f"  - Queda de tensão máxima permitida: {queda_maxima_pct:.2f} %")

    if resultado:
        cabo = resultado["cabo"]
        print("✅ Resultado:")
        print(f"  → Cabo sugerido: {cabo.modelo} ({cabo.secao_mm2} mm²)")
        print(f"  → Capacidade corrigida: {resultado['capacidade_corrigida']:.1f} A")
        print(f"  → Queda de tensão obtida: {resultado['queda_v']:.2f} V ({resultado['queda_pct']:.2f}%)")
    else:
        print("❌ Nenhum cabo atende aos critérios para esse trecho.")
        print(f"  → Provável motivo: corrente muito alta ou queda > {queda_maxima_pct:.2f}% com os cabos disponíveis.")
