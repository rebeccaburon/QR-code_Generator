from pathlib import Path
import sys



PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.backend.db_connection import (
    get_connection,
    get_create_dt_and_by,
    get_analyses_for_batch,
    get_qcbatch_info,
)

BATCH_ID = "QB-20101311-0098"


def test_get_connection():
  
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            row = cur.fetchone()
            assert row is not None
    finally:
        conn.close()


def test_get_create_dt_and_by():
  
    row = get_create_dt_and_by(BATCH_ID)

    assert row is not None, "Expected a row for KNOWN_BATCH_ID"
    assert "create_dt" in row
    assert "create_by" in row


def test_get_analyses_for_batch():
   
    analyses = get_analyses_for_batch(BATCH_ID)

    assert isinstance(analyses, list)

    if analyses:
        first = analyses[0]
        assert "type" in first
        assert "status" in first


def test_get_qcbatch_info():
    """
    Integrationstest: henter vi info-rækken for et batch med de forventede felter?
    """
    info = get_qcbatch_info(BATCH_ID)

    if info is not None:
        for key in ["analysis_started", "analysis_stopped", "ready_for_review", "completed"]:
            assert key in info