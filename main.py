from utils import reader
from utils.fatores import carregar_fatores_de_csv
from calculators.dimensionamento import dimensionar_trecho
from models.trecho_cabo import TrechoCabo
from utils.reader import carregar_projeto_json
from utils.reports import salvar_relatorio_txt
# === Entradas do sistema ===

queda_maxima_pct = 1.5

# Exemplo de sistema: Inversor string COM combiner AC
queda_maxima_pct, trechos = carregar_projeto_json("inputs/projeto.json")

# === Carregar dados dos cabos ===
cabos = reader.carregar_cabos_de_csv("data/cables.csv")
queda_maxima_pct, trechos = reader.carregar_projeto_json("inputs/projeto.json")

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
relatorio = ""

for i, trecho in enumerate(trechos):
    # mesma lógica de prints...
    relatorio += f"\nTrecho {i + 1}: {trecho.origem} → {trecho.destino} ({trecho.tipo})\n"
    relatorio += "📥 Entradas:\n"
    relatorio += f"  - Corrente: {trecho.corrente} A\n"
    relatorio += f"  - Tensão: {trecho.tensao} V\n"
    relatorio += f"  - Comprimento (ida): {trecho.comprimento} m\n"
    relatorio += f"  - Método de instalação: {trecho.tipo_instalacao.replace('_', ' ').title()}\n"
    relatorio += f"  - Nº de cabos agrupados: {trecho.numero_cabos}\n"
    relatorio += f"  - Temperatura do solo: {trecho.temperatura_solo} °C\n"
    relatorio += f"  - Resistividade térmica do solo: {trecho.resistividade_solo} K·m/W\n"
    relatorio += f"  - Afastamento: {trecho.afastamento}\n"
    relatorio += f"  - Disposição: {trecho.disposicao}\n"
    relatorio += f"  - Queda de tensão máxima permitida: {queda_maxima_pct:.2f} %\n"

    if resultado:
        relatorio += "✅ Resultado:\n"
        relatorio += f"  → Cabo sugerido: {cabo.modelo} ({cabo.secao_mm2} mm²)\n"
        relatorio += f"  → Capacidade corrigida: {resultado['capacidade_corrigida']:.1f} A\n"
        relatorio += f"  → Queda de tensão obtida: {resultado['queda_v']:.2f} V ({resultado['queda_pct']:.2f}%)\n"
    else:
        relatorio += "❌ Nenhum cabo atende aos critérios para esse trecho.\n"

salvar_relatorio_txt("reports/relatorio_projeto.txt", relatorio)
print("\n📄 Relatório salvo em: reports/relatorio_projeto.txt")