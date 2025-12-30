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
- **PDF Generation Fix**: Resolved multiple PDF generation issues:
    - Fixed a recurring `AttributeError` during file sending by re-adding the `mimetype='application/pdf'` parameter to the `send_file` function.
    - Addressed a `RuntimeError` related to an incorrect output destination by ensuring the PDF is generated using a compatible method (`dest='S'`).
    - Fixed an `AttributeError` when adding the signature image by using a temporary file. The in-memory `BytesIO` object was not compatible with the installed `fpdf` version, so the image is now saved to a temporary file on disk, the path is passed to `pdf.image()`, and the file is deleted after the PDF is generated.
- **Two-Page PDF Generation**: Added logic to `app.py` to generate the second page of the PDF, the "AFFIDAVIT OF SERVICE", ensuring that the downloaded PDF contains both pages as shown in the preview.
- **PDF Data and Submission Fixes**: 
    - Corrected the "Total Amount Due" by recalculating it on the backend.
    - Ensured "Print Name" is correctly displayed on the PDF by using the landlord's name.
    - Improved signature submission reliability by using a form `submit` event listener instead of an `onclick` event on the button.
- **Robust Float Conversion**: Fixed a `ValueError` by making the string-to-float conversion in the backend more robust, ensuring that empty form values for monetary fields are correctly handled as `0.0`.

## How to use
1. Run `pip install flask fpdf`.
2. Run `python app.py`.
3. Fill out the fields; watch the right-hand panel update.
4. Sign in the box and click **Download PDF**.
