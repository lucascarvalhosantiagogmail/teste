import streamlit as st
from bb import executar_extracao_bb
from sicoob import executar_extracao_sicoob

def dashboard():
    st.title("Extração de Dados Bancários")
    st.divider()

    with st.form("formulario_extracao"):
        opcao = st.radio("Escolha a extração:", ["Banco do Brasil", "Sicoob"])
        enviar = st.form_submit_button("Executar")

        if enviar:
            if opcao == "Banco do Brasil":
                executar_extracao_bb()
            elif opcao == "Sicoob":
                executar_extracao_sicoob()
