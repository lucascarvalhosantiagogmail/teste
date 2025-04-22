import streamlit as st
from dashboard import dashboard

st.set_page_config(page_title="Extração Bancária", layout="centered")

def main():
    dashboard()

if __name__ == "__main__":
    main()
