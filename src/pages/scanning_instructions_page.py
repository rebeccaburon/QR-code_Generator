import streamlit as st
from pathlib import Path
from utils.style import load_css


st.set_page_config(
        page_title = "scanning_instructions",
        layout="wide",
    )

 #  -------------- Load CSS -------------
load_css()


#------------- image path
IMG_PATH = Path(__file__).resolve().parents[1] / "assets" / "images" / "scan_qr_instructions.jpg"


#------ The selected batch - for now  ------------------
selected_batch = st.session_state.get("selected_batch", "QB-20130903-0037")


#----------- page content
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<div class="ceros-logo"> CERoS</div>', unsafe_allow_html=True)



col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"""
        <div class="status-box">
            <div class="status-title">
                How to scan the QR-Code and keep track on the Analysis’s
            </div>
            <div class="status-text">
                Contrary to popular belief, Lorem Ipsum is not simply random text.
                It has roots in a piece of classical Latin literature from 45 BC,
                making it over 2000 years old. Richard McClintock, a Latin professor
                at Hampden-Sydney College in Virginia, looked up one of the more obscure
                Latin words, consectetur, from a Lorem Ipsum passage, and going through
                the cites of the word in classical literature, discovered the undoubtable
                source.<br/><br/>
                Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of “de Finibus Bonorum
                et Malorum” (The Extremes of Good and Evil) by Cicero, written in 45 BC.
                This book is a treatise on the theory of ethics, very popular during the
                Renaissance.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
     st.image(str(IMG_PATH), use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)


if st.button("Show QR-code"):
    selected_batch
    st.switch_page("pages/show_qr-code_page.py")






