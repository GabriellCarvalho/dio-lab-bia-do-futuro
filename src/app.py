import streamlit as st
from agente import perguntar

st.title("🤖 Gui - Seu Guia Financeiro")

if pergunta := st.chat_input("Faça uma pergunta sobre seus gastos ou orçamento:"):
    st.chat_message("user").write(pergunta)
    with st.spinner("Aguarde, estou analisando seus dados..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)