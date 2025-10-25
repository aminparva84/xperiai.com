from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

def create_biorad_cover_letter_pdf():
    """Create a PDF cover letter for Bio-Rad Lead Software Developer position"""
    
    # Create PDF document
    pdf_filename = "Amin_Parva_Cover_Letter_BioRad.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter, 
                          rightMargin=72, leftMargin=72, 
                          topMargin=72, bottomMargin=72)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Create custom styles
    header_style = ParagraphStyle(
        'Header',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=12,
        alignment=TA_LEFT,
        textColor=colors.black
    )
    
    date_style = ParagraphStyle(
        'Date',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=12,
        alignment=TA_LEFT,
        textColor=colors.black
    )
    
    greeting_style = ParagraphStyle(
        'Greeting',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=12,
        alignment=TA_LEFT,
        textColor=colors.black
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=12,
        alignment=TA_LEFT,
        textColor=colors.black,
        leftIndent=0,
        rightIndent=0
    )
    
    closing_style = ParagraphStyle(
        'Closing',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        alignment=TA_LEFT,
        textColor=colors.black
    )
    
    signature_style = ParagraphStyle(
        'Signature',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=0,
        alignment=TA_LEFT,
        textColor=colors.black
    )
    
    # Build content
    story = []
    
    # Header
    story.append(Paragraph("Amin Parva", header_style))
    story.append(Paragraph("39 Aliso Ridge Loop, Mission Viejo, CA 92691", header_style))
    story.append(Paragraph("(949) 922-4584 | parva.amin@yahoo.com", header_style))
    story.append(Spacer(1, 12))
    
    # Date
    story.append(Paragraph("January 5, 2025", date_style))
    story.append(Spacer(1, 12))
    
    # Greeting
    story.append(Paragraph("Dear Bio-Rad Hiring Team,", greeting_style))
    story.append(Spacer(1, 12))
    
    # Body paragraphs
    story.append(Paragraph("I am writing to express my strong interest in the Lead Software Developer position at Bio-Rad. With 15+ years of technical leadership experience and deep expertise in cloud-based application development, I am excited about the opportunity to contribute to Bio-Rad's mission of advancing scientific discovery and healthcare innovation.", body_style))
    
    story.append(Paragraph("<b>Technical Leadership & Cloud Expertise:</b><br/>My extensive experience aligns perfectly with your requirements. I have 8+ years of hands-on AWS experience, including DynamoDB, Aurora Postgres, SQS, SNS, S3, and Systems Manager. Currently, I lead AI/ML initiatives at Athlete Management Technologies, where I architect and develop cloud-based applications using modern frameworks and AWS services. My expertise spans the full technology stack you're seeking, including GoLang, .NET, Python, and Angular.", body_style))
    
    story.append(Paragraph("<b>Architecture & Design Excellence:</b><br/>I excel at ensuring software design aligns with approved architecture and effectively communicating design decisions to teams. In my current role, I define and document software specifications, establish coding standards, and drive the development process through informed decision-making. I have successfully led the design of enterprise-scale systems serving 10,000+ users while maintaining 99.9% uptime.", body_style))
    
    story.append(Paragraph("<b>Team Development & Mentoring:</b><br/>I am passionate about elevating technical expertise through mentoring and coaching. I have successfully mentored 25+ technical professionals, established Centers of Excellence for AI/ML adoption, and built high-performing development teams. My approach combines hands-on technical guidance with leadership development, ensuring team members grow both technically and professionally.", body_style))
    
    story.append(Paragraph("<b>Stakeholder Collaboration:</b><br/>I have extensive experience as a technical liaison among developers, testers, DevOps, and stakeholders. At Antech Diagnostics, I led cross-functional teams of 200+ professionals, ensuring seamless collaboration and alignment with business objectives. I excel at translating complex technical concepts into clear business value and securing stakeholder buy-in for innovative initiatives.", body_style))
    
    story.append(Paragraph("<b>Why Bio-Rad:</b><br/>Bio-Rad's 70-year legacy of advancing scientific discovery resonates deeply with my passion for technology that makes a meaningful impact. I am particularly drawn to the opportunity to contribute to life science and healthcare innovation while working with collaborative teams that span the globe.", body_style))
    
    story.append(Paragraph("I am excited about the possibility of bringing my technical leadership, cloud expertise, and team development skills to Bio-Rad. I would welcome the opportunity to discuss how my experience can contribute to your continued success in advancing scientific discovery.", body_style))
    
    story.append(Paragraph("Thank you for your consideration.", body_style))
    story.append(Spacer(1, 12))
    
    # Closing
    story.append(Paragraph("Sincerely,", closing_style))
    story.append(Spacer(1, 24))
    story.append(Paragraph("Amin Parva", signature_style))
    
    # Build PDF
    doc.build(story)
    print(f"✅ Successfully created PDF: {pdf_filename}")

if __name__ == "__main__":
    create_biorad_cover_letter_pdf()





