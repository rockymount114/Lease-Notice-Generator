import io
import base64
import tempfile
import os
from flask import Flask, render_template, request, send_file
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    data = request.form
    signature_data = data.get('signature_img')
    temp_image_path = None
    
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, 'NOTICE TO PAY RENT OR VACATE', 0, 1, 'C')
        pdf.ln(10)

        # Content
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, f"FROM: {data.get('landlord_name')}", ln=True)
        pdf.multi_cell(0, 8, f"ADDRESS: {data.get('landlord_address')}")
        pdf.cell(0, 8, f"DATE OF NOTICE: {data.get('notice_date')}", ln=True)
        pdf.ln(5)

        pdf.cell(0, 8, f"TO: {data.get('tenant_names')}", ln=True)
        pdf.cell(0, 8, f"PROPERTY ADDRESS: {data.get('property_address')}", ln=True)
        pdf.ln(10)

        # Body Text
        body = (f"PLEASE TAKE NOTICE that you are in default of the lease agreement entered into on "
                f"{data.get('lease_date')} for failure to pay rent. You owe the following for the period "
                f"of {data.get('rent_period')}:")
        pdf.multi_cell(0, 6, body)
        pdf.ln(5)

        # Totals
        rent_due = float(data.get('rent_due') or 0)
        late_fees = float(data.get('late_fees') or 0)
        other_fees = float(data.get('other_fees') or 0)
        total_due = rent_due + late_fees + other_fees

        pdf.cell(50, 8, f"Rent Due: ${rent_due:.2f}", ln=True)
        pdf.cell(50, 8, f"Late Fees: ${late_fees:.2f}", ln=True)
        pdf.cell(50, 8, f"Other Fees: ${other_fees:.2f}", ln=True)
        pdf.set_font("Arial", 'B', 11)
        pdf.cell(50, 8, f"Total Amount Due: ${total_due:.2f}", ln=True)
        pdf.ln(10)

        # Signature Logic
        if signature_data and "," in signature_data:
            header, encoded = signature_data.split(",", 1)
            image_type = header.split(';')[0].split('/')[1]
            img_data = base64.b64decode(encoded)

            with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{image_type}') as temp_image:
                temp_image.write(img_data)
                temp_image_path = temp_image.name
            
            pdf.cell(0, 8, "Signature:", ln=True)
            pdf.image(temp_image_path, x=pdf.get_x(), y=pdf.get_y(), w=40)
            pdf.ln(15)

        pdf.cell(0, 8, f"Print Name: {data.get('landlord_name')}", ln=True)
        pdf.cell(0, 8, f"Phone: {data.get('telephone')}", ln=True)

        # Second Page: Affidavit of Service
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, 'AFFIDAVIT OF SERVICE', 0, 1, 'C')
        pdf.ln(10)

        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, f"STATE OF {data.get('state', '_________')}", ln=True)
        pdf.cell(0, 8, f"{data.get('county', '_________')} COUNTY", ln=True)
        pdf.cell(0, 8, f"Date of Service: {data.get('date_of_service', '_________')}", ln=True)
        pdf.ln(10)

        pdf.multi_cell(0, 6, f"I, {data.get('landlord_name')}, the Landlord, hereby declare that the foregoing notice was properly delivered and served in the following manner:")
        pdf.ln(5)

        # Checkbox options (represented as text)
        pdf.cell(0, 8, "[ ] PERSONAL DELIVERY. This notice was delivered personally to the Tenant in possession of the Rental Premises.", ln=True)
        pdf.cell(0, 8, "[ ] OTHER PERSONAL DELIVERY. This notice was delivered personally to:", ln=True)
        pdf.set_x(pdf.get_x() + 10)
        pdf.multi_cell(0, 6, f"[ ] An authorized individual, named {data.get('authorized_individual_name', '_________')}, who was present at the Rental Premises upon an attempted delivery of this notice to the Tenant in possession of said Rental Premises.")
        pdf.set_x(pdf.get_x() + 10)
        pdf.multi_cell(0, 6, f"[ ] An authorized individual, named {data.get('authorized_individual_name', '_________')}, at the following location known to be the Tenant's place of work: _______________________________.")
        
        pdf.cell(0, 8, "[ ] POSTED AT THE RENTAL PREMISES. This notice was posted in a conspicuous location at the Rental Premises after an unsuccessful attempt to deliver the notice personally to the Tenant in possession of said Rental Premises.", ln=True)
        pdf.cell(0, 8, "[ ] REGISTERED / CERTIFIED MAIL. This notice was sent to the Tenant in possession of the Rental Premises via the following mail carrier:", ln=True)
        pdf.set_x(pdf.get_x() + 10)
        pdf.cell(0, 8, "[ ] USPS Registered Mail (mail receipt # __________________________)", ln=True)
        pdf.set_x(pdf.get_x() + 10)
        pdf.cell(0, 8, "[ ] USPS Certified Mail (mail receipt # __________________________)", ln=True)
        pdf.set_x(pdf.get_x() + 10)
        pdf.cell(0, 8, "[ ] FedEx (with signature confirmation requested)", ln=True)
        pdf.set_x(pdf.get_x() + 10)
        pdf.cell(0, 8, "[ ] UPS (with signature confirmation requested)", ln=True)
        pdf.set_x(pdf.get_x() + 10)
        pdf.cell(0, 8, "[ ] Other: ___________________________________________", ln=True)
        pdf.ln(10)

        pdf.set_font("Arial", 'B', 11)
        pdf.multi_cell(0, 6, "I declare under penalty of perjury that the foregoing statements are true and correct.")
        pdf.ln(10)

        # Second Signature
        if temp_image_path:
            pdf.cell(0, 8, "Signature:", ln=True)
            pdf.image(temp_image_path, x=pdf.get_x(), y=pdf.get_y(), w=40)
            pdf.ln(15)

        pdf.cell(0, 8, f"Print Name: {data.get('landlord_name')}", ln=True)
        
        output = io.BytesIO()
        pdf_out = pdf.output(dest='S').encode('latin-1')
        output.write(pdf_out)
        output.seek(0)

        return send_file(output, as_attachment=True, download_name="Signed_Notice.pdf", mimetype='application/pdf')
    finally:
        if temp_image_path and os.path.exists(temp_image_path):
            os.remove(temp_image_path)