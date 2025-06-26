# Predição de Vendas com Regressão Linear

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)
![Pandas](https://img.shields.io/badge/pandas-latest-blue.svg)
![Matplotlib](https://img.shields.io/badge/matplotlib-latest-orange.svg)

 Um projeto de ciência de dados que demonstra o uso de um modelo de regressão linear simples para prever vendas de produtos com base no orçamento de publicidade. Este projeto mostra habilidades de manipulação de dados, treinamento de modelos, avaliação e visualização.

![Gráfico de Predição de Vendas](assets/Sales%20Prediction%20TV%20Advertising%20Budget.png)

---

## 📖 Índice
- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Conjunto de Dados](#conjunto-de-dados)
- [Começando](#começando)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Contato](#contato)

---

## 🎯 Sobre o Projeto

O objetivo deste projeto é construir um modelo de regressão linear simples que prevê vendas com base no investimento em publicidade na TV. Serve como um exemplo prático de um fluxo de trabalho completo (embora básico) de aprendizado de máquina.

Principais características demonstradas:
- **Carregamento e Preparação de Dados:** Obtém um conjunto de dados de uma URL e o prepara para modelagem usando Pandas.
- **Treinamento do Modelo:** Implementa um modelo de regressão linear usando Scikit-learn.
- **Avaliação do Modelo:** Calcula o Erro Quadrático Médio (RMSE) para avaliar o desempenho do modelo.
- **Visualização de Dados:** Cria um gráfico de dispersão com uma linha de regressão usando Matplotlib para visualizar a relação entre publicidade na TV e vendas.

---

## 🛠️ Tecnologias Utilizadas

Este projeto utiliza uma variedade de bibliotecas e ferramentas padrão de ciência de dados:

- **Linguagem de Programação:**
  - `Python 3.13`
- **Bibliotecas e Frameworks:**
  - `Scikit-learn`: Para construir o modelo de regressão linear e avaliação do modelo.
  - `Pandas`: Para manipulação de dados e carregamento do conjunto de dados.
  - `Matplotlib`: Para criação de visualizações (gráfico de dispersão e linha de regressão).
  - `NumPy`: Para operações numéricas, especificamente para calcular a raiz quadrada do RMSE.
  - `Requests`: Para obter o conjunto de dados de uma URL.

---

## 📊 Conjunto de Dados

O modelo é treinado no conjunto de dados "Advertising", que contém dados sobre o impacto de diferentes canais de publicidade nas vendas.

- **Fonte:** [An Introduction to Statistical Learning](https://www.statlearning.com/s/Advertising.csv)
- **Características Utilizadas:**
  - `TV`: Orçamento de publicidade na TV (em milhares de dólares).
- **Variável Alvo:**
  - `sales`: Vendas de produtos (em milhares de unidades).

---

## 🚀 Começando

Siga estas instruções para obter uma cópia do projeto funcionando em sua máquina local.

### Pré-requisitos

Certifique-se de ter o Python 3 instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

### Instalação

1.  **Clone o repositório:**
   
    git clone https://github.com/ovitelas/predicao-vendas.git
    cd predicao-vendas
    
   

2.  **Crie um ambiente virtual (recomendado):**
    
    python -m venv venv
   

3.  **Instale as dependências necessárias:**
    
    pip install -r requirements.txt
    

---

## Como Usar

Para executar o script, execute o seguinte comando no terminal:


python sales_prediction.py


O script irá:
1.  Baixar o conjunto de dados `Advertising.csv`.
2.  Treinar o modelo de regressão linear.
3.  Exibir o Erro Quadrático Médio (RMSE) no console.
4.  Mostrar um gráfico visualizando as vendas reais versus as vendas previstas.

---

✍️ Autor

Victor Hugo B. Soares
📧 [E-mail - contatovictorhugosoares@gmail.com](contatovictorhugosoares@gmail.com)
🌐 [LinkedIn](https://linkedin.com/in/ovitelas)
📞 [Telefone(WhatsApp) +55 11 964628356](https://wa.me/+5511964628356)


# 🇺🇸 Sales Prediction with Linear Regression

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)
![Pandas](https://img.shields.io/badge/pandas-latest-blue.svg)
![Matplotlib](https://img.shields.io/badge/matplotlib-latest-orange.svg)

 A data science project that demonstrates the use of a simple linear regression model to predict product sales based on advertising budget. This project showcases data handling, model training, evaluation, and visualization skills.

![Sales Prediction Plot](assets/Sales%20Prediction%20TV%20Advertising%20Budget.png)
  

---

## 📖 Table of Contents
- [About the Project](#about-the-project)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

---

## 🎯 About the Project

The goal of this project is to build a simple linear regression model that predicts sales based on the money invested in TV advertising. It serves as a practical example of a complete, albeit basic, machine learning workflow.

Key features demonstrated:
- **Data Loading and Preparation:** Fetches a dataset from a URL and prepares it for modeling using Pandas.
- **Model Training:** Implements a linear regression model using Scikit-learn.
- **Model Evaluation:** Calculates the Root Mean Squared Error (RMSE) to evaluate the model's performance.
- **Data Visualization:** Creates a scatter plot with a regression line using Matplotlib to visualize the relationship between TV advertising and sales.

---

## 🛠️ Tech Stack

This project utilizes a range of standard data science libraries and tools:

- **Programming Language:**
  - `Python 3.13`
- **Libraries & Frameworks:**
  - `Scikit-learn`: For building the linear regression model and for model evaluation.
  - `Pandas`: For data manipulation and loading the dataset.
  - `Matplotlib`: For creating visualizations (scatter plot and regression line).
  - `NumPy`: For numerical operations, specifically for calculating the square root for RMSE.
  - `Requests`: For fetching the dataset from a URL.

---

## 📊 Dataset

The model is trained on the "Advertising" dataset, which contains data on the impact of different advertising channels on sales.

- **Source:** [An Introduction to Statistical Learning](https://www.statlearning.com/s/Advertising.csv)
- **Features Used:**
  - `TV`: Advertising budget for TV (in thousands of dollars).
- **Target Variable:**
  - `sales`: Product sales (in thousands of units).

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1.  **Clone the repository:**
   
    git clone https://github.com/ovitelas/predicao-vendas.git
    cd predicao-vendas
    
   

2.  **Create a virtual environment (recommended):**
    
    python -m venv venv
   

3.  **Install the required dependencies:**
    
    pip install -r requirements.txt
    

---

## Usage

To run the script, execute the following command in your terminal:


python sales_prediction.py


The script will:
1.  Download the `Advertising.csv` dataset.
2.  Train the linear regression model.
3.  Print the Root Mean Squared Error (RMSE) to the console.
4.  Display a plot visualizing the actual sales vs. the predicted sales.

---

✍️ Autor

Victor Hugo B. Soares
📧 [E-mail - contatovictorhugosoares@gmail.com](contatovictorhugosoares@gmail.com)
🌐 [LinkedIn](https://linkedin.com/in/ovitelas)
📞 [Telefone(WhatsApp) +55 11 964628356](https://wa.me/+5511964628356)