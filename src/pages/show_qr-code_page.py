import streamlit as st
from pathlib import Path
from utils.style import load_css


st.set_page_config(
        page_title = "show qr-code",
        layout="wide",
    )

 #  -------------- Load CSS -------------
load_css()


batch_id = st.session_state.get("selected_batch", "Unknown batch")

qr_path = st.session_state.get("qr_image_path")

# ------- Page content -----------------------------

if qr_path and batch_id:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<div class="ceros-logo"> CERoS</div>', unsafe_allow_html=True)
    st.image(qr_path, batch_id)

else:
    st.warning("There is no QR-code or batch id. Go to page: **Chose Batch** ")
    if st.button("Chose a batch", key=f"exit-btn"):
        st.switch_page("pages/choose_batch_view.py")
