from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT))

from src.backend.qr_generator import build_qr_url


def test_build_qr_url():
    batch_id = "test_QB-20250114-00427"
    url = build_qr_url(batch_id)

    assert "qc_batch_view" in url
    assert f"batch_id={batch_id}" in url

