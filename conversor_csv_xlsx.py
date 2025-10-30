import streamlit as st
import pandas as pd
import re
from io import StringIO, BytesIO
import time
<<<<<<< HEAD
<<<<<<< HEAD
from PIL import Image
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
st.markdown(
    """
    <style>
    /* Cor de fundo do app */
    .stApp { background-color: #E0DBD7 !important; }

    h1 { font-family: "Source Sans", sans-serif; font-size: 2.5rem; margin-bottom: 1rem; color: #422900; }

    .css-1d391kg, .st-emotion-cache-3uj0rx, .st-emotion-cache-3qzj0x, 
    .st-emotion-cache-ycmcfb, .st-emotion-cache-1sct1q3, .st-emotion-cache-6rlrad,
    .st-emotion-cache-5qfegl, .st-emotion-cache-4mjat2, .st-emotion-cache-p9nomz,
    .st-emotion-cache-1rpn56r { max-width: 100%; overflow-wrap: break-word; }

    .st-emotion-cache-5qfegl:hover { background-color: #2E7D32 !important; color: #fff !important; border-color: #1b5e20 !important; }
    </style>
    """,
    unsafe_allow_html=True
)
=======
=======
>>>>>>> 5b5433e (ajuste_logos)
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
<<<<<<< HEAD
st.markdown("""
<style>
.stApp { background-color: #E0DBD7 !important; }
h1 { font-family: "Source Sans", sans-serif; font-size: 2.5rem; margin-bottom: 1rem; color: #422900; }
</style>
""", unsafe_allow_html=True)
<<<<<<< HEAD
>>>>>>> 18800bd (ajustes_pastas)
st.markdown("""
<style>
.stApp { background-color: #E0DBD7 !important; }
h1 { font-family: "Source Sans", sans-serif; font-size: 2.5rem; margin-bottom: 1rem; color: #422900; }
</style>
""", unsafe_allow_html=True)
=======
>>>>>>> 5b5433e (ajuste_logos)
=======
st.markdown(
    """
    <style>

    /* Cor de fundo do app */
    .stApp {
        background-color: #E0DBD7 !important; /* ajuste para a cor desejada */
    }

    /* Estilo do título h1 */
    h1 {
        font-family: "Source Sans", sans-serif;
        font-size: 2.5rem;
        margin-bottom: 1rem;
        color: #422900;  /* cor do título */
    }

    /* Ajuste de quebra de linha e overflow para textos longos */
    .css-1d391kg {  /* opcional, para textos dentro de Markdown */
        max-width: 100%;
        overflow-wrap: break-word;
    }

    .st-emotion-cache-3uj0rx {
    font-family: "Source Sans", sans-serif;
    font-size: 1rem;
    margin-bottom: -1rem;
    color: #3D2900;
    max-width: 100%;
    overflow-wrap: break-word;
    }

    .st-emotion-cache-3qzj0x {
        font-family: "Source Sans", sans-serif;
        font-size: 0.875rem;
        color: rgb(142 92 0);
        max-width: 100%;
        overflow-wrap: break-word;
    }

    
    .st-emotion-cache-1r4qj8v {
    position: absolute;
    background: rgb(255, 255, 255);
    color: rgb(145 103 0);
    inset: 0px;
    color-scheme: light;
    overflow: hidden;
    }


    .st-emotion-cache-ycmcfb {
        color: rgb(82 56 1);
    }    

   .st-emotion-cache-1sct1q3 {
    font-size: 0.875rem;
    color: rgb(126 85 8 / 94%);
    display: block;
    text-overflow: ellipsis;
    overflow: hidden;
    white-space: nowrap;
    max-width: 100%;
    } 

    .st-emotion-cache-6rlrad {
    vertical-align: middle;
    overflow: hidden;
    color: rgb(170 138 11 / 62%);
    fill: currentcolor;
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    font-size: 2.3rem;
    width: 2.3rem;
    height: 2.3rem;
    flex-shrink: 0;
    }

    .st-emotion-cache-5qfegl {
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 2.5rem;
    margin: 0px;
    line-height: 1.6;
    text-transform: none;
    font-size: inherit;
    font-family: inherit;
    color: inherit;
    width: 100%;
    cursor: pointer;
    user-select: none;
    background-color: rgb(115 193 80 / 58%);
    border: 1px solid rgba(49, 51, 63, 0.2);
    }

    .st-emotion-cache-4mjat2 {
        vertical-align: middle;
        overflow: hidden;
        color: rgb(173 118 35 / 78%);
        fill: currentcolor;
        display: inline-flex;
        -webkit-box-align: center;
        align-items: center;
        font-size: 1.8rem;
        width: 1.8rem;
        height: 1.8rem;
        flex-shrink: 0;
    }   

    /* Hover: fundo verde escuro */
    .st-emotion-cache-5qfegl:hover {
        background-color: #2E7D32 !important; /* verde escuro */
        color: #fff !important; /* texto branco pra contraste */
        border-color: #1b5e20 !important; /* borda um pouco mais escura */
    }
    .st-emotion-cache-p9nomz {
        margin-right: 0.5rem;
        margin-bottom: 0.25rem;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        color: rgb(103 54 3);
    }

    .st-emotion-cache-1rpn56r {
    color: rgb(93 56 0 / 84%);
    font-size: 0.875rem;
    line-height: 1.25;
}

    </style>
    """,
    unsafe_allow_html=True
)

>>>>>>> a830919 (ajuste_markdow)

# --------------------------
# Caminhos das imagens
# --------------------------
<<<<<<< HEAD
<<<<<<< HEAD
base_path = os.path.dirname(__file__)  # pasta do script
logo_excel_path = os.path.join(base_path, "..", "Assets", "logo_excel.png")
logo_leao_path = os.path.join(base_path, "..", "Assets", "logo_leao.png")
logo_path = "Assets/logo_excel.png"   # Logo do Excel
leao_logo_path = "Assets/logo_leao.png"  # Logo do Leão

# --------------------------
# Cabeçalho com logos
=======
logo_path = os.path.join("Assets", "logo_excel.png")
leao_logo_path = os.path.join("Assets", "logo_leao.png")

# --------------------------
# Cabeçalho com logos (Base64)
>>>>>>> 18800bd (ajustes_pastas)
# Cabeçalho com logos (Base64)
=======
logo_path = "Assets/logo_excel.png"   # Logo do Excel
leao_logo_path = "Assets/logo_leao.png"  # Logo do Leão

# --------------------------
# Cabeçalho com logos (Base64)
>>>>>>> 5b5433e (ajuste_logos)
# --------------------------
col1, col2 = st.columns([4,1])


with col1:
    if os.path.exists(logo_path):
        logo_base64 = get_base64_image(logo_path)
        st.markdown(f'<img src="data:image/png;base64,{logo_base64}" width="108">', unsafe_allow_html=True)
<<<<<<< HEAD
>>>>>>> 18800bd (ajustes_pastas)
    if os.path.exists(logo_path):
        logo_base64 = get_base64_image(logo_path)
        st.markdown(f'<img src="data:image/png;base64,{logo_base64}" width="108">', unsafe_allow_html=True)
=======
>>>>>>> 5b5433e (ajuste_logos)
    else:
        st.warning("⚠️ Logo do Excel não encontrado!")

with col2:
    if os.path.exists(leao_logo_path):
        leao_logo_base64 = get_base64_image(leao_logo_path)
        st.markdown(f'<img src="data:image/png;base64,{leao_logo_base64}" width="125">', unsafe_allow_html=True)
<<<<<<< HEAD
>>>>>>> 18800bd (ajustes_pastas)
    if os.path.exists(leao_logo_path):
        leao_logo_base64 = get_base64_image(leao_logo_path)
        st.markdown(f'<img src="data:image/png;base64,{leao_logo_base64}" width="125">', unsafe_allow_html=True)
=======
>>>>>>> 5b5433e (ajuste_logos)
    else:
        st.warning("⚠️ Logo do Leão não encontrado!")

# --------------------------
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

<<<<<<< HEAD
            # Detectar separador de forma simples
=======
            texto_corrigido = re.sub(r'"\s*\n\s*"', ' ', texto)

            # Detecta separador
>>>>>>> 18800bd (ajustes_pastas)
=======
>>>>>>> 5b5433e (ajuste_logos)
            # Detectar separador
            sample = texto_corrigido[:4096]
            if ',' in sample and ';' not in sample:
                st.session_state.sep = ','
            else:
                st.session_state.sep = ';'

            time.sleep(1)

<<<<<<< HEAD
<<<<<<< HEAD
            # Lê CSV
=======
>>>>>>> 18800bd (ajustes_pastas)
=======
>>>>>>> 5b5433e (ajuste_logos)
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
        output = BytesIO()
        st.session_state.df_excel.to_excel(output, index=False)
        output.seek(0)

        st.download_button(
            label="Baixar Excel",
            data=output,
            file_name="Arquivo_Convertido.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
