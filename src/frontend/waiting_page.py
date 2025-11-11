import streamlit as st
from pathlib import Path


st.set_page_config(
        page_title = "Waiting_page",
        layout="wide",
    )

 #  -------------- Load CSS -------------
def get_css_file(file_name):
        with open (file_name) as file:
            st.markdown (f"<style> {file.read()}</style>", unsafe_allow_html=True)

file_path = Path(__file__).parent / "styles.css"

get_css_file(file_path)


#--- The selected batch - for now  ------------------
selected_batch = st.session_state.get("selected_batch", "QB-20130903-0037")

# ------- Page content -----------------------------
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<div class="ceros-logo"> CERoS</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="status-box">
    <div class="status-title">Generating&hellip;&hellip;&hellip;&hellip;</div>
    <div class="status-subtitle">
        Information about batch: {selected_batch}
    </div>
    <div class="status-text">
        This is a long established fact that a reader will be distracted
        by the readable content of a page when looking at its layout.
        The point of using Lorem Ipsum is that it has a more-or-less
        normal distribution of letters, as opposed to using
        'Content here, content here', making it look like readable English.
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