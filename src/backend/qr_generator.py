import qrcode
from pathlib import Path



BASE_APP_URL = ("http://localhost:8501")

def generate_qr_for_batch(batch_id: str) -> Path:
    qr_url = f"{BASE_APP_URL}/qc_batch_view?batch_id={batch_id}"

    #Save the image
    output_dir = Path("src") / "assets" / "qr_images"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = output_dir / f"{batch_id}.png"

    
    # Generat the QR code 
    qr = qrcode.QRCode()
    qr.add_data(qr_url)
    qr.make(fit=True) # chose smallest QR-code size
    
    # Generate the qr image
    img = qr.make_image()
    img.save(file_path)

    print(f"QR-Code generated for {batch_id}: {file_path}")
    print(f"Scans to URL: {qr_url}") #Test if the url path was correct.
    return file_path
