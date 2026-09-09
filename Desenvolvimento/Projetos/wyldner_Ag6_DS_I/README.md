# ⚡ Calculadora de Consumo Elétrico

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github)
![Energia](https://img.shields.io/badge/Energia-Consumo-yellow)

## 📋 Sobre o projeto

A **Calculadora de Consumo Elétrico** é um programa desenvolvido em Python que permite estimar o consumo mensal de energia elétrica de um aparelho.

O usuário informa o nome do aparelho, sua potência em watts e o tempo médio de uso diário. Com essas informações, o programa calcula uma estimativa do consumo mensal em kWh.

O programa também realiza uma estimativa do custo mensal da energia considerando o valor fixo de **R$ 0,75 por kWh**.

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* 💻 Git
* 🐙 GitHub

## 🧮 Fórmula utilizada

O consumo mensal é calculado através da fórmula:

```text
consumoMensal = (potencia × horasDia × 30) / 1000
```

Onde:

* **potência** = potência do aparelho em watts (W);
* **horasDia** = média de horas de uso por dia;
* **30** = quantidade estimada de dias no mês;
* **1000** = conversão de Wh para kWh.

O custo estimado é calculado através da fórmula:

```text
custoMensal = consumoMensal × 0,75
```

## ▶️ Como executar

É necessário ter o **Python 3** instalado no computador.

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre na pasta do projeto:

```bash
cd consumo-energia
```

Execute o programa:

```bash
python app.py
```

## 💡 Exemplo

```text
=== Calculadora de Consumo Elétrico ===

Digite o nome do aparelho: Geladeira
Digite a potência do aparelho em watts (W): 100
Digite o tempo médio de uso diário em horas: 15

--- Resultado ---
Aparelho: Geladeira
Consumo estimado: 45.00 kWh/mês
Custo estimado: R$ 33.75/mês
```

## 📁 Estrutura do projeto

```text
consumo-energia/
├── app.py
└── README.md
```

## ⚠️ Observação

O valor de **R$ 0,75 por kWh** é utilizado apenas como referência para o cálculo do custo estimado. O valor real da tarifa de energia pode variar.

---