# Aplicativo Streamlit: Buscador de Curtidas de Postagens do Instagram

Este aplicativo Streamlit permite aos usuários obter o número de curtidas de postagens específicas no Instagram. Além disso, ele integra um sistema de captura de leads, armazenando os dados de contato dos usuários em uma planilha do Google Sheets.

## Funcionalidades

- **Captura de Leads**: O aplicativo coleta endereços de e-mail e perfis do Instagram, armazenando-os em uma planilha do Google Sheets junto com a data e hora da submissão.
- **Busca de Curtidas no Instagram**: Após fornecer suas informações, os usuários podem buscar o número de curtidas de qualquer postagem específica no Instagram, utilizando seu shortcode.

## Como Usar

1. Clone o repositório do projeto.
2. Instale as dependências usando `pip install -r requirements.txt`.
3. Certifique-se de ter um arquivo `credentials.json` válido na raiz do projeto para autenticação com o Google Sheets.
4. Execute o aplicativo com `streamlit run app.py`.

## Configuração

- **Google Sheets**: O aplicativo requer acesso a uma planilha do Google Sheets nomeada "Instalikes" com as colunas "Email", "Instagram" e "Time".
- **Autenticação**: Um arquivo `credentials.json` de uma conta de serviço do Google é necessário para autenticar e interagir com o Google Sheets.

## Requisitos

- Python 3
- Streamlit
- gspread
- oauth2client
- instaloader

## Créditos

- **por [Mariana de Assis](https://www.instagram.com/marianateassis/)**

- **desenvolvido por [Eduardo Caminha](https://www.instagram.com/ecaminhan/)**
