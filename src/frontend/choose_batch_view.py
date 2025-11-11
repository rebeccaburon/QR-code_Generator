import streamlit as st
from pathlib import Path


st.set_page_config(
        page_title = "Select Batch",
        layout="wide",
    )
    #  -------------- Load CSS -------------
def get_css_file(file_name):
        with open (file_name) as file:
            st.markdown (f"<style> {file.read()}</style>", unsafe_allow_html=True)

file_path = Path(__file__).parent / "styles.css"

get_css_file(file_path)

    # -------- Page content ------------------

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

# Demo-batches (Skal hentes fra database)
batch_ids = [
    "QB-20101311-0098",
    "QB-20110312-0023",
    "QB-20130903-0037",
    "QB-20231507-0061",
]

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
                  st.session_state["qr_status"] = "Pending"

if "selected_batch" in st.session_state:
    st.success( #Når knappet trykkes på, skal den føre over til en anden side
        f"Selected batch: {st.session_state['selected_batch']} "
        f"— ready to generate QR-code."
    )

st.markdown("</div>", unsafe_allow_html=True)
      
    