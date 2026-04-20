from pypdf import PdfReader
from fastapi import UploadFile
from app.utils.text_cleaner import clean_text

def extract_text_from_pdf(file: UploadFile) -> str:
    """
    Extracts text from uploaded PDF file.
    """

    reader = PdfReader(file.file)

    text = ""

    # Loop through all pages
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    # Clean text before returning
    cleaned_text = clean_text(text)

    return cleaned_text