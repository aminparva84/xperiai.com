from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import black, darkblue

def create_cimarron_cover_letter():
    # Create PDF
    pdf_filename = "Amin_Parva_Cover_Letter_Cimarron.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter, 
                          rightMargin=72, leftMargin=72, 
                          topMargin=72, bottomMargin=72)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Create custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=12,
        textColor=darkblue,
        alignment=1  # Center alignment
    )
    
    header_style = ParagraphStyle(
        'Header',
        parent=styles['Heading2'],
        fontSize=12,
        spaceAfter=6,
        textColor=black
    )
    
    normal_style = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=6,
        leading=14
    )
    
    # Build content
    story = []
    
    # Title
    story.append(Paragraph("Amin Parva", title_style))
    story.append(Paragraph("AI/ML and Software Lead", normal_style))
    story.append(Paragraph("39 Aliso Ridge Loop, Mission Viejo, CA 92691", normal_style))
    story.append(Paragraph("(949) 922-4584 | parva.amin@yahoo.com", normal_style))
    story.append(Spacer(1, 20))
    
    # Date
    story.append(Paragraph("February 2025", normal_style))
    story.append(Spacer(1, 12))
    
    # Company info
    story.append(Paragraph("Cimarron Software", header_style))
    story.append(Paragraph("El Segundo, CA 90245", normal_style))
    story.append(Spacer(1, 12))
    
    # Subject
    story.append(Paragraph("Re: DevSecOps Lead Software Engineer Position", header_style))
    story.append(Spacer(1, 12))
    
    # Cover letter content
    story.append(Paragraph("Dear Hiring Manager,", normal_style))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph(
        "I am writing to express my strong interest in the DevSecOps Lead Software Engineer position at Cimarron Software. "
        "With 15+ years of technical leadership experience and a proven track record in AI/ML engineering, cloud architecture, "
        "and security-focused development practices, I am excited to bring my expertise to Cimarron's innovative software solutions.",
        normal_style
    ))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph(
        "<b>DevSecOps Leadership & Cloud Security Expertise:</b>",
        header_style
    ))
    story.append(Paragraph(
        "Currently leading AI/ML initiatives at Athlete Management Technologies, I have extensive experience in implementing "
        "security-first development practices across cloud infrastructure. I have architected and deployed comprehensive "
        "CI/CD pipelines using GitHub Actions and Docker containerization, ensuring secure code deployment to AWS cloud "
        "services including ECR, App Runner, and EC2. My experience includes implementing enterprise-grade security measures "
        "for AI agent deployments using AWS Bedrock and LangChain frameworks, ensuring compliance and data protection.",
        normal_style
    ))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph(
        "<b>Full-Stack Development & AI Integration:</b>",
        header_style
    ))
    story.append(Paragraph(
        "I bring deep expertise in modern development stacks including Python, C#, JavaScript, and cloud technologies. "
        "My current role involves building end-to-end ML pipelines with TensorFlow and PyTorch, developing Flask APIs for "
        "model deployment, and creating mobile applications with Flutter that integrate TensorFlow Lite for offline inference. "
        "I have successfully implemented AI agents for internal employee support, demonstrating my ability to integrate "
        "cutting-edge AI technologies into production systems while maintaining security and performance standards.",
        normal_style
    ))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph(
        "<b>Technical Leadership & Team Management:</b>",
        header_style
    ))
    story.append(Paragraph(
        "Throughout my career, I have led cross-functional teams and mentored developers while implementing Agile/Scrum "
        "methodologies. At Antech Diagnostics (Mars Inc.), I served as Senior Technical Lead, managing enterprise-scale "
        "healthcare systems and leading digital transformation initiatives. I have experience in vendor management, "
        "stakeholder communication, and driving technical innovation across diverse technology stacks including .NET, "
        "Oracle databases, and cloud migration projects.",
        normal_style
    ))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph(
        "<b>Why Cimarron Software:</b>",
        header_style
    ))
    story.append(Paragraph(
        "Cimarron Software's reputation for innovative software solutions and commitment to technical excellence aligns "
        "perfectly with my career goals. I am particularly excited about the opportunity to lead DevSecOps initiatives "
        "that combine my passion for AI/ML technologies with robust security practices. My experience in building scalable, "
        "secure cloud applications and leading technical teams makes me well-positioned to contribute to Cimarron's continued success.",
        normal_style
    ))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph(
        "I would welcome the opportunity to discuss how my technical expertise and leadership experience can contribute "
        "to Cimarron Software's DevSecOps initiatives. Thank you for considering my application.",
        normal_style
    ))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("Sincerely,", normal_style))
    story.append(Paragraph("Amin Parva", normal_style))
    
    # Build PDF
    doc.build(story)
    print(f"Successfully created PDF: {pdf_filename}")
    return pdf_filename

if __name__ == "__main__":
    create_cimarron_cover_letter()



