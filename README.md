# Flask Lease Notice Generator

This Flask application provides a web-based interface to generate a two-page "Notice to Pay Rent or Vacate" and "Affidavit of Service" for North Carolina. It features a live preview that updates as you fill out the form, a digital signature pad, and generates a downloadable PDF of the final notice.

## Features

- **Dynamic Form**: A comprehensive form to capture all necessary details for the eviction notice, including landlord, tenant, rent, and service information.
- **Live Preview**: A real-time preview of the two-page notice that updates instantly as you type.
- **Digital Signature Pad**: A smooth, responsive signature pad (powered by `SignaturePad.js`) to capture a digital signature. The signature is embedded in the final PDF.
- **Two-Page PDF Generation**: Generates a complete, two-page PDF document containing both the "Notice to Pay Rent or Vacate" and the "Affidavit of Service".
- **Placeholder Support**: The live preview displays placeholder lines for empty fields and shows a default signature image before one is drawn.
- **Responsive UI**: A clean, two-column layout with the form on one side and the live preview on the other.

### Application Screenshots

PDF page 1 review

<img src="static/images/preview page1.png" alt="Preview Page 1" width="800"/>

PDF page 2 review

<img src="static/images/preview page2.png" alt="Preview Page 2" width="800"/>

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **PDF Generation**: `fpdf`
- **Digital Signature**: `SignaturePad.js`

## How to use

1. Install the required Python packages:
   ```bash
   pip install flask fpdf
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open your web browser and navigate to the address provided by Flask (usually `http://127.0.0.1:5000`).
4. Fill out the fields in the form; the preview on the right-hand panel will update as you type.
5. Sign in the signature box and click **Download PDF** to generate and download the final notice.

---

### Support This Project

[![Buy Me a Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=rockymount114&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff)](https://www.buymeacoffee.com/rockymount114)
