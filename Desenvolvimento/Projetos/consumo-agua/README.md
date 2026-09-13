# 💧 Classificador de Consumo de Água

Um programa desenvolvido em **Python** para classificar o perfil de consumo de água de imóveis e apresentar mensagens educativas de acordo com o tipo de imóvel e o consumo mensal informado.

O projeto foi desenvolvido como parte de uma atividade acadêmica, com foco na prática de **entrada de dados, estruturas condicionais, operadores lógicos e validação de informações**.

## 🎯 Objetivo

O sistema solicita:

- 🏠 Tipo de imóvel: `casa`, `apartamento` ou `comercial`
- 💧 Consumo mensal de água em metros cúbicos (`m³`)

A partir dessas informações, o programa classifica o consumo de acordo com as regras definidas para a campanha de conscientização ambiental.

## 📋 Regras de classificação

| Condição | Resultado |
|---|---|
| Imóvel comercial | 🏢 Tarifa comercial aplicada – consulte o plano corporativo. |
| Apartamento com consumo menor que 10 m³ | 🌱 Consumo econômico – excelente controle de água! |
| Apartamento ou casa com consumo de até 25 m³ | ✅ Consumo moderado – dentro do padrão residencial. |
| Demais situações | ⚠️ Consumo excessivo – adote medidas de economia e verifique vazamentos. |

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-181717?logo=github&logoColor=white)

### Conceitos utilizados

- 🐍 Python
- 🔀 Estruturas condicionais (`if`, `elif`, `else`)
- 🔁 Estruturas de repetição (`while`)
- 🔤 Manipulação de strings com `casefold()`
- 🔢 Conversão de dados com `float()`
- ⚖️ Operadores lógicos (`and` e `or`)
- ✅ Validação de entradas
- 💬 Entrada e saída de dados pelo terminal

## 📁 Estrutura do projeto

```text
consumo-agua/
│
├── app.py
└── README.md
```

## ▶️ Como executar

### 1. Pré-requisito

É necessário ter o **Python 3** instalado no computador.

### 2. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 3. Acesse a pasta do projeto

```bash
cd consumo-agua
```

### 4. Execute o programa

```bash
python app.py
```

## 💻 Funcionamento

Ao executar o programa, o usuário deverá informar o tipo de imóvel e o consumo mensal de água.

Exemplo:

```text
=== Bem vindo ao classificador de consumo ===

Digite o tipo de imóvel:
(comercial, casa ou apartamento) apartamento

Digite seu consumo de água mensal (m³): 8.5

Consumo econômico – excelente controle de água!
```

O programa também realiza a validação das informações inseridas, solicitando uma nova entrada caso o tipo de imóvel não esteja entre as opções esperadas ou o consumo informado não seja positivo.

## 🌱 Proposta

Além da classificação do consumo, o projeto busca utilizar a programação como uma forma simples de **conscientização sobre o uso responsável da água**, incentivando a identificação de consumos elevados e possíveis vazamentos.

---

💧 **Pequenas atitudes ajudam a preservar um recurso essencial.**