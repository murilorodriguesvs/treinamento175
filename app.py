import streamlit as st

st.set_page_config(
    layout="wide",   # remove a coluna estreita padrão
    page_title="Treinamento RCVM 175",
    page_icon="🌐"
)

# Remove margens/padding padrão com CSS injetado
st.markdown(
    """
    <style>
        .main .block-container {
            padding: 0rem 0rem 0rem 0rem;
            max-width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Lê o HTML local
with open("Treinamento 175.html", "r", encoding="utf-8") as f:
    html = f.read()

# Exibe o HTML inteiro
st.components.v1.html(html, height=800, scrolling=True)
