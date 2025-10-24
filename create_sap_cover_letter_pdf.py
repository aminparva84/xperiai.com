#!/usr/bin/env python3
"""
Create a professional PDF cover letter for SAP Senior AI/ML Applied Scientist - Generative AI position
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from datetime import datetime

def create_cover_letter_pdf():
    """Create a professional PDF cover letter for SAP"""
    
    # Create PDF document
    pdf_filename = "Amin_Parva_Cover_Letter_SAP.pdf"
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
        alignment=TA_CENTER,
        textColor=HexColor('#2c3e50')
    )
    
    header_style = ParagraphStyle(
        'CustomHeader',
        parent=styles['Heading2'],
        fontSize=12,
        spaceAfter=6,
        alignment=TA_LEFT,
        textColor=HexColor('#34495e')
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        alignment=TA_JUSTIFY,
        leftIndent=0,
        rightIndent=0
    )
    
    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontSize=9,
        spaceAfter=3,
        alignment=TA_CENTER,
        textColor=HexColor('#7f8c8d')
    )
    
    # Build content
    story = []
    
    # Title
    story.append(Paragraph("Cover Letter - Senior AI/ML Applied Scientist - Generative AI", title_style))
    story.append(Spacer(1, 12))
    
    # Contact information
    story.append(Paragraph("Amin Parva", header_style))
    story.append(Paragraph("39 Aliso Ridge Loop, Mission Viejo, CA 92691", contact_style))
    story.append(Paragraph("(949) 922-4584 | parva.amin@yahoo.com", contact_style))
    story.append(Paragraph("[LinkedIn Profile] | [Portfolio]", contact_style))
    story.append(Spacer(1, 20))
    
    # Date and recipient
    current_date = datetime.now().strftime("%B %d, %Y")
    story.append(Paragraph(f"<b>Date:</b> {current_date}", body_style))
    story.append(Paragraph("<b>To:</b> Hiring Manager, SAP", body_style))
    story.append(Paragraph("<b>Re:</b> Senior AI/ML Applied Scientist - Generative AI Position", body_style))
    story.append(Spacer(1, 15))
    
    # Greeting
    story.append(Paragraph("Dear Hiring Manager,", body_style))
    story.append(Spacer(1, 10))
    
    # Introduction paragraph
    intro_text = """
    I am writing to express my strong interest in the <b>Senior AI/ML Applied Scientist - Generative AI</b> position at SAP. 
    With over 15 years of experience in artificial intelligence, machine learning, and generative AI technologies, I am excited 
    about the opportunity to contribute to SAP's innovative initiatives in this rapidly evolving domain.
    """
    story.append(Paragraph(intro_text, body_style))
    story.append(Spacer(1, 12))
    
    # Why I'm Perfect for This Role section
    story.append(Paragraph("<b>Why I'm Perfect for This Role</b>", header_style))
    story.append(Spacer(1, 8))
    
    # Generative AI & Large Language Models Expertise
    story.append(Paragraph("<b>Generative AI & Large Language Models Expertise:</b>", body_style))
    story.append(Paragraph("• <b>Advanced AI/ML Implementation:</b> Currently leading AI/ML solutions at Athlete Management Technologies, specializing in generative AI and large language model integration", body_style))
    story.append(Paragraph("• <b>AI Agent Orchestration:</b> Extensive experience with AI agents (Cursor AI) and modern AI-powered development methodologies", body_style))
    story.append(Paragraph("• <b>Foundation Model Integration:</b> Proven track record of integrating foundation models into production systems and streamlining transformation journeys", body_style))
    story.append(Spacer(1, 8))
    
    # Technical Excellence in AI/ML
    story.append(Paragraph("<b>Technical Excellence in AI/ML:</b>", body_style))
    story.append(Paragraph("• <b>Deep Learning Frameworks:</b> Expert proficiency in TensorFlow, TensorFlow Lite, PyTorch, and modern ML frameworks", body_style))
    story.append(Paragraph("• <b>Generative AI Technologies:</b> Hands-on experience with large language models, neural networks, and ensemble methods", body_style))
    story.append(Paragraph("• <b>Production AI Systems:</b> Successfully architected and deployed AI models at enterprise scale with real-time processing capabilities", body_style))
    story.append(Spacer(1, 8))
    
    # Research & Innovation Leadership
    story.append(Paragraph("<b>Research & Innovation Leadership:</b>", body_style))
    story.append(Paragraph("• <b>Applied AI Research:</b> 15+ years of experience translating cutting-edge AI research into practical business solutions", body_style))
    story.append(Paragraph("• <b>Team Leadership:</b> Proven ability to mentor junior data scientists and lead strategic AI initiatives", body_style))
    story.append(Paragraph("• <b>Cross-Functional Collaboration:</b> Successfully led AI teams across multiple departments and stakeholder groups", body_style))
    story.append(Spacer(1, 12))
    
    # Relevant Experience Highlights
    story.append(Paragraph("<b>Relevant Experience Highlights</b>", header_style))
    story.append(Spacer(1, 8))
    
    # Current Role
    story.append(Paragraph("<b>Current Role - AI/ML and Software Lead | Athlete Management Technologies</b>", body_style))
    story.append(Paragraph("• <b>Generative AI Implementation:</b> Leading the development of AI-powered solutions using large language models and generative AI technologies", body_style))
    story.append(Paragraph("• <b>AI Agent Integration:</b> Pioneered the use of AI agents in development workflows, resulting in 40% improvement in team productivity", body_style))
    story.append(Paragraph("• <b>Foundation Model Deployment:</b> Architected and deployed TensorFlow and TensorFlow Lite models with Flask APIs for real-time inference", body_style))
    story.append(Paragraph("• <b>MLOps & Production Systems:</b> Built comprehensive CI/CD pipelines for AI model deployment using AWS SageMaker and containerization", body_style))
    story.append(Spacer(1, 8))
    
    # Previous Experience
    story.append(Paragraph("<b>Previous Experience - Senior Technical Lead | Antech Diagnostics</b>", body_style))
    story.append(Paragraph("• <b>Enterprise AI Solutions:</b> Led AI/ML initiatives for 1000+ healthcare clients, implementing predictive analytics and pattern recognition systems", body_style))
    story.append(Paragraph("• <b>Data Science Leadership:</b> Served as technical SME for large-scale enterprise integrations, providing expert guidance on AI/ML best practices", body_style))
    story.append(Paragraph("• <b>Research & Development:</b> Developed innovative solutions using advanced machine learning techniques for healthcare data analysis", body_style))
    story.append(Spacer(1, 12))
    
    # What I Bring to SAP
    story.append(Paragraph("<b>What I Bring to SAP</b>", header_style))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("<b>Technical Excellence:</b>", body_style))
    story.append(Paragraph("• Deep expertise in generative AI, large language models, and foundation model integration", body_style))
    story.append(Paragraph("• Strong background in deep learning frameworks, MLOps, and production AI systems", body_style))
    story.append(Paragraph("• Proven ability to design and implement scalable AI solutions that deliver business value", body_style))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("<b>Leadership & Innovation:</b>", body_style))
    story.append(Paragraph("• 15+ years of technical leadership experience with a focus on AI/ML and generative AI", body_style))
    story.append(Paragraph("• Strong research background with experience in applied AI and machine learning", body_style))
    story.append(Paragraph("• Ability to mentor junior data scientists and lead strategic AI initiatives", body_style))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("<b>Industry Knowledge:</b>", body_style))
    story.append(Paragraph("• Extensive experience across healthcare, enterprise, and technology sectors", body_style))
    story.append(Paragraph("• Understanding of enterprise AI requirements and cloud transformation challenges", body_style))
    story.append(Paragraph("• Track record of delivering AI solutions that meet business objectives and drive innovation", body_style))
    story.append(Spacer(1, 12))
    
    # Why SAP
    story.append(Paragraph("<b>Why SAP</b>", header_style))
    story.append(Spacer(1, 8))
    
    why_text = """
    I am particularly drawn to SAP's commitment to <b>leveraging large language models to accelerate cloud transformation</b> for clients. 
    Your focus on <b>foundation model integration</b> and <b>streamlining cloud transformation journeys</b> aligns perfectly with my expertise 
    in generative AI and enterprise AI solutions.
    """
    story.append(Paragraph(why_text, body_style))
    story.append(Spacer(1, 8))
    
    interest_text = """
    The opportunity to work with SAP's <b>collaborative environment</b> and <b>global teams</b> presents an exciting platform for innovation. 
    I am particularly interested in contributing to the development and integration of foundation models into SAP solutions, where I can 
    leverage my experience in AI agent orchestration and modern AI-powered development methodologies.
    """
    story.append(Paragraph(interest_text, body_style))
    story.append(Spacer(1, 12))
    
    # Key Differentiators
    story.append(Paragraph("<b>Key Differentiators</b>", header_style))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("<b>Unique Value Proposition:</b>", body_style))
    story.append(Paragraph("• <b>AI Agent Expertise:</b> Pioneered the transformation of traditional development teams into AI-powered organizations", body_style))
    story.append(Paragraph("• <b>Production AI Experience:</b> Successfully deployed generative AI solutions in enterprise environments", body_style))
    story.append(Paragraph("• <b>Technical Leadership:</b> Proven ability to lead AI initiatives while maintaining hands-on technical involvement", body_style))
    story.append(Paragraph("• <b>Business Impact:</b> Track record of delivering AI solutions that generate measurable ROI and drive business success", body_style))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("<b>Research & Development:</b>", body_style))
    story.append(Paragraph("• <b>Applied AI Focus:</b> Experience translating cutting-edge AI research into practical business solutions", body_style))
    story.append(Paragraph("• <b>Innovation Leadership:</b> Led the development of novel AI approaches and methodologies", body_style))
    story.append(Paragraph("• <b>Cross-Domain Expertise:</b> Applied AI solutions across healthcare, sports analytics, and enterprise systems", body_style))
    story.append(Spacer(1, 12))
    
    # Next Steps
    story.append(Paragraph("<b>Next Steps</b>", header_style))
    story.append(Spacer(1, 8))
    
    next_steps_text = """
    I would welcome the opportunity to discuss how my experience in generative AI, technical leadership, and applied AI research 
    can contribute to SAP's continued success in this exciting field. I am confident that my combination of technical expertise, 
    leadership experience, and passion for AI innovation makes me an ideal candidate for this role.
    """
    story.append(Paragraph(next_steps_text, body_style))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("Thank you for considering my application. I look forward to hearing from you soon.", body_style))
    story.append(Spacer(1, 15))
    
    # Closing
    story.append(Paragraph("Best regards,", body_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph("Amin Parva", body_style))
    story.append(Spacer(1, 12))
    
    # P.S.
    ps_text = """
    <i>P.S. I am particularly excited about the opportunity to work with SAP's global teams and contribute to the advancement of 
    AI-driven solutions that deliver tangible business value to enterprise clients worldwide.</i>
    """
    story.append(Paragraph(ps_text, body_style))
    
    # Build PDF
    doc.build(story)
    print(f"Cover letter PDF created successfully: {pdf_filename}")
    return pdf_filename

if __name__ == "__main__":
    create_cover_letter_pdf()



