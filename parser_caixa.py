import pandas as pd

def extrair_caixa(pdf):
    dados = [
        {"Data": "07/01/2025", "Descrição": "Depósito", "Valor": 500.00},
        {"Data": "08/01/2025", "Descrição": "Saque", "Valor": -100.00},
    ]
    return pd.DataFrame(dados)
