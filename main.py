import streamlit as st

print('oi')

st.title("Título da página") ##título da página (texto que aparece em cima no começo)

st.subheader("Subheader") ## subheader da página(aparece abaixo do título)

st.header("Header") 

st.text("Página com interface utilizando streamlit") ## parágrafo

st.markdown("Método que possibilita marcação de alguma palavra, deixando-a em **negrito**") ## apenas um asterisco para itálico

st.markdown("# Exemplo") ## deixa o texto no tamanho do h1

st.markdown("## Exemplo") ## deixa o texto no tamanho do h2

st.markdown("### Exemplo") ## deixa o texto no tamanho do h3

st.markdown("> Exemplo") ## deixa com uma barra na frente

st.markdown("---") ## cria uma barra

st.markdown("[Google](https://www.google.com")