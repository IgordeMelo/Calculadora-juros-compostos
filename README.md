# 🧮 Calculadora de Juros Compostos

Uma calculadora web simples para simular a evolução de um investimento com juros compostos, considerando valor inicial e aportes mensais.

## 📋 Funcionalidades

- Cálculo de montante final com juros compostos
- Suporte a aportes mensais recorrentes
- Exibição do total investido e do total em juros ganhos
- Interface web simples e responsiva

## 🛠️ Tecnologias utilizadas

**Backend:**
- Python
- Flask
- Flask-CORS

**Frontend:**
- HTML5
- CSS3
- JavaScript (Fetch API)

## 🚀 Como rodar o projeto localmente

1. Clone este repositório
2. Instale as dependências do backend:
```bash
   pip install flask flask-cors
```
3. Rode a API:
```bash
   python app.py
```
4. Abra o arquivo `index.html` no navegador (recomenda-se usar a extensão Live Server do VS Code)

## 📐 Fórmula utilizada
M = P * (1 + i)^t + A * [((1 + i)^t - 1) / i]

Onde:
- `M` = montante final
- `P` = valor principal (inicial)
- `i` = taxa de juros mensal (decimal)
- `t` = número de meses
- `A` = valor do aporte mensal

## 🤖 Sobre este projeto

Este projeto foi desenvolvido como forma de aprendizado prático de Python, Flask e integração entre backend e frontend, com apoio do Claude (Anthropic) para orientação passo a passo durante o desenvolvimento.

## 📄 Licença

Este projeto é de uso livre para fins de estudo e aprendizado.
