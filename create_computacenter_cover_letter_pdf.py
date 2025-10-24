#!/usr/bin/env python3
"""
Create a professional PDF cover letter for Computacenter Lead Consultant (Data Protection SME) position
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
    """Create a professional PDF cover letter for Computacenter"""
    
    # Create PDF document
    pdf_filename = "Amin_Parva_Cover_Letter_Computacenter.pdf"
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
    story.append(Paragraph("Cover Letter - Lead Consultant (Data Protection SME)", title_style))
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
    story.append(Paragraph("<b>To:</b> Hiring Manager, Computacenter", body_style))
    story.append(Paragraph("<b>Re:</b> Lead Consultant (Data Protection SME) Position", body_style))
    story.append(Spacer(1, 15))
    
    # Greeting
    story.append(Paragraph("Dear Hiring Manager,", body_style))
    story.append(Spacer(1, 10))
    
    # Introduction paragraph
    intro_text = """
    I am writing to express my strong interest in the <b>Lead Consultant (Data Protection SME)</b> position at Computacenter. 
    With over 15 years of experience in enterprise technology solutions, data security, and technical leadership, I am excited 
    about the opportunity to contribute to Computacenter's mission of delivering innovative IT infrastructure solutions that 
    empower clients to achieve their strategic goals.
    """
    story.append(Paragraph(intro_text, body_style))
    story.append(Spacer(1, 12))
    
    # Why I'm Perfect for This Role section
    story.append(Paragraph("<b>Why I'm Perfect for This Role</b>", header_style))
    story.append(Spacer(1, 8))
    
    # Data Protection & Security Expertise
    story.append(Paragraph("<b>Data Protection & Security Expertise:</b>", body_style))
    story.append(Paragraph("• <b>Enterprise Data Security:</b> Led comprehensive data protection initiatives across healthcare and enterprise environments, implementing robust security measures for sensitive client data", body_style))
    story.append(Paragraph("• <b>Compliance & Governance:</b> Extensive experience with data privacy regulations, security frameworks, and compliance requirements in highly regulated industries", body_style))
    story.append(Paragraph("• <b>Technical Security Implementation:</b> Designed and implemented secure data architectures, encryption protocols, and access control systems for enterprise-scale applications", body_style))
    story.append(Spacer(1, 8))
    
    # Technical Leadership & Consulting
    story.append(Paragraph("<b>Technical Leadership & Consulting:</b>", body_style))
    story.append(Paragraph("• <b>Subject Matter Expert (SME):</b> Served as technical SME for large-scale enterprise integrations, providing expert guidance on data protection and security best practices", body_style))
    story.append(Paragraph("• <b>Cross-Functional Collaboration:</b> Successfully led technical teams and collaborated with stakeholders across multiple departments to ensure data protection compliance", body_style))
    story.append(Paragraph("• <b>Client-Facing Expertise:</b> Proven ability to communicate complex technical concepts to both technical and non-technical stakeholders, building trust and confidence", body_style))
    story.append(Spacer(1, 12))
    
    # Relevant Experience Highlights
    story.append(Paragraph("<b>Relevant Experience Highlights</b>", header_style))
    story.append(Spacer(1, 8))
    
    # Current Role
    story.append(Paragraph("<b>Current Role - AI/ML and Software Lead | Athlete Management Technologies</b>", body_style))
    story.append(Paragraph("• <b>Data Protection & Privacy:</b> Implemented comprehensive data protection measures for sensitive athlete performance data, ensuring compliance with privacy regulations", body_style))
    story.append(Paragraph("• <b>Secure Data Architecture:</b> Designed and built secure data pipelines processing real-time sensor data with end-to-end encryption and access controls", body_style))
    story.append(Paragraph("• <b>Cloud Security:</b> Architected secure cloud solutions using AWS with proper data classification, encryption, and monitoring", body_style))
    story.append(Spacer(1, 8))
    
    # Previous Experience
    story.append(Paragraph("<b>Previous Experience - Senior Technical Lead | Antech Diagnostics</b>", body_style))
    story.append(Paragraph("• <b>Healthcare Data Security:</b> Led data protection initiatives for 1000+ healthcare clients, ensuring HIPAA compliance and data security", body_style))
    story.append(Paragraph("• <b>Enterprise Integration Security:</b> Served as SME for Oracle-Antrim integration, implementing secure data transfer protocols and access controls", body_style))
    story.append(Paragraph("• <b>Compliance Management:</b> Developed and maintained data protection policies and procedures for enterprise healthcare systems", body_style))
    story.append(Spacer(1, 12))
    
    # What I Bring to Computacenter
    story.append(Paragraph("<b>What I Bring to Computacenter</b>", header_style))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("<b>Technical Excellence:</b>", body_style))
    story.append(Paragraph("• Deep expertise in data protection technologies, security frameworks, and compliance requirements", body_style))
    story.append(Paragraph("• Strong background in enterprise IT infrastructure, cloud security, and data governance", body_style))
    story.append(Paragraph("• Proven ability to design and implement secure, scalable solutions", body_style))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("<b>Leadership & Consulting:</b>", body_style))
    story.append(Paragraph("• 15+ years of technical leadership experience with a focus on data protection and security", body_style))
    story.append(Paragraph("• Strong client-facing skills with experience in enterprise consulting and stakeholder management", body_style))
    story.append(Paragraph("• Ability to translate complex technical requirements into practical, implementable solutions", body_style))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("<b>Industry Knowledge:</b>", body_style))
    story.append(Paragraph("• Extensive experience across healthcare, enterprise, and technology sectors", body_style))
    story.append(Paragraph("• Understanding of regulatory requirements and compliance frameworks", body_style))
    story.append(Paragraph("• Track record of delivering data protection solutions that meet business objectives", body_style))
    story.append(Spacer(1, 12))
    
    # Why Computacenter
    story.append(Paragraph("<b>Why Computacenter</b>", header_style))
    story.append(Spacer(1, 8))
    
    why_text = """
    I am particularly drawn to Computacenter's commitment to <b>putting customers first</b> and <b>being honest and straightforward</b> 
    in all interactions. Your focus on <b>diverse and inclusive</b> practices and <b>building a sustainable business</b> aligns perfectly 
    with my professional values. The opportunity to work with a company that has been a trusted technology partner for over 40 years 
    and serves some of the world's largest organizations is incredibly exciting.
    """
    story.append(Paragraph(why_text, body_style))
    story.append(Spacer(1, 8))
    
    interest_text = """
    I am particularly interested in contributing to Computacenter's <b>security solutions</b> and <b>consulting services</b>, where I can 
    leverage my expertise in data protection to help clients navigate complex security challenges and achieve their digital transformation goals.
    """
    story.append(Paragraph(interest_text, body_style))
    story.append(Spacer(1, 12))
    
    # Next Steps
    story.append(Paragraph("<b>Next Steps</b>", header_style))
    story.append(Spacer(1, 8))
    
    next_steps_text = """
    I would welcome the opportunity to discuss how my experience in data protection, technical leadership, and enterprise consulting 
    can contribute to Computacenter's continued success. I am confident that my combination of technical expertise, leadership experience, 
    and client-focused approach makes me an ideal candidate for this role.
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
    <i>P.S. I am particularly excited about the opportunity to work with Computacenter's diverse client base across financial services, 
    healthcare, and public sector organizations, where data protection expertise is critical for success.</i>
    """
    story.append(Paragraph(ps_text, body_style))
    
    # Build PDF
    doc.build(story)
    print(f"Cover letter PDF created successfully: {pdf_filename}")
    return pdf_filename

if __name__ == "__main__":
    create_cover_letter_pdf()
