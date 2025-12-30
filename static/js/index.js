    const canvas = document.getElementById('signature-pad');
    const signaturePad = new SignaturePad(canvas, {
        backgroundColor: 'rgb(250, 250, 250)' // Same as CSS background
    });
    const noticeForm = document.getElementById('noticeForm');

    function resizeCanvas() {
        const ratio = Math.max(window.devicePixelRatio || 1, 1);
        canvas.width = canvas.offsetWidth * ratio;
        canvas.height = canvas.offsetHeight * ratio;
        canvas.getContext("2d").scale(ratio, ratio);
        signaturePad.clear(); // otherwise isEmpty() might be dirty
    }

    window.addEventListener("resize", resizeCanvas);
    resizeCanvas();

    function saveSignature() {
        if (!signaturePad.isEmpty()) {
            document.getElementById('signature_img').value = signaturePad.toDataURL();
        }
    }

    noticeForm.addEventListener('submit', saveSignature);
    
    function updatePreview() {
        // From visible inputs (Notice Details)
        document.getElementById('preview_notice_date').innerText = document.getElementById('in_date').value;
        const landlordName = document.getElementById('in_lname').value;
        document.getElementById('preview_landlord_name').innerText = landlordName;
        document.getElementById('preview_print_name').innerText = landlordName.toUpperCase();
        document.getElementById('preview_affidavit_name').innerText = landlordName;
        document.getElementById('preview_affidavit_print_name').innerText = landlordName.toUpperCase();
        document.getElementById('preview_property_address').innerText = document.getElementById('in_addr').value;
        document.getElementById('preview_landlord_address').innerText = document.getElementById('in_landlord_address').value;
        document.getElementById('preview_state').innerText = document.getElementById('in_state').value || '_________';
        document.getElementById('preview_county').innerText = document.getElementById('in_county').value || '_________';
        document.getElementById('preview_tenant_names').innerText = document.getElementById('in_tenant_names').value;
        document.getElementById('preview_lease_date').innerText = document.getElementById('in_lease_date').value;
        
        const rentalDueStartDate = document.getElementById('in_rental_due_start_date').value;
        const rentalDueEndDate = document.getElementById('in_rental_due_end_date').value;
        let rentPeriod = "";
        if (rentalDueStartDate && rentalDueEndDate) {
            rentPeriod = `${rentalDueStartDate} to ${rentalDueEndDate}`;
        } else if (rentalDueStartDate) {
            rentPeriod = rentalDueStartDate;
        } else if (rentalDueEndDate) {
            rentPeriod = rentalDueEndDate;
        }
        document.getElementById('preview_rent_period').innerText = rentPeriod || "_________";

        const rentDue = parseFloat(document.getElementById('in_rent').value) || 0;
        document.getElementById('preview_rent_due').innerText = rentDue.toFixed(2);
        const lateFees = parseFloat(document.getElementById('in_late_fees').value) || 0;
        document.getElementById('preview_late_fees').innerText = lateFees.toFixed(2);
        const otherFees = parseFloat(document.getElementById('in_other_fees').value) || 0;
        document.getElementById('preview_other_fees').innerText = otherFees.toFixed(2);

        const totalDue = rentDue + lateFees + otherFees;
        document.getElementById('preview_total_due').innerText = totalDue.toFixed(2);

        document.getElementById('preview_telephone').innerText = document.getElementById('in_telephone').value;
        document.getElementById('preview_email').innerText = document.getElementById('in_email').value;

        // From visible inputs (Affidavit of Service)
        document.getElementById('preview_date_of_service').innerText = document.getElementById('in_date_of_service').value;
        const authName = document.getElementById('in_authorized_individual_name').value;
        document.getElementById('preview_authorized_individual_name_1').innerText = authName || '_____________________________________';
        document.getElementById('preview_authorized_individual_name_2').innerText = authName || '_____________________________________';
    }

    // Initial call to populate preview
    document.addEventListener('DOMContentLoaded', updatePreview);