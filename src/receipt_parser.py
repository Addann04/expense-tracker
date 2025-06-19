def parse_receipt(uploaded_file):
    import pytesseract
    from pdf2image import convert_from_path
    import re

    filename = uploaded_file.name.lower()
    if filename.endswith('.pdf'):
        file_bytes = uploaded_file.read()
        images = convert_from_path(file_bytes)
        text = ''
        for image in images:
            text += pytesseract.image_to_string(image)
    elif filename.endswith(('.jpg', '.jpeg', '.png')):
        file_bytes = uploaded_file.read()
        text = pytesseract.image_to_string(file_bytes)
    else:
        return None

    date_pattern = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b'
    amount_pattern = r'\$\d+(?:\.\d{2})?'
    vendor_pattern = r'(?<=\n)(.*?)(?=\n)'

    date_match = re.search(date_pattern, text)
    amount_match = re.search(amount_pattern, text)
    vendor_match = re.search(vendor_pattern, text)

    date = date_match.group(0) if date_match else None
    amount = amount_match.group(0) if amount_match else None
    vendor = vendor_match.group(0).strip() if vendor_match else None

    return {
        'date': date,
        'amount': amount,
        'vendor': vendor
    }