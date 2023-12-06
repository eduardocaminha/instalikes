import streamlit as st
import instaloader

# Função para obter o número de curtidas de uma postagem específica do Instagram
def obter_curtidas(shortcode):
    L = instaloader.Instaloader()
    postagem = instaloader.Post.from_shortcode(L.context, shortcode)
    return postagem.likes

# Interface do aplicativo Streamlit
st.title('Buscador de Curtidas de Postagens do Instagram')

# Instruções para o usuário
st.write("""
    Para encontrar o shortcode de uma postagem do Instagram, 
    acesse a postagem no navegador e copie a parte do URL após 'instagram.com/p/'. 
    Por exemplo, no URL 'https://www.instagram.com/p/XXXXX/', o shortcode é 'XXXXX'.
""")

# Entrada do usuário para o shortcode da postagem do Instagram
shortcode = st.text_input('Digite o shortcode da postagem do Instagram:')

# Botão para buscar as curtidas
if st.button('Obter Curtidas'):
    if shortcode:
        try:
            curtidas = obter_curtidas(shortcode)
            st.success(f'A postagem com o shortcode "{shortcode}" possui {curtidas} curtidas.')
        except Exception as e:
            st.error(f'Ocorreu um erro: {e}')
    else:
        st.error('Por favor, digite um shortcode.')

# Créditos na barra lateral
st.sidebar.markdown("""
    **por Mariana de Assis**
    [[Mariana de Assis]](https://www.instagram.com/marianateassis/)
""", unsafe_allow_html=True)
