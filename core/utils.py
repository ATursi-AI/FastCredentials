import os
import qrcode
import base64
from io import BytesIO
from django.conf import settings
from django.template.loader import render_to_string
from weasyprint import HTML

def generate_certificate_pdf(cert):
    """
    Generates a PDF certificate.
    Embeds the QR code directly as a Base64 string to prevent missing image errors.
    """
    # 1. Setup Directory (Only for the PDF output)
    cert_dir = os.path.join(settings.MEDIA_ROOT, 'certificates')
    os.makedirs(cert_dir, exist_ok=True)

    # 2. Define PDF Path
    filename = f"certificate_{cert.cert_id}.pdf"
    file_path = os.path.join(cert_dir, filename)

    # 3. Generate QR Code (In Memory)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )
    qr.add_data(f"https://fastcredentials.com/verify/{cert.cert_id}")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # 4. Convert to Base64 String (The Fix)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()
    qr_src = f"data:image/png;base64,{qr_base64}"

    # 5. Render HTML
    context = {
        'cert': cert,
        'user': cert.user,
        'qr_code_path': qr_src  # Passing the image data directly
    }
    html_string = render_to_string('certificate_pdf.html', context)

    # 6. Convert to PDF
    HTML(string=html_string, base_url=str(settings.BASE_DIR)).write_pdf(file_path)

    return f"certificates/{filename}"
