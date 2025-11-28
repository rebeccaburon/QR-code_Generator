import streamlit as st
from pathlib import Path
from utils.style import load_css


st.set_page_config(
        page_title = "qr-code_is_generated",
        layout="wide",
    )

 #  -------------- Load CSS -------------
load_css()

batch_id = st.session_state.get("selected_batch", "Unknown batch")

qr_path = st.session_state.get("qr_image_path")

# ----------- Page content -----------------------------

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<div class="ceros-logo"> CERoS</div>', unsafe_allow_html=True)

if batch_id and qr_path:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="status-box">
            <div class="status-title">
                The QR-Code is generated. <br>Read more about what the code contains
            </div>
            <div class="status-text">
                The QR code contains essential batch metadata used to identify and track the sample throughout the laboratory workflow. 
                This includes the batch ID, creation date, assigned department, and a secure reference link that directs the system to the corresponding record in the internal database. 
                    The encoded information ensures that staff can quickly access status updates, analysis details, and handling instructions directly from the work phone
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image(str(qr_path), use_container_width=True)
        st.markdown(f"<div class='qr-label'>{batch_id}</div>", unsafe_allow_html=True)


    if st.button("Print QR-code"):
        st.switch_page("pages/printing_instructions_page.py")

else:
    st.warning("No batch selected yet.")
    if st.button("Go select QC-batch", key="exit-btn"):
        st.switch_page("pages/choose_batch_view.py")





st.markdown("</div>", unsafe_allow_html=True)









