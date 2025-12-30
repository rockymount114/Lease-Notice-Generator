# Flask Notice Generator v2.0

## Updates
- **Fixed KeyError**: All form keys are now handled via `.get()` or provided as hidden inputs to ensure the backend never crashes on missing data.
- **Digital Signature**: Integrated `SignaturePad.js` to capture mouse/touch signatures as Base64.
- **Live Preview**: Real-time synchronization between input fields and a CSS-styled "A4 paper" preview.
- **New Customizable Fields**: Added new customizable fields in `template_contents.md` for both "Notice to Pay Rent or Vacate" and "Affidavit of Service" sections to allow users to fill out more detailed information.
- **Enhanced User Interface**: Updated `templates/index.html` to include visible input fields for all customizable fields, converting previous hidden inputs, and improving dynamic live preview functionality for better user interaction.
- **State and County Fields**: Added dedicated input fields for 'State' and 'County' in `templates/index.html`, which are displayed dynamically in the preview and default to "_________" if left empty.
- **UI Reorganization**: Reorganized the layout of `templates/index.html` to closely match the visual structure of the provided document images, including both the form input fields and the live preview. This was achieved by grouping related fields and using a flexbox layout for the preview.
- **PDF Generation Fix**: Fixed an `AttributeError` and a subsequent `RuntimeError` during PDF download by reverting to the original, more compatible PDF generation method using `pdf.output(dest='S')` and encoding to 'latin-1'. This ensures compatibility with older `fpdf` library versions.
- **Two-Page PDF Generation**: Added logic to `app.py` to generate the second page of the PDF, the "AFFIDAVIT OF SERVICE", ensuring that the downloaded PDF contains both pages as shown in the preview.

## How to use
1. Run `pip install flask fpdf`.
2. Run `python app.py`.
3. Fill out the fields; watch the right-hand panel update.
4. Sign in the box and click **Download PDF**.
