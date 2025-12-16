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


selected_batch = st.session_state.get("selected_batch")


# ----------- Page content -----------------------------

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<div class="ceros-logo"> CERoS</div>', unsafe_allow_html=True)



left, right = st.columns([2, 1])

with left:
    st.markdown(f"""
        <div class="status-box">
            <div class="status-title">
                How to scan the QR-Code and keep track on the Analysis’s
            </div>
            <div class="status-text">
                To scan the QR code, unlock the work phone and open the camera. 
                Hold the phone steady and position the camera so the entire QR code is visible within the guide frame on the screen. 
                The scanner will automatically detect the code once it is in focus, and a confirmation message will appear when the batch is successfully registered. 
                <div></div>
                If the scan does not trigger, adjust the distance slightly or tilt the phone to avoid 
                glare from the refrigerator lighting. After the scan is completed, the batch data should load automatically on the device
            </div>
        </div>
    """, unsafe_allow_html=True)

with right:
     st.image(str(IMG_PATH), use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)


if st.button("Show QR-code"):
    selected_batch
    st.switch_page("pages/show_qr-code_page.py")






