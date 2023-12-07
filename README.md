# Aplicativo Streamlit para Busca de Curtidas no Instagram

Este aplicativo Streamlit permite aos usuários obter o número de curtidas de postagens específicas no Instagram. Antes de acessar esta funcionalidade, os usuários devem inserir seu e-mail, que é capturado para fins de geração de leads via Mailchimp.

## Funcionalidades

- **Captura de Leads**: Insira o e-mail para ser adicionado à lista de leads do Mailchimp.
- **Busca de Curtidas no Instagram**: Após a inserção bem-sucedida do e-mail, o usuário pode obter o número de curtidas de uma postagem do Instagram usando seu shortcode.

## Como Usar

1. Clone o repositório do projeto.
2. Instale as dependências usando `pip install -r requirements.txt`.
3. Execute o aplicativo com `streamlit run seu_script.py`.

## Configuração

Você precisará configurar as seguintes variáveis com suas próprias credenciais do Mailchimp:

- `mailchimp_api_key`: Sua chave API do Mailchimp.
- `mailchimp_server`: Seu prefixo de servidor do Mailchimp.
- `mailchimp_audience_id`: O ID da audiência/lista do Mailchimp onde os leads serão armazenados.

## Requisitos

- Python 3
- Streamlit
- Mailchimp Marketing
- Instaloader

## Créditos

Desenvolvido por [Eduardo Caminha](caminhae@gmail.com).