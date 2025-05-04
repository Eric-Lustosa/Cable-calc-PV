import os
from datetime import datetime

def salvar_relatorio_txt(caminho_arquivo, trechos_resultados, queda_maxima_pct, nome_projeto="Sistema Fotovoltaico"):
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)

    data_hoje = datetime.today().strftime("%d/%m/%Y")

    texto = f"{'='*40}\n"
    texto += "RELATÓRIO DE DIMENSIONAMENTO DE CABOS\n"
    texto += f"Projeto: {nome_projeto}\n"
    texto += f"Data: {data_hoje}\n"
    texto += f"{'='*40}\n\n"

    for i, item in enumerate(trechos_resultados):
        trecho = item["trecho"]
        resultado = item["resultado"]

        texto += f"Trecho {i + 1}: {trecho.origem} → {trecho.destino} ({trecho.tipo})\n"
        texto += "-"*40 + "\n"
        texto += "📥 ENTRADAS:\n"
        texto += f"  Corrente nominal........: {trecho.corrente} A\n"
        texto += f"  Tensão..................: {trecho.tensao} V\n"
        texto += f"  Comprimento (ida).......: {trecho.comprimento} m\n"
        texto += f"  Instalação..............: {trecho.tipo_instalacao.replace('_', ' ').title()}\n"
        texto += f"  Nº cabos agrupados......: {trecho.numero_cabos}\n"
        texto += f"  Temperatura do solo.....: {trecho.temperatura_solo} °C\n"
        texto += f"  Resistividade do solo...: {trecho.resistividade_solo} K·m/W\n"
        texto += f"  Afastamento.............: {trecho.afastamento}\n"
        texto += f"  Disposição..............: {trecho.disposicao}\n"
        texto += f"  Queda máxima permitida..: {queda_maxima_pct:.2f} %\n"

        if resultado:
            cabo = resultado["cabo"]
            texto += "\n✅ RESULTADO:\n"
            texto += f"  Cabo sugerido...........: {cabo.modelo} ({cabo.secao_mm2} mm²)\n"
            texto += f"  Capacidade corrigida....: {resultado['capacidade_corrigida']:.1f} A\n"
            texto += f"  Queda de tensão.........: {resultado['queda_v']:.2f} V ({resultado['queda_pct']:.2f}%)\n"
        else:
            texto += "\n❌ RESULTADO:\n"
            texto += "  Nenhum cabo atende aos critérios para esse trecho.\n"

        texto += "-"*40 + "\n\n"

    # Rodapé
    texto += "Gerado automaticamente por Cable-Calc-PV\n"

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(texto)
