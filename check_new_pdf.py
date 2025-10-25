import PyPDF2

def check_pdf_content(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text

if __name__ == "__main__":
    text = check_pdf_content('Amin_Parva_Resume_Updated.pdf')
    print(text[:2000])  # First 2000 characters





