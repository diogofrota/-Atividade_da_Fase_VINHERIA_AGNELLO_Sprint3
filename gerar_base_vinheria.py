import random
from datetime import datetime, timedelta

import pandas as pd


random.seed(42)

TOTAL_REGISTROS = 500

produtos = {
    "Vinho Tinto Reserva": {"categoria": "Tinto", "preco_base": 229},
    "Cabernet Sauvignon": {"categoria": "Tinto", "preco_base": 169},
    "Vinho Branco Chardonnay": {"categoria": "Branco", "preco_base": 139},
    "Vinho Rose Premium": {"categoria": "Rose", "preco_base": 149},
    "Espumante Brut": {"categoria": "Espumante", "preco_base": 119},
    "Merlot Selecionado": {"categoria": "Tinto", "preco_base": 159},
    "Sauvignon Blanc": {"categoria": "Branco", "preco_base": 129},
    "Prosecco Italiano": {"categoria": "Espumante", "preco_base": 189},
}

canais_venda = ["Loja Fisica", "Site", "Marketplace", "WhatsApp"]
regioes = ["Sul", "Sudeste", "Centro-Oeste", "Nordeste", "Norte"]
tipos_cliente = ["Novo", "Recorrente"]
formas_pagamento = ["Cartao de Credito", "Pix", "Boleto", "Cartao de Debito"]
campanhas = ["Sim", "Nao"]
descontos = [0, 5, 10, 15, 20, 25, 30]


def limitar_probabilidade(valor):
    return max(0.10, min(0.90, valor))


def calcular_probabilidade_sucesso(registro):
    probabilidade_sucesso = 0.50

    if registro["Tipo_Cliente"] == "Recorrente":
        probabilidade_sucesso += 0.15

    if registro["Avaliacao_Cliente"] >= 4:
        probabilidade_sucesso += 0.15
    elif registro["Avaliacao_Cliente"] <= 2:
        probabilidade_sucesso -= 0.10

    if 5 <= registro["Desconto"] <= 15:
        probabilidade_sucesso += 0.10
    elif registro["Desconto"] >= 25:
        probabilidade_sucesso -= 0.04

    if registro["Preco"] > 250:
        probabilidade_sucesso -= 0.10

    if registro["Tempo_Entrega_Dias"] > 7:
        probabilidade_sucesso -= 0.15

    if registro["Custo_Frete"] > 40:
        probabilidade_sucesso -= 0.10

    if registro["Campanha_Marketing"] == "Sim":
        probabilidade_sucesso += 0.08

    if registro["Canal_Venda"] in ["Site", "WhatsApp"]:
        probabilidade_sucesso += 0.05

    if registro["Forma_Pagamento"] == "Pix":
        probabilidade_sucesso += 0.04
    elif registro["Forma_Pagamento"] == "Boleto":
        probabilidade_sucesso -= 0.04

    probabilidade_sucesso += random.uniform(-0.12, 0.12)

    return limitar_probabilidade(probabilidade_sucesso)


def gerar_registro(id_venda):
    produto = random.choice(list(produtos.keys()))
    dados_produto = produtos[produto]

    preco = max(59, round(random.gauss(dados_produto["preco_base"], 38)))
    quantidade = random.choices([1, 2, 3, 4, 5, 6, 7, 8], weights=[25, 22, 17, 13, 9, 7, 4, 3])[0]
    canal_venda = random.choices(canais_venda, weights=[28, 30, 18, 24])[0]
    regiao = random.choices(regioes, weights=[20, 34, 14, 18, 14])[0]
    tipo_cliente = random.choices(tipos_cliente, weights=[45, 55])[0]
    desconto = random.choices(descontos, weights=[22, 18, 20, 17, 12, 7, 4])[0]
    avaliacao_cliente = random.choices([1, 2, 3, 4, 5], weights=[6, 10, 24, 32, 28])[0]
    tempo_entrega = random.choices(range(1, 13), weights=[10, 14, 16, 14, 12, 9, 7, 6, 4, 3, 3, 2])[0]
    forma_pagamento = random.choices(formas_pagamento, weights=[42, 32, 12, 14])[0]
    campanha_marketing = random.choices(campanhas, weights=[46, 54])[0]

    custo_base_regiao = {
        "Sul": 22,
        "Sudeste": 24,
        "Centro-Oeste": 34,
        "Nordeste": 42,
        "Norte": 48,
    }[regiao]
    custo_frete = round(max(8, random.gauss(custo_base_regiao, 8)), 2)

    data_inicial = datetime(2025, 1, 1)
    data_venda = data_inicial + timedelta(days=random.randint(0, 485))

    registro = {
        "ID_Venda": id_venda,
        "Data_Venda": data_venda.strftime("%d/%m/%Y"),
        "Produto": produto,
        "Categoria": dados_produto["categoria"],
        "Preco": preco,
        "Quantidade": quantidade,
        "Canal_Venda": canal_venda,
        "Regiao": regiao,
        "Tipo_Cliente": tipo_cliente,
        "Desconto": desconto,
        "Avaliacao_Cliente": avaliacao_cliente,
        "Tempo_Entrega_Dias": tempo_entrega,
        "Forma_Pagamento": forma_pagamento,
        "Campanha_Marketing": campanha_marketing,
        "Custo_Frete": custo_frete,
    }

    probabilidade_sucesso = calcular_probabilidade_sucesso(registro)
    registro["Venda_Sucesso"] = "Sim" if random.random() < probabilidade_sucesso else "Nao"

    return registro


def gerar_base():
    registros = [gerar_registro(id_venda) for id_venda in range(1, TOTAL_REGISTROS + 1)]
    return pd.DataFrame(registros)


if __name__ == "__main__":
    df = gerar_base()
    df.to_csv("base_vendas_vinheria.csv", index=False)
    df.to_excel("base_vendas_vinheria.xlsx", index=False)

    total_sucesso = (df["Venda_Sucesso"] == "Sim").sum()
    total_falha = (df["Venda_Sucesso"] == "Nao").sum()

    print("Base gerada com sucesso.")
    print(f"Total de registros: {len(df)}")
    print(f"Vendas com sucesso: {total_sucesso}")
    print(f"Vendas sem sucesso: {total_falha}")
