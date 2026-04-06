# AquaCli 💧
**Versão:** 1.0.0

## 🎯 O Problema
Muitas pessoas, especialmente idosos e trabalhadores com rotinas intensas, esquecem de beber água durante o dia. A desidratação crônica pode causar dores de cabeça, fadiga e problemas renais graves. 

## 💡 A Solução
O **AquaCli** é uma aplicação simples via interface de linha de comando (CLI) que permite registrar o consumo de água e verificar se a meta diária (2000ml) foi atingida. Ele é rápido, não consome recursos do computador e serve como um diário de hidratação.

## 🛠 Tecnologias Utilizadas
- **Linguagem:** Python 3.10+
- **Testes:** pytest
- **Linting:** flake8
- **CI/CD:** GitHub Actions

## 🚀 Como instalar e executar
1. Clone este repositório.
2. Instale as dependências:
   `pip install -r requirements.txt`
3. Execute o programa adicionando água:
   `python app.py --add 500`

## 🧪 Como rodar os testes e linting
Para garantir a qualidade do código, utilize os comandos abaixo:
- **Linting:** `flake8 app.py test_app.py`
- **Testes:** `pytest test_app.py`
