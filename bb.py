
import streamlit as st
import pandas as pd
from io import BytesIO
from PyPDF2 import PdfReader

def extrair_dados_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    texto_completo = ""
    for pagina in reader.pages:
        texto_completo += pagina.extract_text() or ""
    
    # Simulação de extração
    dados = {"Data": ["01/01/2024"], "Descrição": ["Exemplo"], "Valor": [100.0]}
    df = pd.DataFrame(dados)
    return df

def executar_extracao_bb():
    st.subheader("Extração - Banco do Brasil")
    uploaded_file = st.file_uploader("Faça o upload do extrato em PDF do Banco do Brasil", type=["pdf"])

    if uploaded_file is not None:
        st.success("Arquivo carregado com sucesso!")
        with st.spinner("Processando o PDF..."):
            df = extrair_dados_pdf(uploaded_file)

        if df is not None and not df.empty:
            st.success(f"{len(df)} transações extraídas.")
            st.dataframe(df)

            towrite = BytesIO()
            df.to_excel(towrite, index=False, engine='openpyxl')
            towrite.seek(0)

            st.download_button(
                label="📥 Baixar como Excel",
                data=towrite,
                file_name="extrato_bb_formatado.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.warning("Nenhum dado foi extraído do PDF.")
    else:
        st.info("Aguardando o upload do arquivo PDF.")
