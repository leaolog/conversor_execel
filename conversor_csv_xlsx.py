import streamlit as st
import pandas as pd
import re
from io import StringIO, BytesIO
import time
import os
import base64

# --------------------------
# Função para converter imagem em Base64
# --------------------------
def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

# --------------------------
# Estilos CSS
# --------------------------
st.markdown("""
<style>
.stApp { background-color: #E0DBD7 !important; }
h1 { font-family: "Source Sans", sans-serif; font-size: 2.5rem; margin-bottom: 1rem; color: #422900; }
</style>
""", unsafe_allow_html=True)

# --------------------------
# Caminhos das imagens
# --------------------------
logo_path = "Assets/logo_excel.png"   # Logo do Excel
leao_logo_path = "Assets/logo_leao.png"  # Logo do Leão

# --------------------------
# Cabeçalho com logos (Base64)
# --------------------------
col1, col2 = st.columns([4,1])


with col1:
    if os.path.exists(logo_path):
        logo_base64 = get_base64_image(logo_path)
        st.markdown(f'<img src="data:image/png;base64,{logo_base64}" width="108">', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Logo do Excel não encontrado!")

with col2:
    if os.path.exists(leao_logo_path):
        leao_logo_base64 = get_base64_image(leao_logo_path)
        st.markdown(f'<img src="data:image/png;base64,{leao_logo_base64}" width="125">', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Logo do Leão não encontrado!")

# --------------------------
# Título da página
# Título da página
# --------------------------
st.title("Conversor de Arquivos CSV → Excel")
st.markdown("Arraste ou selecione um arquivo CSV para convertê-lo em Excel.")

# --------------------------
# Inicializa session_state
# --------------------------
if "excel_gerado" not in st.session_state:
    st.session_state.excel_gerado = False
if "df_excel" not in st.session_state:
    st.session_state.df_excel = None
if "sep" not in st.session_state:
    st.session_state.sep = ';'

# --------------------------
# Upload do arquivo CSV
# --------------------------
uploaded_file = st.file_uploader("📂 Escolha um arquivo CSV", type=["csv"])

if uploaded_file:
    if not st.session_state.excel_gerado:
        with st.spinner("🔄 Processando arquivo..."):
            texto = uploaded_file.getvalue().decode('utf-8', errors='ignore')

            # Corrige quebras de linha dentro de aspas
            texto_corrigido = re.sub(r'"\s*\n\s*"', ' ', texto)

            # Detectar separador
            sample = texto_corrigido[:4096]
            if ',' in sample and ';' not in sample:
                st.session_state.sep = ','
            else:
                st.session_state.sep = ';'
            if ',' in sample and ';' not in sample:
                st.session_state.sep = ','
            else:
                st.session_state.sep = ';'

            time.sleep(1)
            time.sleep(1)

            # Lê CSV com pandas
            df = pd.read_csv(
                StringIO(texto_corrigido),
                sep=st.session_state.sep,
                dtype=str,
                engine='python',
                quoting=3,
                on_bad_lines='skip'
            )

            # Limpeza
            df = df.dropna(how='all', axis=1)
            df.columns = df.columns.str.strip()
            df = df.dropna(how='all')
            df = df[df.count(axis=1) > 2]

            # Salva no session_state
            st.session_state.df_excel = df
            st.session_state.excel_gerado = True

    if st.session_state.excel_gerado:
        st.success("✅ Arquivo processado com sucesso!")

        # Preparar para download
        # Preparar para download
        output = BytesIO()
        st.session_state.df_excel.to_excel(output, index=False)
        output.seek(0)

        st.download_button(
            label="Baixar Excel",
            data=output,
            file_name="Arquivo_Convertido.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
