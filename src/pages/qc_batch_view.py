import streamlit as st
from pathlib import Path
from datetime import datetime
from utils.style import load_css
from backend.db_connection import get_create_dt_and_by, get_analyses_for_batch, get_qcbatch_info

st.set_page_config(
    page_title="QC-Batch overview", 
    layout="wide"
    )

# ---------- Load shared CSS ----------

load_css()
# 1. Try to read from URL: ?batch_id=..
params = st.experimental_get_query_params()
batch_id_from_url = params.get("batch_id", [None])[0]

if batch_id_from_url:
    batch_id = batch_id_from_url
else:
    # 2. Fallback to session_state (for normal navigation inside the app)
    batch_id = st.session_state.get("selected_batch","Unknown batch" )


if batch_id == "Unknown batch":
    st.error("No batch selected yet.")
    if st.button("Go select QC-batch", key="exit-btn"):
        st.switch_page("pages/choose_batch_view.py")
    st.stop()


created_row = get_create_dt_and_by(batch_id)

if created_row:
    created_dt = created_row["create_dt"].strftime("%d-%m-%y")
    created_by = created_row["create_by"]
else:
    created_dt = "Unknown"
    created_by = "Unknown"





analyses = get_analyses_for_batch (batch_id)
info = get_qcbatch_info(batch_id) or {}

ready_for_review = info.get("ready_for_review")
completed = info.get("completed")

ready_review_label = "Yes" if ready_for_review else "No"
completed_label = "Yes" if completed else "No"

analysis_started = info.get("analysis_started")
analysis_stopped = info.get("analysis_stopped")

started_label = analysis_started or "Unknown"
stopped_label = analysis_stopped or "Unknown"
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
        <div class="panel-section">
            Analysis started: <b>{started_label}</b>
        </div>
        <div class="panel-section">
            Analysis stopped: <b>{stopped_label}</b>
        </div>
        <div class="panel-section">
            Ready for Review: <b>{ready_review_label}</b>
        </div>
        <div class="panel-section">
            Completed: <b>{completed_label}</b>
        </div>
    </div>
    """, unsafe_allow_html=True)



with right:
    if not analyses:
        st.info("No analyses found for this batch.")
    else:
        for a in analyses:
            raw_status = a.get("status", "")
            status = raw_status.strip().lower()  

            if status == "running":
                badge_cls = "badge badge-running"
                label = "Running……"
            elif status == "review":
                badge_cls = "badge badge-review"
                label = "Ready for Review"
            elif status == "complete":
                badge_cls = "badge badge-complete"
                label = "Complete"
            else:
                badge_cls = "badge badge-complete"
                label = raw_status

            st.markdown(
                f"""
                <div class="analysis-row">
                    <div class="cell type">{a.get('type', 'Unknown')}</div>
                    <div class="cell creator">{created_by}</div>
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