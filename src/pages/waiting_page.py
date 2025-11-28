import streamlit as st
from pathlib import Path
from utils.style import load_css
import time

st.set_page_config(
        page_title = "Waiting_page",
        layout="wide",
    )

 #  -------------- Load CSS -------------
load_css()


batch_id = st.session_state.get("selected_batch", "Unknown batch") 


TOTAL_WAIT_SEC = 15

# Save the start time in session_state 
if "wait_start_time" not in st.session_state:
    st.session_state.wait_start_time = time.time()

count_down_timer = int(time.time() - st.session_state.wait_start_time)

remaining = TOTAL_WAIT_SEC - count_down_timer

# ----------- Page content -----------------------------
if batch_id:
    if remaining <= 0:
        st.switch_page("pages/qr-code_is_generated.py")
        st.stop()
    else:
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        
    
        st.markdown('<div class="ceros-logo"> CERoS</div>', unsafe_allow_html=True)
        st.markdown(f"""
                <div class="status-box">
                <div class="status-title">Generating&hellip;&hellip;&hellip;&hellip;</div>
                <div class="status-subtitle"> Batch: {batch_id}</div>
                <div class="status-text"> Please wait while the system prepares the QR-code for this batch. 
                The application is validating your input, creating the encoded link, and assembling the final image. 
                This process normally takes a few seconds. 
                Once completed, the QR-code will appear on screen and can be printed or saved for labeling
                <div class="status-subtitle"> Qr-Code is generetaed in: <b>{remaining}</b> sec. </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hourglass-wrapper">
     <div class="hourglass-circle">
        ⏳
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    time.sleep(1)
    st.rerun()
else:
    st.warning("No batch selected yet.")
    if st.button("Go select QC-batch", key="exit-btn"):
        st.switch_page("pages/choose_batch_view.py")

