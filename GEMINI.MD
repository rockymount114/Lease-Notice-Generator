# Flask Notice Generator v2.0

## Updates
- **Fixed KeyError**: All form keys are now handled via `.get()` or provided as hidden inputs to ensure the backend never crashes on missing data.
- **Digital Signature**: Integrated `SignaturePad.js` to capture mouse/touch signatures as Base64.
- **Live Preview**: Real-time synchronization between input fields and a CSS-styled "A4 paper" preview.
- **New Customizable Fields**: Added new customizable fields in `template_contents.md` for both "Notice to Pay Rent or Vacate" and "Affidavit of Service" sections to allow users to fill out more detailed information.
- **Enhanced User Interface**: Updated `templates/index.html` to include visible input fields for all customizable fields, converting previous hidden inputs, and improving dynamic live preview functionality for better user interaction.
- **State and County Fields**: Added dedicated input fields for 'State' and 'County' in `templates/index.html`, which are displayed dynamically in the preview and default to "_________" if left empty.
- **UI Reorganization**: Reorganized the layout of `templates/index.html` to closely match the visual structure of the provided document images, including both the form input fields and the live preview. This was achieved by grouping related fields and using a flexbox layout for the preview.
- **Form Field Optimization**: Further optimized `templates/index.html` by:
    - Grouping "Rent Due", "Late Fees", and "Other Fees" into a single row.
    - Grouping "State", "County", "Date of Service", and "Authorized Individual Name" into a single row.
    - Reducing the space allocated for the "Authorized Individual Name" field.
- **PDF Generation Fix**: Resolved a series of PDF generation issues through iterative fixes:
    - Addressed a recurring `AttributeError: '_io.BytesIO' object has no attribute 'rfind'` during file sending by ensuring the `mimetype='application/pdf'` parameter was present in the `send_file` function.
    - Corrected a `RuntimeError` from an incorrect fpdf output destination by using the compatible `dest='S'` method.
    - Finally fixed the `AttributeError: '_io.BytesIO' object has no attribute 'startswith'` when adding the signature image. This was resolved by implementing a robust temporary file workaround, as the installed `fpdf` version did not support in-memory `BytesIO` objects for images. The image is now saved to a temporary file on disk, its path is passed to `pdf.image()`, and the file is safely deleted after the PDF is generated.
- **Two-Page PDF Generation**: Added logic to `app.py` to generate the second page of the PDF, the "AFFIDAVIT OF SERVICE", ensuring that the downloaded PDF contains both pages as shown in the preview.
- **PDF Data and Submission Fixes**: 
    - Corrected the "Total Amount Due" by recalculating it on the backend.
    - Ensured "Print Name" is correctly displayed on the PDF by using the landlord's name.
    - Improved signature submission reliability by using a form `submit` event listener instead of an `onclick` event on the button.
- **Robust Float Conversion**: Fixed a `ValueError` by making the string-to-float conversion in the backend more robust, ensuring that empty form values for monetary fields are correctly handled as `0.0`.
- **Application Startup Fix**: Restored the `if __name__ == '__main__':` block in `app.py` to allow the Flask application to be run directly.

## How to use
1. Run `pip install flask fpdf`.
2. Run `python app.py`.
3. Fill out the fields; watch the right-hand panel update.
4. Sign in the box and click **Download PDF**.
