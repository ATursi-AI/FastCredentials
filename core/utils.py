import os
import qrcode
import base64
from io import BytesIO
from datetime import timedelta
from django.conf import settings
from django.template.loader import render_to_string
from weasyprint import HTML

def generate_certificate_pdf(cert):
    """
    Generates a PDF certificate with 2026 Tiered Expiration Logic.
    
    TIERED STANDARDS:
    - Tier 3 (3 Years): Forklift, Alcohol, Food
    - Tier 2 (2 Years): First Aid, CPR, AED, BLS, Healthcare
    - Tier 1 (1 Year): Everything Else (Medical, OSHA, Compliance)
    """
    # 1. Setup Directory
    cert_dir = os.path.join(settings.MEDIA_ROOT, 'certificates')
    os.makedirs(cert_dir, exist_ok=True)

    # 2. Define PDF Path
    filename = f"certificate_{cert.cert_id}.pdf"
    file_path = os.path.join(cert_dir, filename)

    # 3. Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )
    qr.add_data(f"https://fastcredentials.com/verify/{cert.cert_id}")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # 4. Convert to Base64
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()
    qr_src = f"data:image/png;base64,{qr_base64}"

    # 5. CALCULATE EXPIRATION DATE
    title = cert.course.title.upper()
    
    # Tier 3: 3 Years (1095 Days)
    if any(x in title for x in ['FORKLIFT', 'ALCOHOL', 'FOOD']):
        expire_date = cert.issued_at + timedelta(days=1095)
    
    # Tier 2: 2 Years (730 Days)
    elif any(x in title for x in ['FIRST AID', 'CPR', 'AED', 'BLS', 'HEALTHCARE']):
        expire_date = cert.issued_at + timedelta(days=730)
    
    # Tier 1: 1 Year (365 Days)
    else:
        expire_date = cert.issued_at + timedelta(days=365)

    # 6. Render HTML
    context = {
        'cert': cert,
        'user': cert.user,
        'qr_code_path': qr_src,
        'expire_date': expire_date
    }
    html_string = render_to_string('certificate_pdf.html', context)

    # 7. Convert to PDF
    HTML(string=html_string, base_url=str(settings.BASE_DIR)).write_pdf(file_path)

    return f"certificates/{filename}"
