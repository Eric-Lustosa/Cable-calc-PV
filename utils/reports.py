import os

def salvar_relatorio_txt(caminho_arquivo, relatorio_texto):
    """
    Salva o conteúdo do relatório em um arquivo .txt.
    """
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(relatorio_texto)
