import streamlit as st

# Lê o HTML local
with open("Treinamento 175.html", "r", encoding="utf-8") as f:
    html = f.read()

# Exibe o HTML inteiro
st.components.v1.html(html, height=800, scrolling=True)
