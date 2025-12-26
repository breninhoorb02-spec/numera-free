def classificar(descricao, valor):
    descricao = descricao.lower()

    if valor > 0:
        if "salário" in descricao or "salario" in descricao:
            return "Receita - Salários"
        if "pix" in descricao:
            return "Receita - Pix"
        return "Receita Geral"

    else:
        if "aluguel" in descricao:
            return "Despesa - Aluguel"
        if "energia" in descricao or "luz" in descricao:
            return "Despesa - Energia"
        if "internet" in descricao:
            return "Despesa - Internet"
        if "pix" in descricao:
            return "Despesa - Pix"
        return "Despesa Geral"
