def validate_file_type(file):
    allowed_extensions = ['jpg', 'jpeg', 'png', 'pdf']
    if file is not None:
        file_extension = file.name.split('.')[-1].lower()
        if file_extension in allowed_extensions:
            return True
    return False

def log_message(message):
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(message)

def format_expense_data(expense_data):
    return {
        'date': expense_data.get('date'),
        'amount': expense_data.get('amount'),
        'vendor': expense_data.get('vendor'),
        'description': expense_data.get('description', '')
    }