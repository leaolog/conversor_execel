import streamlit as st
import pandas as pd
import re
from io import StringIO, BytesIO
import time
import os
import base64
import zipfile

# --------------------------
# Função para converter imagem em Base64
# --------------------------
def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

# --------------------------
# Estilos CSS
# --------------------------
st.markdown(
    """
    <style>
    .stApp { background-color: #E0DBD7 !important; }
    h1 { font-family: "Source Sans", sans-serif; font-size: 2.5rem; margin-bottom: 1rem; color: #422900; }
    .css-1d391kg, .st-emotion-cache-3uj0rx, .st-emotion-cache-3qzj0x, .st-emotion-cache-1sct1q3 { max-width: 100%; overflow-wrap: break-word; }
    .st-emotion-cache-6rlrad, .st-emotion-cache-4mjat2 { vertical-align: middle; overflow: hidden; display: inline-flex; }
    .st-emotion-cache-5qfegl { display: inline-flex; justify-content: center; cursor: pointer; background-color: rgb(115 193 80 / 58%); border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 0.5rem; }
    .st-emotion-cache-5qfegl:hover { background-color: #2E7D32 !important; color: #fff !important; border-color: #1b5e20 !important; }
    .clear-btn {
        display: flex;
        justify-content: flex-end;
        margin-top: -20px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------
# Caminhos das imagens
# --------------------------
logo_path = "Assets/logo_excel.png"
leao_logo_path = "Assets/logo_leao.png"

# --------------------------
# Cabeçalho com logos (Base64)
# --------------------------
col1, col2 = st.columns([4, 1])

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
# --------------------------
st.title("Conversor de Arquivos CSV → Excel (ZIP ou Individual)")
st.markdown("Arraste ou selecione **um ou mais arquivos CSV** para convertê-los em **arquivos Excel (.xlsx)**.")

# --------------------------
# Inicializa estado
# --------------------------
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = None

# --------------------------
# Upload múltiplo de arquivos
# --------------------------
uploaded_files = st.file_uploader(
    "📂 Escolha um ou mais arquivos CSV",
    type=["csv"],
    accept_multiple_files=True,
    key="uploader"
)

# Atualiza o estado
if uploaded_files:
    st.session_state.uploaded_files = uploaded_files

# --------------------------
# Processamento dos arquivos
# --------------------------
if st.session_state.uploaded_files:
    uploaded_files = st.session_state.uploaded_files

    # --- Botão de limpar (só aparece depois do upload) ---
    clear_col, _ = st.columns([1, 4])
    with clear_col:
        clear_clicked = st.button("🧹 Limpar arquivos convertidos", key="clear_button")

    # Se clicado, limpa e recarrega
    if clear_clicked:
        st.session_state.uploaded_files = None
        st.experimental_rerun()

    # --- Processamento ---
    with st.spinner("🔄 Processando arquivos..."):
        time.sleep(0.5)

# --- Caso 1: Apenas um arquivo ---
if len(uploaded_files) == 1:
    uploaded_file = uploaded_files[0]

    texto = uploaded_file.getvalue().decode('utf-8', errors='ignore')
    texto_corrigido = re.sub(r'"\s*\n\s*"', ' ', texto)
    sample = texto_corrigido[:4096]
    sep = ',' if ',' in sample and ';' not in sample else ';'

    df = pd.read_csv(
        StringIO(texto_corrigido),
        sep=sep,
        dtype=str,
        engine='python',
        quoting=3,
        on_bad_lines='skip'
    )

    df = df.dropna(how='all', axis=1)
    df.columns = df.columns.str.strip()
    df = df.dropna(how='all')
    df = df[df.count(axis=1) > 2]

    output = BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)

    st.success("✅ Arquivo convertido com sucesso!")

    # Linha com os dois botões lado a lado (Baixar e Limpar)
    col_download, col_clear = st.columns([4, 1])
    with col_download:
        st.download_button(
            label="📥 Baixar Excel",
            data=output,
            file_name=f"{os.path.splitext(uploaded_file.name)[0]}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )

    with col_clear:
        if st.button("🧹 Limpar", use_container_width=True):
            st.session_state.uploaded_files = None
            st.experimental_rerun()

# --- Caso 2: Múltiplos arquivos ---
else:
    zip_buffer = BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for uploaded_file in uploaded_files:
            try:
                texto = uploaded_file.getvalue().decode('utf-8', errors='ignore')
                texto_corrigido = re.sub(r'"\s*\n\s*"', ' ', texto)
                sample = texto_corrigido[:4096]
                sep = ',' if ',' in sample and ';' not in sample else ';'

                df = pd.read_csv(
                    StringIO(texto_corrigido),
                    sep=sep,
                    dtype=str,
                    engine='python',
                    quoting=3,
                    on_bad_lines='skip'
                )

                df = df.dropna(how='all', axis=1)
                df.columns = df.columns.str.strip()
                df = df.dropna(how='all')
                df = df[df.count(axis=1) > 2]

                excel_buffer = BytesIO()
                df.to_excel(excel_buffer, index=False)
                excel_buffer.seek(0)

                file_name = os.path.splitext(uploaded_file.name)[0] + ".xlsx"
                zipf.writestr(file_name, excel_buffer.read())

            except Exception as e:
                st.error(f"⚠️ Erro ao processar {uploaded_file.name}: {e}")

    zip_buffer.seek(0)
    st.success("✅ Todos os arquivos foram convertidos e compactados com sucesso!")

    # Linha com botões lado a lado
    col_download, col_clear = st.columns([4, 1])
    with col_download:
        st.download_button(
            label="📦 Baixar ZIP com arquivos Excel",
            data=zip_buffer,
            file_name="Arquivos_Convertidos.zip",
            mime="application/zip",
            use_container_width=True
        )

    with col_clear:
        if st.button("🧹 Limpar", use_container_width=True):
            st.session_state.uploaded_files = None
            st.experimental_rerun()
