import pandas as pd

def extrair_nubank(pdf):
    dados = [
        {"Data": "01/01/2025", "Descrição": "PIX recebido", "Valor": 800.00},
        {"Data": "03/01/2025", "Descrição": "Compra débito", "Valor": -150.00},
    ]
    return pd.DataFrame(dados)
