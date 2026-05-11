import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder

# Carregar base
df = pd.read_csv("base_vendas_vinheria.csv")

# Converter dados categóricos
colunas_categoricas = [
    "Produto",
    "Categoria",
    "Canal_Venda",
    "Regiao",
    "Tipo_Cliente",
    "Forma_Pagamento",
    "Campanha_Marketing",
    "Venda_Sucesso"
]

for coluna in colunas_categoricas:
    df[coluna] = LabelEncoder().fit_transform(df[coluna])

# Variáveis de entrada
X = df[[
    "Produto",
    "Categoria",
    "Preco",
    "Quantidade",
    "Canal_Venda",
    "Regiao",
    "Tipo_Cliente",
    "Desconto",
    "Avaliacao_Cliente",
    "Tempo_Entrega_Dias",
    "Forma_Pagamento",
    "Campanha_Marketing",
    "Custo_Frete"
]]

# Variável alvo
y = df["Venda_Sucesso"]

# Separação treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Modelo
modelo = DecisionTreeClassifier(max_depth=6, min_samples_leaf=8, random_state=42)

modelo.fit(X_train, y_train)

# Previsão
y_pred = modelo.predict(X_test)

# Métricas
print("Acurácia:", accuracy_score(y_test, y_pred))
print("Precisão:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1-Score:", f1_score(y_test, y_pred))
print("Total de registros:", len(df))
print("Quantidade de vendas com sucesso:", int((df["Venda_Sucesso"] == 1).sum()))
print("Quantidade de vendas sem sucesso:", int((df["Venda_Sucesso"] == 0).sum()))
