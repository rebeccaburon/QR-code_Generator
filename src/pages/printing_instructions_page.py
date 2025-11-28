import streamlit as st
from pathlib import Path
from utils.style import load_css


st.set_page_config(
        page_title = "printning_instructions",
        layout="wide",
    )

 #  -------------- Load CSS -------------
load_css()





# ----------- Page content -----------------------------

batch_id = st.session_state.get("selected_batch")

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<div class="ceros-logo"> CERoS</div>', unsafe_allow_html=True)

if batch_id:
      st.markdown(f"""
    <div class="status-box">
  <div class="status-title">The QR-Code is printed for batch id: <br> {batch_id}</div>
  <div class="status-subtitle">Instructions for labeling</div>

  <div class="status-text">
    When attaching the QR-label to a refrigerated batch, it is important to ensure that the sticker is placed on a clean and dry surface. 
    This prevents condensation from interfering with the scanner and helps maintain readability throughout storage. 
    The purpose of these guidelines is to support a consistent labeling workflow that aligns with standard handling procedures in the laboratory.
    <div><br></br></div>
    <div> <strong>Place the label:</strong></div>
    Place the label on the upper right part of the container, ensuring it is not covering any critical text (e.g., batch name, expiry date). 
    The QR code must remain fully visible when the container is stored in its normal position on the shelf.
    Peel off the QR label and position it carefully on the prepared area. 
    Press from the center outward to avoid air bubbles or folds. 
    Make sure all four corners are firmly attached so the label does not peel in cold conditions.
    Use the work mobile to scan the QR code.
  </div>
</div>
""", unsafe_allow_html=True)
if batch_id:
  if st.button("Show Scanning Instructions", key=f"exit-btn"):
    batch_id
    st.switch_page("pages/scanning_instructions_page.py")
      
else:
    st.warning("No batch selected yet.")
    if st.button("Go select QC-batch "):
        st.switch_page("pages/choose_batch_view.py")
    

st.markdown('<div class="exit-row">', unsafe_allow_html=True)





