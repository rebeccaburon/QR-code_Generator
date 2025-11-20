import streamlit as st
from pathlib import Path
from utils.style import load_css
from backend.qr_generator import generate_qr_for_batch
from backend.db_connection import get_all_qcbatches


st.set_page_config(
        page_title = "Select Batch",
        layout="wide"
    )
#  -------------- Load CSS -------------
load_css()

# ----------- Page content -----------------------------

st.markdown('<div class= "main-container">', unsafe_allow_html= True)

st.markdown('<div class="ceros-logo"> CERoS</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="intro-box">
        When the samples are loaded and the raw images are captured
        with the MFI instrument, the CERoS QR Generator will start.<br/>
        In this demo, we choose a batch first.
    </div>
    """,
    unsafe_allow_html=True,
)


batch_ids = get_all_qcbatches()

for i, batch_id in enumerate(batch_ids):
      col_batch, col_btn = st.columns([4,1.5])

      with col_batch:
            st.markdown(
            f'<div class="batch-pill">{batch_id}</div>',
            unsafe_allow_html=True,
        )

      with col_btn:
            if st.button("Generate QR-Code", key=f"btn_{i}"):
                  st.session_state["selected_batch"] = batch_id
                  qr_path = generate_qr_for_batch(batch_id)
                  st.session_state["qr_image_path"] = str(qr_path)
                  st.session_state["qr_status"] = "Pending"


                  st.switch_page("pages/waiting_page.py")

st.markdown("</div>", unsafe_allow_html=True)
      
    