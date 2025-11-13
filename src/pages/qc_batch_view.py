import streamlit as st
from pathlib import Path
from datetime import datetime
from utils.style import load_css

st.set_page_config(page_title="QC-Batch overview", layout="wide")

# ---------- Load shared CSS ----------

load_css()

# ---------- Demo data ----------
batch_id = st.session_state.get("selected_batch", "QB - 20251110 - 00348")
created_dt = datetime.now().strftime("%d.%m.%y %H:%M:%S")
started_dt = datetime.now().strftime("%d.%m.%y %H:%M:%S")

analyses = [
    {"name": "Analysis 1", "type": "Custom", "status": "running"},
    {"name": "Analysis 2", "type": "Custom", "status": "review"},
    {"name": "Analysis 3", "type": "Custom", "status": "running"},
    {"name": "Analysis 4", "type": "Custom", "status": "complete"},
    {"name": "Analysis 5", "type": "Custom", "status": "running"},
]


st.markdown('<div class="main-container">', unsafe_allow_html=True)


st.markdown('<div class="ceros-logo" style="text-align:center;">CERoS</div>', unsafe_allow_html=True)
st.markdown(
    '<h3 class="page-subtitle">Charactarization, Evalution & Reporting of Sub-visual particles</h3>',
    unsafe_allow_html=True,
)

# To-kolonne layout: venstre panel + højre liste med Demo data
left, right = st.columns([1, 2])

# --- Venstre info-panel
with left:
    st.markdown(f"""
    <div class="batch-sidepanel">
                <div class="panel-title">QC-Batch</div>
                <div class="panel-batchid">{batch_id}</div>
                <div class="panel-item">
                    <div class="label">Creation date:</div>
                    <div class="value">{created_dt}</div>
    </div>
    <div class="panel-item">
        <div class="label">Analysis started:</div>
        <div class="value">{started_dt}</div>
    </div>
    
    <div class="panel-section">Ready for Review</div>
    
    <div class="panel-section">Completed</div>
    </div>
    """, unsafe_allow_html=True)

# --- Højre: liste med analyser
with right:
    for a in analyses:
        # badge class afhænger af status
        badge_cls = {
            "running": "badge badge-running",
            "review": "badge badge-review",
            "complete": "badge badge-complete",
        }[a["status"]]

        st.markdown(f"""
        <div class="analysis-row">
            <div class="cell name">{a['name']}</div>
            <div class="cell type">{a['type']}</div>
            <div class="cell status">
                <span class="{badge_cls}">
                    {"Running……" if a["status"]=="running" else
                     "Ready for Review" if a["status"]=="review" else
                     "Complete"}
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Exit-knap centreret
st.markdown("""<div class="exit-row","exit-btn" ></div>""", unsafe_allow_html=True)
if st.button("Exit"):
    st.switch_page("pages/choose_batch_view.py")




st.markdown("</div>", unsafe_allow_html=True)