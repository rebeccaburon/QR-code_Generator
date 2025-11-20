import streamlit as st
from pathlib import Path
from datetime import datetime
from utils.style import load_css
from backend.db_connection import get_create_dt, get_analyses_for_batch

st.set_page_config(
    page_title="QC-Batch overview", 
    layout="wide"
    )

# ---------- Load shared CSS ----------

load_css()


batch_id = st.session_state.get("selected_batch", "Unknown batch")
if batch_id == "Unknown batch":
    st.error("No batch selected yet.")
    if st.button("Go select QC-batch", key="exit-btn"):
        st.switch_page("pages/choose_batch_view.py")
    st.stop()


created_dt_db = get_create_dt(batch_id)

if created_dt_db:
    created_dt = created_dt_db.strftime("%d-%m-%y")
else:
    created_dt = "Unknown"


analyses = get_analyses_for_batch (batch_id)


# ---------Layout ----------

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<div class="ceros-logo" style="text-align:center;">CERoS</div>', unsafe_allow_html=True)
st.markdown(
    '<h3 class="page-subtitle">Charactarization, Evalution & Reporting of Sub-visual particles</h3>',
    unsafe_allow_html=True,
)

left, right = st.columns([1, 2])

with left:
    st.markdown(f"""
    <div class="batch-sidepanel">
                <div class="panel-title">QC-Batch</div>
                <div class="panel-batchid">{batch_id}</div>
                <div class="panel-item">
                    <div class="label">Creation date:</div>
                    <div class="value">{created_dt}</div>
    </div>
    
    <div class="panel-section">Ready for Review</div>
    
    <div class="panel-section">Completed</div>
    </div>
    """, unsafe_allow_html=True)


with right:
    if not analyses:
        st.info("No analyses found for this batch.")
    else:
        for a in analyses:
            status = a.get("status", "complete")
            badge_cls = {
                "running": "badge badge-running",
                "review": "badge badge-review",
                "complete": "badge badge-complete",
            }.get(status, "badge badge-complete")

            st.markdown(
                f"""
                <div class="analysis-row">
                    <div class="cell type">{a.get('type', 'Unknown')}</div>
                    <div class="cell status">
                        <span class="{badge_cls}">
                            {"Running……" if status == "running"
                              else "Ready for Review" if status == "review"
                              else "Complete"}
                        </span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


    # Exit-knap centreret
st.markdown("""<div class="exit-row","exit-btn" ></div>""", unsafe_allow_html=True)
if st.button("Exit"):
    st.switch_page("pages/choose_batch_view.py")




st.markdown("</div>", unsafe_allow_html=True)