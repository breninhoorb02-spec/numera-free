import pandas as pd

def extrair_pdf_generico(pdf_file):
    # Parser genérico de teste
    dados = [
        {"Data": "01/01/2025", "Descrição": "Entrada exemplo", "Valor": 1500.00},
        {"Data": "02/01/2025", "Descrição": "Saída exemplo", "Valor": -200.00}
    ]
    return pd.DataFrame(dados)
