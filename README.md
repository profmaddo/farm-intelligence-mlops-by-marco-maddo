# farm-intelligence-mlops-by-marco-maddo
Farm Intelligence MLOps by Marco Maddo
---
# 🌾 MLOps Project: Agricultural Yield Prediction / Projeto MLOps: Previsão de Rendimento Agrícola

## 🇬🇧 Context and Objective
Predicting agricultural yield is essential for effective resource planning and maximizing production. This project demonstrates a complete MLOps solution using Python, MLflow, FastAPI, and Docker to simulate and predict crop yields based on factors like temperature, rainfall, soil pH, and fertilizer usage.

## 🇧🇷 Contexto e Objetivo
Prever o rendimento agrícola é essencial para o planejamento de recursos e maximização da produção. Este projeto demonstra uma solução completa de MLOps utilizando Python, MLflow, FastAPI e Docker para simular e prever a produtividade com base em fatores como temperatura, precipitação, pH do solo e uso de fertilizantes.

---

## 🇬🇧 Problem, Solution and Result
### Problem
Farmers and agronomists need intelligent tools to forecast yields. However, many do not have access to systems that can leverage data and machine learning.

### Solution
This project includes:
- Mock dataset with agricultural features
- Python training pipeline (Random Forest)
- Model deployment with FastAPI
- MLflow tracking
- Docker Compose orchestration
- Automated testing with pytest

### Result
With only 100 mock samples, the trained model reached a **Mean Squared Error (MSE) of ~16.8**. The FastAPI server returns instant predictions. All experiments are tracked in MLflow.

---


---

## 🇬🇧 Understanding the Evaluation Metric: Mean Squared Error (MSE)

In this project, the model's performance is evaluated using **MSE (Mean Squared Error)**. MSE is a common metric used in regression tasks to measure the average of the squares of the errors between predicted and actual values.

### 📐 Formula:
\[
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
\]

- \( y_i \): actual value
- \( \hat{y}_i \): predicted value
- \( n \): number of observations

### 📊 Interpretation:
- **MSE close to 0** means high accuracy
- **Higher MSE** indicates the model is making large errors
- In our training run, MSE ≈ **28.88**

---

## 🇧🇷 Entendendo a Métrica de Avaliação: Erro Quadrático Médio (MSE)

Neste projeto, a performance do modelo é avaliada utilizando o **MSE (Erro Quadrático Médio)**. O MSE é uma métrica comum em tarefas de regressão que mede a média dos quadrados dos erros entre os valores previstos e os reais.

### 📐 Fórmula:
\[
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
\]

- \( y_i \): valor real
- \( \hat{y}_i \): valor previsto
- \( n \): número de observações

### 📊 Interpretação:
- **MSE próximo de 0** indica alta precisão
- **MSE alto** indica que o modelo está cometendo grandes erros
- No nosso treinamento, MSE ≈ **28.88**


---

## 🇧🇷 Problema, Solução e Resultado
### Problema
Produtores rurais e agrônomos precisam de ferramentas inteligentes para prever o rendimento, mas muitos não têm acesso a sistemas baseados em dados e machine learning.

### Solução
Este projeto inclui:
- Base de dados simulada com variáveis agrícolas
- Pipeline de treinamento com Python (Random Forest)
- Deploy do modelo via FastAPI
- Rastreamento com MLflow
- Orquestração com Docker Compose
- Testes automatizados com pytest

### Resultado
Com apenas 100 amostras simuladas, o modelo treinado obteve um **Erro Quadrático Médio (MSE) de ~16.8**. A API FastAPI responde com previsões em tempo real. Todos os experimentos são rastreados no MLflow.

---
# Projeto MLOps: Previsão de Rendimento Agrícola

Este projeto demonstra um pipeline completo de MLOps com Python, incluindo:
- Treinamento de modelo com `scikit-learn`
- Deploy com `FastAPI`
- Monitoramento com `MLflow`
- Testes com `pytest`
- Containerização com `Docker`
- Orquestração com `docker-compose`
- CI/CD com GitHub Actions

---

## 🧭 Arquitetura do Projeto

![Arquitetura MLOps](https://github.com/profmaddo/farm-intelligence-mlops-by-marco-maddo/blob/main/images/mlops_architecture_diagram.png)

---

## 📁 Estrutura dos Diretórios

- `data/` → Base de dados simulada (mock)
- `models/` → Modelos treinados salvos em `.pkl`
- `api/` → API FastAPI para servir predições
- `test_api.py` → Testes com pytest
- `Dockerfile` → Container do serviço
- `docker-compose.yml` → Orquestração da API e do MLflow
- `Makefile` → Comandos para automação de tarefas
- `train.py` → Script de treino com MLflow

---

## ⚙️ CI/CD com GitHub Actions

O projeto conta com integração contínua via GitHub Actions. O workflow:
- Executa `pytest` para validar a API
- Garante que o modelo esteja treinável
- Pode ser estendido para deploy automático

---

## ▶️ Como Executar Localmente

```bash
# 1. Build do ambiente
make build

# 2. Treinar o modelo
make train

# 3. Executar a API
make run

# 4. Rodar MLflow separadamente (http://localhost:5000)
make mlflow

# 5. Testar com pytest
make test
```

---

## Autor
Projeto criado por Marco Maddo como exemplo educacional de MLOps com Python.

---


---

## 🗂️ Arquitetura do Projeto

A imagem abaixo resume o fluxo completo de MLOps:

![Arquitetura](diagrama_arquitetura_mlops.png)

---

## 🐳 Como rodar com Docker Compose

1. **Build dos serviços**
```bash
make build
```

2. **Treinamento do modelo**
```bash
make train
```

3. **Executar a API**
```bash
make run
```

4. **Iniciar o servidor MLflow**
```bash
make mlflow
```

5. **Rodar testes**
```bash
make test
```

---

## 🚀 CI/CD com GitHub Actions

Este projeto pode ser testado automaticamente com o seguinte workflow:

```yaml
name: CI - Test API

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      docker:
        image: docker:19.03.12
        options: --privileged
    steps:
    - uses: actions/checkout@v3

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2

    - name: Build container
      run: docker-compose build

    - name: Run tests
      run: docker-compose run --rm api pytest test_api.py
```

Para usar:
- Salve este conteúdo como `.github/workflows/test.yml` no seu repositório.
- Push para o GitHub e os testes rodarão automaticamente!

---



