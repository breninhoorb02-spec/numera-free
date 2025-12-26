import pandas as pd

def extrair_bradesco(pdf):
    dados = [
        {"Data": "02/01/2025", "Descrição": "Crédito cliente", "Valor": 950.00},
        {"Data": "04/01/2025", "Descrição": "Débito automático", "Valor": -220.00},
    ]
    return pd.DataFrame(dados)
