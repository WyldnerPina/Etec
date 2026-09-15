# 🧮 Calculadora para Aplicação de Desconto

Um programa desenvolvido em **Python** para calcular automaticamente o desconto aplicado sobre o valor de uma compra e informar o valor final a ser pago.

O projeto foi desenvolvido como parte de uma atividade acadêmica, com foco na prática de **entrada de dados, estruturas condicionais, cálculos matemáticos e formatação de valores**.

## 🎯 Objetivo

O sistema solicita ao usuário o valor total da compra e aplica automaticamente uma porcentagem de desconto de acordo com o valor informado.

### 💰 Regras de desconto

| Valor da compra | Desconto |
|---|---:|
| Menor que R$ 200,00 | 5% |
| De R$ 200,00 a menor que R$ 300,00 | 10% |
| R$ 300,00 ou mais | 15% |

Após calcular o desconto, o programa apresenta:

- 💸 Valor do desconto aplicado
- 🛒 Valor total a ser pago

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-181717?logo=github&logoColor=white)

### Conceitos utilizados

- 🐍 Python
- 🔀 Estruturas condicionais (`if`, `elif`, `else`)
- 🔢 Conversão de dados com `float()`
- ➕ Operações matemáticas
- 💰 Cálculo de porcentagem
- 📝 `f-string` para formatação de valores
- 💵 Formatação de números com duas casas decimais
- ⌨️ Entrada e saída de dados pelo terminal

## 📁 Estrutura do projeto

```text
calculadora-desconto/
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
cd calculadora-desconto
```

### 4. Execute o programa

```bash
python app.py
```

## 💻 Funcionamento

Ao executar o programa, o usuário deverá informar o valor total da compra.

Exemplo:

```text
=== Calculadora para aplicação de desconto ===

Digite o valor total da compra: 250

Valor do desconto: R$25.00
Valor total a ser pago: R$225.00
```

Nesse exemplo, como o valor da compra está entre **R$ 200,00 e R$ 299,99**, é aplicado um desconto de **10%**.

## 🧠 Lógica utilizada

A porcentagem de desconto é determinada através de estruturas condicionais:

```text
Valor < R$ 200,00
        ↓
      5%

Valor < R$ 300,00
        ↓
      10%

Valor ≥ R$ 300,00
        ↓
      15%
```

Depois de determinar o desconto, o programa calcula o valor correspondente ao desconto e o subtrai do valor original da compra.

## ⚠️ Observações

Nesta versão, o programa considera que o usuário informará um valor numérico válido e positivo.

Não foram implementados tratamentos específicos para:

- Valores negativos;
- Valores que excedam a capacidade do tipo `float`;
- Entradas que não sejam numéricas.

Esses tratamentos podem ser adicionados posteriormente como melhorias no projeto.

---

💰 **Um cálculo simples, praticando conceitos fundamentais de programação.**