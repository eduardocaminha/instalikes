import streamlit as st
import mailchimp_marketing as Mailchimp
from mailchimp_marketing.api_client import ApiClientError
import instaloader
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do Mailchimp
mailchimp_api_key = os.environ.get('MAILCHIMP_API_KEY')
mailchimp_server = os.environ.get('MAILCHIMP_SERVER')
mailchimp_audience_id = os.environ.get('MAILCHIMP_AUDIENCE_ID')

# Inicializa o cliente do Mailchimp
mailchimp_client = Mailchimp.Client()
mailchimp_client.set_config({
    "api_key": mailchimp_api_key,
    "server": mailchimp_server
})

# Função para adicionar e-mail e perfil do Instagram à audiência do Mailchimp
def adicionar_email_e_perfil_ao_mailchimp(email, instagram_handle, audience_id):
    info_membro = {
        "email_address": email,
        "status": "subscribed",
        "merge_fields": {
            "INSTAGRAM": instagram_handle,  # Ajuste o nome do campo se necessário
        },
    }
    try:
        # Certifique-se de que audience_id está sendo passado corretamente
        resposta = mailchimp_client.lists.add_list_member(audience_id, info_membro)
        return resposta
    except ApiClientError as error:
        error_details = error.text if hasattr(error, 'text') else str(error)
        if 'Member Exists' in error_details:
            return {"success": True}
        else:
            return {"error": f"ApiClientError: {error_details}"}
    except Exception as e:
        return {"error": f"Exception: {str(e)}"}

# Função para obter o número de curtidas de uma postagem específica do Instagram
def obter_curtidas(shortcode):
    L = instaloader.Instaloader()
    postagem = instaloader.Post.from_shortcode(L.context, shortcode)
    return postagem.likes

# Interface do aplicativo Streamlit
st.title('Buscador de Curtidas de Postagens do Instagram')

# Formulário de captura de leads
with st.form(key='form_lead'):
    email = st.text_input("Digite seu e-mail:")
    instagram_handle = st.text_input("Digite seu perfil do Instagram:")
    botao_enviar_lead = st.form_submit_button('Enviar')

# Verifica se o e-mail foi enviado
if botao_enviar_lead:
    resultado = adicionar_email_e_perfil_ao_mailchimp(email, instagram_handle, mailchimp_audience_id)

    # Se não houver erro ou se o membro já existir, mostrar instruções e permitir acesso à funcionalidade de curtidas
    if 'success' in resultado or 'id' in resultado:
        st.success("Agora você pode usar a funcionalidade de curtidas.")
        
        # Instruções para encontrar o shortcode da postagem
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
    elif 'error' in resultado:
        st.error(f"Ocorreu um erro ao enviar os dados: {resultado['error']}")

# Créditos na barra lateral
st.sidebar.markdown("""
    **por Mariana de Assis**
    [![Mariana de Assis](URL_DA_FOTO_DO_PERFIL)](https://www.instagram.com/marianateassis/)
""", unsafe_allow_html=True)