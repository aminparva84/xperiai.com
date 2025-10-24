import os
import subprocess
import sys

def convert_html_to_pdf():
    """Convert HTML resume to PDF using available tools"""
    
    html_file = "Amin_Parva_Resume_Professional_Template.html"
    pdf_file = "Amin_Parva_Resume_Professional_Template.pdf"
    
    if not os.path.exists(html_file):
        print(f"Error: {html_file} not found!")
        return False
    
    try:
        # Try using weasyprint first
        print("Attempting to convert using weasyprint...")
        subprocess.run([sys.executable, "-m", "weasyprint", html_file, pdf_file], check=True)
        print(f"✅ Successfully created PDF: {pdf_file}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Weasyprint not available, trying alternative method...")
        
        try:
            # Try using wkhtmltopdf if available
            subprocess.run(["wkhtmltopdf", html_file, pdf_file], check=True)
            print(f"✅ Successfully created PDF: {pdf_file}")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("wkhtmltopdf not available, trying browser method...")
            
            try:
                # Try using Chrome/Edge headless
                chrome_paths = [
                    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
                ]
                
                for chrome_path in chrome_paths:
                    if os.path.exists(chrome_path):
                        cmd = [
                            chrome_path,
                            "--headless",
                            "--disable-gpu",
                            "--print-to-pdf=" + pdf_file,
                            "--print-to-pdf-no-header",
                            "file:///" + os.path.abspath(html_file)
                        ]
                        subprocess.run(cmd, check=True)
                        print(f"✅ Successfully created PDF: {pdf_file}")
                        return True
                        
            except subprocess.CalledProcessError:
                pass
    
    print("❌ Could not convert to PDF automatically.")
    print("\n📋 Manual conversion options:")
    print("1. Open the HTML file in your browser")
    print("2. Press Ctrl+P (Print)")
    print("3. Select 'Save as PDF' as destination")
    print("4. Save as 'Amin_Parva_Resume_Professional_Template.pdf'")
    print("\nOr install weasyprint: pip install weasyprint")
    
    return False

if __name__ == "__main__":
    convert_html_to_pdf()






