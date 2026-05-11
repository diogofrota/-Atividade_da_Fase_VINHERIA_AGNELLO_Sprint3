<div align="center">

# 🍷 Vinheria Agnello

### Machine Learning e Business Intelligence para previsão de sucesso de vendas

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Decision%20Tree-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/Status-Base%20com%20Ru%C3%ADdo-111827?style=for-the-badge)

**Projeto de Ciência de Dados que aplica Aprendizado Supervisionado para prever o sucesso de vendas de uma vinheria utilizando uma base simulada, probabilística e com ruído controlado.**

</div>

---

## 📌 Descrição do Projeto

O projeto **Vinheria Agnello** simula um cenário comercial de uma vinheria e utiliza **Machine Learning** para prever se uma venda tem maior probabilidade de sucesso.

A base de dados foi reprojetada para ser mais realista: em vez de seguir uma regra perfeita, a variável alvo `Venda_Sucesso` é gerada por probabilidade. Isso permite que o conjunto contenha exceções naturais, como vendas com cliente recorrente que falham, vendas caras que dão certo, avaliações baixas com sucesso e vendas com desconto que não convertem.

Esse desenho torna o projeto mais próximo de um problema real de negócio, em que dados possuem incerteza, ruído, variação e padrões imperfeitos.

---

## 🎯 Objetivos

| Objetivo | Descrição |
|---|---|
| Prever sucesso de vendas | Classificar vendas como `Sim` ou `Nao` para sucesso comercial. |
| Simular dados realistas | Criar uma base com variação, ruído e exceções. |
| Aplicar Aprendizado Supervisionado | Treinar um modelo com variável alvo conhecida. |
| Avaliar modelo preditivo | Medir desempenho com acurácia, precisão, recall e F1-score. |
| Apoiar decisões comerciais | Identificar fatores que impactam conversão de vendas. |
| Conectar análise e BI | Usar Power BI para análise visual de indicadores comerciais. |

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso no projeto |
|---|---|
| **Python** | Geração da base, modelagem e avaliação. |
| **Pandas** | Manipulação de dados e exportação CSV/XLSX. |
| **Scikit-Learn** | Separação treino/teste, modelo e métricas. |
| **DecisionTreeClassifier** | Algoritmo de classificação por Árvore de Decisão. |
| **LabelEncoder** | Codificação de variáveis categóricas. |
| **Power BI** | Dashboard de vendas e análise executiva. |
| **Excel** | Versão tabular da base simulada. |

---

## 📁 Estrutura do Projeto

```text
Vinheria_Agnello_Projeto/
├── gerar_base_vinheria.py         # Gera a base simulada com probabilidade e ruído
├── base_vendas_vinheria.csv       # Base principal consumida pelo modelo
├── base_vendas_vinheria.xlsx      # Versão Excel da base simulada
├── modelo_vinheria.py             # Treina e avalia o modelo de Árvore de Decisão
├── dashboard_vinheria.pbix        # Dashboard Power BI do projeto
├── relatorio_vinheria.docx        # Relatório complementar
├── venv/                          # Ambiente virtual local
└── README.md                      # Documentação do projeto
```

---

## 🗃️ Base de Dados

A base é gerada pelo arquivo:

```bash
python gerar_base_vinheria.py
```

Arquivos de saída:

```text
base_vendas_vinheria.csv
base_vendas_vinheria.xlsx
```

A versão atual possui **500 registros** e **16 colunas**. Cada registro representa uma venda simulada com atributos comerciais, operacionais, logísticos e comportamentais.

### Dicionário de Dados

| Coluna | Tipo | Descrição |
|---|---:|---|
| `ID_Venda` | Numérica | Identificador único da venda. |
| `Data_Venda` | Data | Data simulada da venda. |
| `Produto` | Categórica | Nome do vinho vendido. |
| `Categoria` | Categórica | Categoria do vinho: tinto, branco, rosé ou espumante. |
| `Preco` | Numérica | Preço unitário simulado do produto. |
| `Quantidade` | Numérica | Quantidade de unidades vendidas. |
| `Canal_Venda` | Categórica | Canal utilizado: loja física, site, marketplace ou WhatsApp. |
| `Regiao` | Categórica | Região geográfica da venda. |
| `Tipo_Cliente` | Categórica | Cliente `Novo` ou `Recorrente`. |
| `Desconto` | Numérica | Percentual de desconto aplicado. |
| `Avaliacao_Cliente` | Numérica | Avaliação do cliente em escala de 1 a 5. |
| `Tempo_Entrega_Dias` | Numérica | Tempo estimado de entrega em dias. |
| `Forma_Pagamento` | Categórica | Forma de pagamento utilizada. |
| `Campanha_Marketing` | Categórica | Indica se a venda recebeu influência de campanha. |
| `Custo_Frete` | Numérica | Custo simulado de frete. |
| `Venda_Sucesso` | Categórica | Variável alvo: `Sim` ou `Nao`. |

---

## 🎲 Simulação Probabilística e Ruído

A coluna `Venda_Sucesso` não é definida por uma regra determinística. O script calcula uma probabilidade inicial e ajusta essa chance conforme características da venda.

Exemplo conceitual:

```python
probabilidade_sucesso = 0.50

if Tipo_Cliente == "Recorrente":
    probabilidade_sucesso += 0.15

if Avaliacao_Cliente >= 4:
    probabilidade_sucesso += 0.15

if 5 <= Desconto <= 15:
    probabilidade_sucesso += 0.10

if Preco > 250:
    probabilidade_sucesso -= 0.10

if Tempo_Entrega_Dias > 7:
    probabilidade_sucesso -= 0.15

if Custo_Frete > 40:
    probabilidade_sucesso -= 0.10

if Campanha_Marketing == "Sim":
    probabilidade_sucesso += 0.08

if Canal_Venda in ["Site", "WhatsApp"]:
    probabilidade_sucesso += 0.05
```

Depois disso, a probabilidade é limitada entre **0.10** e **0.90** e a venda é sorteada com aleatoriedade:

```python
Venda_Sucesso = "Sim" if random.random() < probabilidade_sucesso else "Nao"
```

### Por que isso é importante?

| Característica | Impacto |
|---|---|
| Ruído controlado | Evita que o modelo memorize uma regra perfeita. |
| Exceções realistas | Permite casos contraditórios, comuns em dados reais. |
| Métricas menos artificiais | Reduz a chance de resultados perfeitos como `1.0`. |
| Melhor análise crítica | Obriga a interpretar erros, limitações e incerteza. |

---

## 🎯 Variáveis do Modelo

### Variáveis de Entrada

```python
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
```

| Variável | Papel esperado |
|---|---|
| `Produto` | Captura diferenças de comportamento por vinho. |
| `Categoria` | Agrupa padrões por tipo de produto. |
| `Preco` | Pode reduzir conversão em faixas muito altas. |
| `Quantidade` | Representa volume comprado. |
| `Canal_Venda` | Site e WhatsApp podem ter conversão superior. |
| `Regiao` | Ajuda a capturar diferenças geográficas. |
| `Tipo_Cliente` | Clientes recorrentes tendem a converter mais. |
| `Desconto` | Descontos moderados podem elevar a chance de sucesso. |
| `Avaliacao_Cliente` | Avaliações altas tendem a favorecer sucesso. |
| `Tempo_Entrega_Dias` | Entregas longas podem reduzir a conversão. |
| `Forma_Pagamento` | Algumas formas podem facilitar ou dificultar conclusão. |
| `Campanha_Marketing` | Campanhas elevam levemente a probabilidade. |
| `Custo_Frete` | Fretes altos podem reduzir a chance de venda. |

### Variável Alvo

```python
y = df["Venda_Sucesso"]
```

| Variável | Descrição |
|---|---|
| `Venda_Sucesso` | Resultado da venda, com valores `Sim` ou `Nao`. |

---

## 🔄 Preparação dos Dados

As variáveis categóricas são convertidas para formato numérico com `LabelEncoder`, permitindo que o `DecisionTreeClassifier` processe os atributos.

```python
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
```

> Em uma solução produtiva, `OneHotEncoder` e `ColumnTransformer` podem ser alternativas mais robustas para variáveis categóricas nominais.

---

## 🌳 Algoritmo: Árvore de Decisão

O modelo utiliza o algoritmo **Decision Tree Classifier**, uma técnica supervisionada de classificação que divide os dados em regras sucessivas para separar as classes da variável alvo.

No projeto, a árvore procura padrões entre atributos como avaliação, desconto, preço, canal de venda, frete, entrega e tipo de cliente para prever `Venda_Sucesso`.

### Configuração Utilizada

```python
modelo = DecisionTreeClassifier(
    max_depth=6,
    min_samples_leaf=8,
    random_state=42
)
```

| Parâmetro | Finalidade |
|---|---|
| `max_depth=6` | Limita a profundidade da árvore e reduz overfitting. |
| `min_samples_leaf=8` | Evita folhas muito pequenas e regras excessivamente específicas. |
| `random_state=42` | Garante reprodutibilidade. |

---

## ✂️ Separação Treino e Teste

O conjunto é dividido em **70% para treino** e **30% para teste**.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)
```

| Conjunto | Percentual | Finalidade |
|---|---:|---|
| Treino | 70% | Aprendizado dos padrões. |
| Teste | 30% | Avaliação em dados não vistos durante o treinamento. |

---

## 📊 Métricas do Modelo

Resultado obtido após gerar a nova base probabilística e executar o modelo:

| Métrica | Resultado |
|---|---:|
| Acurácia | `0.8000` |
| Precisão | `0.8560` |
| Recall | `0.8992` |
| F1-Score | `0.8770` |
| Total de registros | `500` |
| Vendas com sucesso | `373` |
| Vendas sem sucesso | `127` |

### Interpretação das Métricas

| Métrica | Interpretação |
|---|---|
| Acurácia | Mede a proporção total de classificações corretas. |
| Precisão | Mede a confiabilidade das previsões positivas. |
| Recall | Mede a capacidade de encontrar vendas que realmente tiveram sucesso. |
| F1-Score | Equilibra precisão e recall em uma única métrica. |

O resultado não é perfeito, o que é desejável neste projeto. A presença de ruído e exceções reduz o risco de uma avaliação artificialmente alta e torna a análise mais próxima de um cenário comercial real.

---

## 📉 Dashboard Power BI

O dashboard `dashboard_vinheria.pbix` pode ser utilizado para explorar indicadores comerciais e operacionais da base.

### Indicadores Recomendados

| Indicador | Finalidade |
|---|---|
| Total de vendas | Volume de transações simuladas. |
| Taxa de sucesso | Proporção de vendas com `Venda_Sucesso = Sim`. |
| Vendas por canal | Comparação entre loja física, site, marketplace e WhatsApp. |
| Vendas por região | Distribuição geográfica das vendas. |
| Ticket médio | Análise de preço e quantidade. |
| Desconto médio | Avaliação de incentivos comerciais. |
| Tempo médio de entrega | Análise operacional e logística. |
| Custo médio de frete | Impacto logístico na conversão. |
| Sucesso por campanha | Comparação entre vendas com e sem campanha. |

---

## 🔎 Insights Possíveis

| Insight | Leitura de negócio |
|---|---|
| Clientes recorrentes tendem a converter melhor | Relacionamento e fidelização podem aumentar vendas. |
| Avaliações altas elevam a chance de sucesso | Experiência do cliente afeta desempenho comercial. |
| Descontos moderados podem ajudar | Incentivos equilibrados podem melhorar conversão. |
| Preços altos nem sempre impedem sucesso | Produtos premium ainda podem converter em alguns contextos. |
| Entrega e frete afetam decisão | Custos e prazos logísticos influenciam a compra. |
| Campanhas têm impacto incremental | Marketing pode elevar a probabilidade, mas não garante venda. |
| Site e WhatsApp podem ter boa conversão | Canais digitais podem ser relevantes para vendas consultivas. |

---

## 🚀 Como Executar

### 1. Acessar a pasta do projeto

```bash
cd Vinheria_Agnello_Projeto
```

### 2. Criar ambiente virtual

macOS ou Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependências

```bash
python -m pip install --upgrade pip
pip install pandas scikit-learn openpyxl
```

### 4. Gerar a base simulada

```bash
python gerar_base_vinheria.py
```

Saída esperada:

```text
Base gerada com sucesso.
Total de registros: 500
Vendas com sucesso: 373
Vendas sem sucesso: 127
```

### 5. Executar o modelo

```bash
python modelo_vinheria.py
```

Saída esperada:

```text
Acurácia: 0.8
Precisão: 0.856
Recall: 0.8991596638655462
F1-Score: 0.8770491803278688
Total de registros: 500
Quantidade de vendas com sucesso: 373
Quantidade de vendas sem sucesso: 127
```

---

## 🧪 Fluxo do Projeto

```text
Gerador probabilístico
   ↓
Base CSV e XLSX
   ↓
Leitura com Pandas
   ↓
Codificação com LabelEncoder
   ↓
Separação 70/30
   ↓
Treinamento da Árvore de Decisão
   ↓
Predição no conjunto de teste
   ↓
Cálculo das métricas
   ↓
Análise no Power BI
```

---

## 🧩 Conceitos Aplicados

| Conceito | Aplicação |
|---|---|
| Aprendizado Supervisionado | Modelo treinado com variável alvo conhecida. |
| Classificação | Previsão binária de sucesso ou falha da venda. |
| Simulação probabilística | Geração da variável alvo com chance ajustada por fatores de negócio. |
| Ruído em dados | Inclusão de exceções para evitar padrões perfeitos. |
| Pré-processamento | Codificação numérica de variáveis categóricas. |
| Generalização | Avaliação em conjunto de teste separado. |
| Métricas de classificação | Uso de acurácia, precisão, recall e F1-score. |
| Business Intelligence | Visualização dos indicadores no Power BI. |

---

## 📌 Possíveis Melhorias Futuras

| Melhoria | Benefício |
|---|---|
| Aumentar volume histórico | Melhorar robustez estatística. |
| Usar dados reais | Aproximar o modelo do comportamento de mercado. |
| Aplicar validação cruzada | Medir estabilidade em múltiplas divisões. |
| Comparar algoritmos | Testar Random Forest, Gradient Boosting e Regressão Logística. |
| Criar pipeline Scikit-Learn | Unificar pré-processamento e treinamento. |
| Usar OneHotEncoder | Tratar variáveis nominais de forma mais adequada. |
| Analisar importância das variáveis | Entender os fatores de maior impacto. |
| Criar matriz de confusão | Visualizar erros por classe. |
| Publicar dashboard | Disponibilizar relatório no Power BI Service. |
| Criar API preditiva | Expor o modelo para uso em sistemas comerciais. |

---

## ✅ Checklist

| Etapa | Status |
|---|---|
| Script gerador da base | ✅ Concluído |
| Base CSV atualizada | ✅ Concluído |
| Base Excel atualizada | ✅ Concluído |
| Base com 500 registros | ✅ Concluído |
| Variável alvo probabilística | ✅ Concluído |
| Ruído e exceções simuladas | ✅ Concluído |
| Modelo com novas variáveis | ✅ Concluído |
| Separação 70/30 | ✅ Concluído |
| Métricas não perfeitas | ✅ Concluído |
| README atualizado | ✅ Concluído |

---

## 📜 Licença

Este projeto é disponibilizado para fins acadêmicos, educacionais e de portfólio.

O conteúdo pode ser utilizado e adaptado para estudos e demonstrações técnicas, mantendo os devidos créditos ao autor.

---

## 👤 Autor

**Projeto:** Vinheria Agnello  
**Área:** Ciência de Dados, Machine Learning e Business Intelligence  
**Ferramentas:** Python, Pandas, Scikit-Learn e Power BI  

<div align="center">

### 🍷 Vinheria Agnello

**Transformando dados comerciais em inteligência para decisões estratégicas.**

</div>
