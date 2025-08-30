# 📊 Dashboard de Vendas - Supermercado  

## 📋 Sobre o Projeto  

Dashboard interativo desenvolvido em **Python**, utilizando **Streamlit**, **Plotly Express** e **Pandas**, com **estilização customizada em CSS**.  
Este projeto simula um **painel de gestão de vendas** usado em supermercados, permitindo **insights estratégicos** sobre desempenho, clientes e filiais.  

> 💡 Este repositório foi criado para demonstrar minhas habilidades em **análise de dados, visualização interativa, design responsivo e boas práticas de desenvolvimento**, competências essenciais para um futuro profissional de tecnologia.  

---

![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat&logo=streamlit)
![Python](https://img.shields.io/badge/Python-Data%20Analysis-3776AB?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=flat&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Viz-3F4F75?style=flat&logo=plotly)
![CSS3](https://img.shields.io/badge/CSS3-Custom%20Style-264DE4?style=flat&logo=css3)

---

## ✨ Destaques do Projeto  

- **📈 Visualizações interativas** com gráficos dinâmicos e responsivos  
- **🎨 Estilização avançada** via CSS externo (`assets/style.css`)  
- **🔍 Filtros inteligentes** por mês para análise segmentada  
- **⚡ KPIs estratégicos** (vendas, avaliações, cidade destaque)  
- **📱 Layout responsivo** para diferentes dispositivos  
- **📊 Insights de negócio reais** simulando relatórios corporativos  

---

## 🛠️ Tecnologias Utilizadas  

| Tecnologia     | Utilização |
|----------------|------------|
| **Streamlit**  | Criação da aplicação web interativa |
| **Pandas**     | Processamento e análise de dados |
| **Plotly**     | Visualizações interativas e responsivas |
| **CSS3**       | Estilização customizada e responsiva |
| **Python 3.12+** | Lógica e backend da aplicação |

---

## 📊 Funcionalidades Principais  

- **📅 Análise Temporal**: Vendas diárias com filtro por mês  
- **🏪 Performance por Filial**: Comparação de faturamento entre cidades  
- **🍗 Ranking de Produtos**: Produtos mais vendidos por receita  
- **💳 Métodos de Pagamento**: Distribuição percentual por forma de pagamento  
- **⭐ Satisfação do Cliente**: Avaliação média por cidade  
- **📊 KPIs em Tempo Real**: Total de vendas, média de avaliação e filial destaque  

---

## 🖥️ Design Responsivo & Acessibilidade  

O CSS do projeto foi desenvolvido com foco em **responsividade e experiência do usuário**:  
- Utilização de `clamp()` para tamanhos de fonte adaptáveis  
- Media Queries para melhor visualização em telas menores  
- Evita dependência de classes instáveis do Streamlit (seletores mais duradouros)  
- Fundo gradiente otimizado para evitar bugs em dispositivos móveis  
- Contraste de cores planejado para garantir legibilidade  

Essas práticas demonstram atenção a **detalhes de UX e acessibilidade**, diferenciais importantes em projetos profissionais.  

---

## 🚀 Como Executar Localmente  

### Pré-requisitos  
- Python 3.12 ou superior instalado  
- Git para clonar o repositório  
- Pip para instalar dependências  

### Passos  

```bash
# Clone o repositório
git clone https://github.com/SEU-USUARIO/supermarket-sales-dashboard.git
cd supermarket-sales-dashboard

# Crie e ative o ambiente virtual
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o dashboard
streamlit run dashboard.py
