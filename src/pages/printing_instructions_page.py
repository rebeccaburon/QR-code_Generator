import streamlit as st
from pathlib import Path
from utils.style import load_css


st.set_page_config(
        page_title = "printning_instructions",
        layout="wide",
    )

 #  -------------- Load CSS -------------
load_css()

#------ The selected batch - for now  ------------------
batch_id = st.session_state.get("selected_batch")


#----------- page content
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<div class="ceros-logo"> CERoS</div>', unsafe_allow_html=True)

if batch_id:
      st.markdown(f"""
    <div class="status-box">
  <div class="status-title">The QR-Code is printed for batch id: <br> {batch_id}</div>
  <div class="status-subtitle">Instructions for labeling</div>

  <div class="status-text">
    This is a long established fact that a reader will be distracted by the readable
    content of a page when looking at its layout. The point of using Lorem Ipsum is that
    it has a more-or-less normal distribution of letters, as opposed to using
    ‘Content here, content here’, making it look like readable English.<br/><br/>
    There are many variations of passages of Lorem Ipsum available, but the majority have
    suffered alteration. The standard chunk of Lorem Ipsum used since the 1500s is
    reproduced below for those interested.
            
  </div>
</div>
""", unsafe_allow_html=True)
if batch_id and st.button("Show Scanning Instructions", key=f"exit-btn"):
    batch_id
    st.switch_page("pages/scanning_instructions_page.py")
      
else:
    st.warning("No batch selected yet.")
    if st.button("Go select QC-batch "):
        st.switch_page("pages/choose_batch_view.py")
    

st.markdown('<div class="exit-row">', unsafe_allow_html=True)





