import io
import base64
from flask import Flask, render_template, request, send_file
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    data = request.form
    
    # Handle the signature image
    signature_data = data.get('signature_img')
    
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
    pdf.cell(50, 8, f"Rent Due: ${data.get('rent_due')}", ln=True)
    pdf.cell(50, 8, f"Late Fees: ${data.get('late_fees')}", ln=True)
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(50, 8, f"Total Amount Due: ${data.get('total_due')}", ln=True)
    pdf.ln(10)

    # Signature Logic
    if signature_data and "," in signature_data:
        # Remove header of base64 string
        header, encoded = signature_data.split(",", 1)
        img_data = base64.b64decode(encoded)
        img_buffer = io.BytesIO(img_data)
        
        pdf.cell(0, 8, "Signature:", ln=True)
        # Place signature image (adjust width/height as needed)
        pdf.image(img_buffer, x=pdf.get_x(), y=pdf.get_y(), w=40)
        pdf.ln(15)

    pdf.cell(0, 8, f"Print Name: {data.get('print_name')}", ln=True)
    pdf.cell(0, 8, f"Phone: {data.get('telephone')}", ln=True)

    output = io.BytesIO()
    pdf_out = pdf.output(dest='S').encode('latin-1')
    output.write(pdf_out)
    output.seek(0)

    return send_file(output, as_attachment=True, download_name="Signed_Notice.pdf")

if __name__ == '__main__':
    app.run(debug=True)