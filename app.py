import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import instaloader

# Carrega as credenciais e inicializa o cliente do Google Sheets
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Instalikes").sheet1

# Função para adicionar lead à planilha
def adicionar_lead_ao_sheet(email, instagram):
    # Busca por registros existentes
    registros = sheet.get_all_records()
    for registro in registros:
        if registro['Email'] == email and registro['Instagram'] == instagram:
            return True  # Retorna True se encontrar um registro existente

    # Adiciona um novo registro
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([email, instagram, agora])
    return False  # Retorna False indicando que é um novo registro

# Função para obter o número de curtidas de uma postagem específica do Instagram
def obter_curtidas(shortcode):
    L = instaloader.Instaloader()
    postagem = instaloader.Post.from_shortcode(L.context, shortcode)
    return postagem.likes

# Interface do aplicativo Streamlit
st.title('Veja o Número de Curtidas em Posts do Instagram')

# Formulário de captura de leads
with st.form(key='form_lead'):
    email = st.text_input("Digite seu e-mail:")
    instagram_handle = st.text_input("Digite seu perfil do Instagram:")
    botao_enviar_lead = st.form_submit_button('Enviar')

# Verifica se o e-mail foi enviado
if botao_enviar_lead:
    existe = adicionar_lead_ao_sheet(email, instagram_handle)

    if not existe:
        st.success("Agora você pode acessar a ferramenta!")

    # Mostrar buscador de curtidas
    st.write("""
        Para encontrar o shortcode de uma postagem do Instagram, 
        acesse a postagem no navegador e copie a parte do URL após 'instagram.com/p/'. 
        Por exemplo, no URL 'https://www.instagram.com/p/XXXXX/', o shortcode é 'XXXXX'.
    """)
    shortcode = st.text_input('Digite o shortcode da postagem do Instagram:')
    if st.button('Obter Curtidas'):
        if shortcode:
            try:
                curtidas = obter_curtidas(shortcode)
                st.write(f'A postagem com o shortcode "{shortcode}" tem {curtidas} curtidas.')
            except Exception as e:
                st.error(f'Ocorreu um erro: {e}')

# Rodapé com créditos
st.markdown("""
---
**por [Mariana de Assis](https://www.instagram.com/marianateassis/)**

**desenvolvido por [Eduardo Caminha](https://www.instagram.com/ecaminhan/)**
""", unsafe_allow_html=True)