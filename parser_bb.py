import pandas as pd

def extrair_bb(pdf):
    dados = [
        {"Data": "05/01/2025", "Descrição": "TED recebida", "Valor": 1200.00},
        {"Data": "06/01/2025", "Descrição": "Pagamento boleto", "Valor": -300.00},
    ]
    return pd.DataFrame(dados)
