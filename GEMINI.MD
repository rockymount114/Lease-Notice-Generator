# Flask Notice Generator v2.0

## Updates
- **Fixed KeyError**: All form keys are now handled via `.get()` or provided as hidden inputs to ensure the backend never crashes on missing data.
- **Digital Signature**: Integrated `SignaturePad.js` to capture mouse/touch signatures as Base64.
- **Live Preview**: Real-time synchronization between input fields and a CSS-styled "A4 paper" preview.
- **New Customizable Fields**: Added new customizable fields in `template_contents.md` for both "Notice to Pay Rent or Vacate" and "Affidavit of Service" sections to allow users to fill out more detailed information.
- **Enhanced User Interface**: Updated `templates/index.html` to include visible input fields for all customizable fields, converting previous hidden inputs, and improving dynamic live preview functionality for better user interaction.

## How to use
1. Run `pip install flask fpdf`.
2. Run `python app.py`.
3. Fill out the fields; watch the right-hand panel update.
4. Sign in the box and click **Download PDF**.
