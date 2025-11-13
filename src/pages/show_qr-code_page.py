import streamlit as st
from pathlib import Path
from utils.style import load_css


st.set_page_config(
        page_title = "show qr-code",
        layout="wide",
    )

 #  -------------- Load CSS -------------
load_css()

IMG_PATH = Path(__file__).resolve().parents[1] / "assets" / "images" / "qr-code.png"

#--- The selected batch - for now  ------------------
selected_batch = st.session_state.get("selected_batch", "QB-20130903-0037")

# ------- Page content -----------------------------
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<div class="ceros-logo"> CERoS</div>', unsafe_allow_html=True)

st.image(IMG_PATH, selected_batch)