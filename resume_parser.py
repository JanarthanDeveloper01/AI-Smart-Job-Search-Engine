import pdfplumber
import docx

def extract_text_from_resume(uploaded_file):

    text = ""

    if uploaded_file.name.endswith(".pdf"):

        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

    elif uploaded_file.name.endswith(".docx"):

        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text

    return text