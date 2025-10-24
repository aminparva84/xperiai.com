import PyPDF2

def check_1page_pdf():
    with open('Amin_Parva_Resume_1Page.pdf', 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        print(f"Number of pages: {len(reader.pages)}")
        print("Content preview:")
        print(text[:2000])

if __name__ == "__main__":
    check_1page_pdf()




