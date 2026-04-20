import re

def clean_text(text: str) -> str:
    """
    Cleans extracted text by:
    - Removing extra spaces
    - Removing unwanted characters
    """

    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove weird characters (optional tweak later)
    text = re.sub(r'[^\w\s.,;:()\-]', '', text)

    return text.strip()