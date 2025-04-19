# Cable-calc-PV
# PV Cable Tool

Ferramenta em Python para cálculo de queda de tensão e capacidade de condução de corrente em sistemas fotovoltaicos, considerando cabos AC e DC, com suporte para inversores string e centrais.

## Objetivos

- Lógica clara com orientação a objetos (OO)
- Cálculos conforme normas NBR 5410, NBR 16690 e IECs europeias
- Pronto para receber interface gráfica no futuro
- Importação de dados de cabos e equipamentos via arquivos ou API

## Uso básico (exemplo inicial)

```bash
python main.py

pv_cable_tool/
├── data/              # Dados de entrada (ex: cables.csv)
├── models/            # Definição de classes
├── calculators/       # Módulos de cálculo
├── utils/             # Funções auxiliares (leitura, conversão, etc)
├── main.py            # Ponto de entrada para testes
