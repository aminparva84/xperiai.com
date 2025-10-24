from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

def create_cover_letter_pdf():
    """Create a PDF cover letter for Engineering Manager position at Compa"""
    
    # Create PDF document
    pdf_filename = "Amin_Parva_Cover_Letter_Compa.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=A4, 
                          rightMargin=60, leftMargin=60, 
                          topMargin=60, bottomMargin=60)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Create custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=12,
        alignment=TA_CENTER,
        textColor=colors.darkblue
    )
    
    header_style = ParagraphStyle(
        'CoverHeader',
        parent=styles['Heading2'],
        fontSize=12,
        spaceAfter=6,
        textColor=colors.darkblue
    )
    
    body_style = ParagraphStyle(
        'CoverBody',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=6,
        leading=14
    )
    
    # Build content
    story = []
    
    # Header
    story.append(Paragraph("AMIN PARVA", title_style))
    story.append(Paragraph("Senior Software Architect & AI/ML Engineering Director", styles['Normal']))
    story.append(Paragraph("parva.amin@yahoo.com | (949) 922-4584 | 39 Aliso Ridge Loop, Mission Viejo, CA 92691", styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Date
    story.append(Paragraph("December 2024", styles['Normal']))
    story.append(Spacer(1, 12))
    
    # Recipient
    story.append(Paragraph("Hiring Manager", styles['Normal']))
    story.append(Paragraph("Compa", styles['Normal']))
    story.append(Paragraph("Orange County HQ", styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Salutation
    story.append(Paragraph("Dear Hiring Manager,", styles['Normal']))
    story.append(Spacer(1, 12))
    
    # Body paragraphs
    story.append(Paragraph("I am writing to express my strong interest in the Engineering Manager, Core Infrastructure position at Compa. With 15+ years of experience leading technical teams and architecting enterprise-scale systems, I am excited about the opportunity to drive infrastructure innovation and build high-performing engineering teams at your Orange County headquarters.", body_style))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("In my current role as AI/ML Engineering Director at Athlete Management Technologies, I have successfully led cross-functional teams of 10+ engineers while architecting and implementing enterprise-scale ML pipelines processing 10TB+ of sensor data daily. My expertise in building scalable infrastructure, managing technical teams, and driving operational excellence aligns perfectly with Compa's mission to revolutionize compensation technology.", body_style))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("<b>Key Leadership Achievements:</b>", header_style))
    story.append(Paragraph("• <b>Team Leadership:</b> Led 10+ member engineering teams across 15+ major projects, consistently delivering on-time and within budget", body_style))
    story.append(Paragraph("• <b>Infrastructure Architecture:</b> Designed microservices architecture improving system scalability by 300% and reducing deployment time by 80%", body_style))
    story.append(Paragraph("• <b>Technical Mentoring:</b> Mentored 20+ developers, with 90% of mentees receiving promotions within 18 months", body_style))
    story.append(Paragraph("• <b>Process Innovation:</b> Transformed traditional agile teams into AI-powered development structures, improving team productivity by 40%", body_style))
    story.append(Paragraph("• <b>Cross-functional Collaboration:</b> Successfully coordinated with product, design, and business teams to deliver complex technical solutions", body_style))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("<b>Core Infrastructure Expertise:</b>", header_style))
    story.append(Paragraph("• <b>Cloud Platforms:</b> AWS, Azure, GCP with expertise in SageMaker, EMR, Lambda, and container orchestration", body_style))
    story.append(Paragraph("• <b>Data Engineering:</b> Real-time data processing using Apache Kafka, Spark, and Airflow", body_style))
    story.append(Paragraph("• <b>System Design:</b> Microservices, API design, database architecture, and performance optimization", body_style))
    story.append(Paragraph("• <b>DevOps & MLOps:</b> Docker, Kubernetes, CI/CD pipelines, and automated deployment strategies", body_style))
    story.append(Paragraph("• <b>Programming:</b> Python, C#, .NET Core, JavaScript, SQL with focus on scalable backend systems", body_style))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("What particularly excites me about Compa is your innovative approach to compensation technology and the opportunity to build robust infrastructure that can scale with your growing platform. I am drawn to your mission of making compensation more transparent and equitable, and I believe my experience in building reliable, high-performance systems can contribute significantly to your technical vision.", body_style))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("I am particularly impressed by Compa's commitment to engineering excellence and would welcome the opportunity to discuss how my leadership experience and technical expertise can help drive your infrastructure initiatives forward. I am confident that my proven track record of building and leading high-performing engineering teams, combined with my deep technical knowledge, makes me an ideal fit for this role.", body_style))
    
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("Thank you for considering my application. I look forward to the opportunity to discuss how I can contribute to Compa's continued success.", body_style))
    
    story.append(Spacer(1, 20))
    
    # Closing
    story.append(Paragraph("Best regards,", styles['Normal']))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Amin Parva", styles['Normal']))
    
    # Build PDF
    doc.build(story)
    print(f"✅ Successfully created cover letter PDF: {pdf_filename}")
    return pdf_filename

if __name__ == "__main__":
    create_cover_letter_pdf()






