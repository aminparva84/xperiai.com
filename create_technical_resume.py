from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import os

def create_technical_resume():
    """Create a technical-focused PDF resume for Software Architect and AI/Data Engineer positions"""
    
    # Create PDF document
    pdf_filename = "Amin_Parva_Technical_Resume.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=A4, 
                          rightMargin=60, leftMargin=60, 
                          topMargin=60, bottomMargin=60)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Create custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=6,
        alignment=TA_CENTER,
        textColor=colors.darkblue
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=12,
        alignment=TA_CENTER,
        textColor=colors.darkblue
    )
    
    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=6,
        spaceBefore=12,
        textColor=colors.darkblue
    )
    
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_CENTER,
        spaceAfter=12
    )
    
    # Build content
    story = []
    
    # Header
    story.append(Paragraph("AMIN PARVA", title_style))
    story.append(Paragraph("Senior Software Architect & AI/Data Engineer", subtitle_style))
    story.append(Paragraph("parva.amin@yahoo.com | (949) 922-4584 | 39 Aliso Ridge Loop, Mission Viejo, CA 92691", contact_style))
    story.append(Spacer(1, 12))
    
    # Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_style))
    summary_text = """
    Senior Software Architect and AI/Data Engineer with 15+ years of experience designing and implementing enterprise-scale systems, machine learning pipelines, and data processing solutions. Currently specializing in athlete performance analytics, predictive modeling, and real-time data processing at Athlete Management Technologies. <b>Expert in data trimming, pattern recognition, and advanced analytics</b> with deep expertise in software architecture, AI/ML implementation, and data engineering. Proven track record of architecting scalable systems, optimizing data processing workflows, and delivering high-performance solutions across healthcare, sports technology, and enterprise domains.
    """
    story.append(Paragraph(summary_text, styles['Normal']))
    story.append(Spacer(1, 12))
    
    # Core Technical Competencies
    story.append(Paragraph("CORE TECHNICAL COMPETENCIES", section_style))
    
    competencies_data = [
        ['Software Architecture & Design', 'Microservices Architecture, System Design, API Design, Database Design, Cloud Architecture, Scalable Systems, Performance Optimization, Security Architecture, Event-Driven Architecture, Domain-Driven Design'],
        ['AI/ML & Data Engineering', 'Machine Learning Pipeline Design, Data Processing, Pattern Recognition, Predictive Analytics, Neural Networks, Deep Learning, TensorFlow, PyTorch, Scikit-learn, MLOps, Data Pipeline Architecture, Real-time Data Processing'],
        ['Programming & Development', 'Python (Pandas, NumPy, SciPy, Matplotlib, Seaborn), C#, .NET Core, JavaScript, TypeScript, SQL, R, Scala, Go, Rust, Java, C++, VB.NET, HTML5, CSS3, SASS'],
        ['Data Technologies & Tools', 'Apache Spark, Apache Kafka, Apache Airflow, Apache Hadoop, Apache Flink, Apache Beam, Apache NiFi, Apache Superset, Jupyter, Apache Zeppelin, Apache Druid, ClickHouse, Apache Pinot'],
        ['Cloud & Infrastructure', 'AWS (SageMaker, EMR, Glue, Kinesis, Lambda, S3, RDS, Redshift, DynamoDB), Azure (Synapse, Data Factory, ML Studio), GCP (BigQuery, Dataflow, AI Platform), Docker, Kubernetes, Terraform, Ansible'],
        ['Databases & Storage', 'PostgreSQL, MySQL, Oracle, SQL Server, MongoDB, Cassandra, Redis, Elasticsearch, InfluxDB, TimescaleDB, Apache HBase, Apache Hive, Apache Impala, Snowflake, BigQuery']
    ]
    
    # Convert competencies data to use Paragraph objects for better text wrapping
    competencies_table_data = []
    for category, skill_list in competencies_data:
        # Create paragraph for category with proper wrapping
        category_paragraph = Paragraph(category, ParagraphStyle(
            'CategoryText',
            parent=styles['Normal'],
            fontSize=8,
            leading=10,
            leftIndent=0,
            rightIndent=0
        ))
        # Create paragraph for skill list with proper wrapping
        skill_paragraph = Paragraph(skill_list, ParagraphStyle(
            'SkillText',
            parent=styles['Normal'],
            fontSize=6,
            leading=8,
            leftIndent=0,
            rightIndent=0
        ))
        competencies_table_data.append([category_paragraph, skill_paragraph])
    
    # Create competencies table with better formatting
    competencies_table = Table(competencies_table_data, colWidths=[2.0*inch, 4.0*inch], repeatRows=1, splitByRow=1)
    competencies_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.darkblue),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('BACKGROUND', (1, 0), (1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, colors.beige])
    ]))
    
    story.append(competencies_table)
    story.append(Spacer(1, 8))
    
    # Professional Experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_style))
    
    # Current Role
    story.append(Paragraph("<b>AI/ML Engineer & Data Architect</b> | <b>Athlete Management Technologies</b> | Feb 2025 - Present", styles['Heading3']))
    story.append(Paragraph("<i>Designing and implementing AI/ML systems and data processing pipelines for athlete performance analytics</i>", styles['Normal']))
    
    technical_achievements = [
        "Architected and implemented enterprise-scale ML pipeline processing 10TB+ of sensor data daily, serving 10,000+ athletes with 99.9% uptime",
        "Developed advanced data trimming algorithms and pattern recognition models using Python, TensorFlow, and scikit-learn, improving data quality by 95%",
        "Designed real-time data processing system using Apache Kafka and Apache Spark, reducing data processing latency from 5 minutes to 30 seconds",
        "Implemented automated feature engineering pipeline with 200+ engineered features for movement pattern analysis and performance prediction",
        "Built scalable data architecture using AWS SageMaker, S3, and EMR, handling 50M+ data points per day with sub-second query response times",
        "Created comprehensive data validation and quality monitoring system using Apache Airflow and custom Python scripts, reducing data errors by 90%",
        "Designed and implemented MLOps pipeline with automated model training, validation, and deployment using Docker and Kubernetes"
    ]
    
    for achievement in technical_achievements:
        story.append(Paragraph(f"• {achievement}", styles['Normal']))
    
    story.append(Spacer(1, 8))
    
    # Antech Role
    story.append(Paragraph("<b>Senior Software Architect & Technical Lead</b> | <b>Antech Diagnostics (Mars Inc.)</b> | Oct 2015 - Nov 2024", styles['Heading3']))
    story.append(Paragraph("<i>Architecting enterprise healthcare systems and leading technical implementation across multiple large-scale projects</i>", styles['Normal']))
    
    antech_technical_achievements = [
        "Architected and implemented 15+ enterprise-scale healthcare systems serving 5,000+ clients, processing 100M+ lab results annually",
        "Designed microservices architecture using .NET Core, Docker, and Kubernetes, improving system scalability by 300% and reducing deployment time by 80%",
        "Led technical implementation of HL7 integration system, processing 1M+ messages daily with 99.99% reliability and sub-second response times",
        "Architected data warehouse solution using Oracle and SQL Server, optimizing query performance by 500% through advanced indexing and partitioning",
        "Implemented real-time data processing pipeline using Apache Kafka and .NET Core, reducing data processing time from hours to minutes",
        "Designed and developed RESTful APIs and GraphQL endpoints, serving 10,000+ concurrent users with 99.9% availability",
        "Led technical migration from legacy MUMPS/Cache systems to modern .NET architecture, improving system performance by 400%"
    ]
    
    for achievement in antech_technical_achievements:
        story.append(Paragraph(f"• {achievement}", styles['Normal']))
    
    story.append(Spacer(1, 8))
    
    # Technijian Role
    story.append(Paragraph("<b>Software Architect & Senior Engineer</b> | <b>Technijian</b> | Jan 2015 - Oct 2015", styles['Heading3']))
    story.append(Paragraph("<i>Designing and implementing enterprise software solutions and leading technical architecture decisions</i>", styles['Normal']))
    
    technijian_technical_achievements = [
        "Architected n-tier enterprise software platform using ASP.NET MVC, Entity Framework, and SQL Server, serving 10,000+ users with 99.9% uptime",
        "Designed and implemented comprehensive security framework with OAuth 2.0, JWT tokens, and role-based access control, achieving SOC 2 compliance",
        "Developed real-time data synchronization system using SignalR and WebSockets, enabling real-time updates across distributed systems",
        "Architected API gateway solution using .NET Core and Ocelot, managing 50+ microservices with rate limiting and authentication",
        "Implemented advanced caching strategies using Redis and in-memory caching, improving application performance by 200%",
        "Designed and developed responsive web applications using AngularJS, jQuery, and Bootstrap, ensuring cross-browser compatibility"
    ]
    
    for achievement in technijian_technical_achievements:
        story.append(Paragraph(f"• {achievement}", styles['Normal']))
    
    story.append(Spacer(1, 8))
    
    # ParvaGroup Role
    story.append(Paragraph("<b>Technical Director & Lead Developer</b> | <b>ParvaGroup</b> | July 2008 - Nov 2014", styles['Heading3']))
    story.append(Paragraph("<i>Leading technical development and architecting web-based solutions for enterprise clients</i>", styles['Normal']))
    
    parva_technical_achievements = [
        "Architected and developed 75+ web applications using ASP.NET, C#, SQL Server, and JavaScript, serving 25+ enterprise clients",
        "Designed scalable database schemas and optimized SQL queries, improving application performance by 300% and reducing load times by 60%",
        "Implemented comprehensive testing framework using NUnit and Selenium, achieving 95% code coverage and reducing bugs by 80%",
        "Developed custom CMS solution using .NET and SQL Server, enabling clients to manage content with 99.9% uptime",
        "Architected multi-tenant SaaS platform with role-based access control and automated provisioning, serving 500+ users",
        "Led technical team of 8 developers, implementing agile methodologies and establishing coding standards and best practices"
    ]
    
    for achievement in parva_technical_achievements:
        story.append(Paragraph(f"• {achievement}", styles['Normal']))
    
    story.append(Spacer(1, 8))
    
    # Key Technical Projects
    story.append(Paragraph("KEY TECHNICAL PROJECTS", section_style))
    
    # Project 1
    story.append(Paragraph("<b>Athlete Performance Analytics Platform</b> | <b>Athlete Management Technologies</b> | 2025", styles['Heading3']))
    project1_text = """
    <b>Technologies:</b> Python, TensorFlow, Apache Spark, Apache Kafka, AWS SageMaker, Docker, Kubernetes, PostgreSQL, Redis<br/>
    <b>Architecture:</b> Microservices-based real-time data processing platform with ML pipeline for athlete performance prediction<br/>
    <b>Key Contributions:</b> Designed and implemented end-to-end data pipeline processing 10TB+ daily sensor data, developed advanced pattern recognition algorithms, and built scalable ML infrastructure serving 10,000+ athletes with 99.9% uptime.
    """
    story.append(Paragraph(project1_text, styles['Normal']))
    story.append(Spacer(1, 6))
    
    # Project 2
    story.append(Paragraph("<b>Healthcare Data Integration Platform</b> | <b>Antech Diagnostics</b> | 2020-2024", styles['Heading3']))
    project2_text = """
    <b>Technologies:</b> .NET Core, Apache Kafka, Oracle, SQL Server, Docker, Kubernetes, Redis, Elasticsearch<br/>
    <b>Architecture:</b> Event-driven microservices architecture with real-time data processing and HL7 integration<br/>
    <b>Key Contributions:</b> Architected and implemented enterprise-scale healthcare data platform processing 100M+ lab results annually, designed real-time data streaming pipeline, and led technical migration from legacy systems to modern architecture.
    """
    story.append(Paragraph(project2_text, styles['Normal']))
    story.append(Spacer(1, 6))
    
    # Project 3
    story.append(Paragraph("<b>Enterprise Client Portal Platform</b> | <b>Technijian</b> | 2015", styles['Heading3']))
    project3_text = """
    <b>Technologies:</b> ASP.NET MVC, Entity Framework, SQL Server, AngularJS, SignalR, Redis, OAuth 2.0<br/>
    <b>Architecture:</b> N-tier enterprise application with real-time features and comprehensive security framework<br/>
    <b>Key Contributions:</b> Designed and developed enterprise portal platform serving 10,000+ users, implemented real-time data synchronization, and architected comprehensive security framework achieving SOC 2 compliance.
    """
    story.append(Paragraph(project3_text, styles['Normal']))
    story.append(Spacer(1, 8))
    
    # Certifications
    story.append(Paragraph("CERTIFICATIONS", section_style))
    certs = [
        "Scrum Master | LinkedIn Learning | 2024",
        "Leadership Fundamentals | LinkedIn Learning | 2024", 
        "Management in Organization | LinkedIn Learning | 2024",
        "Advanced C# | LinkedIn Learning | 2024"
    ]
    
    for cert in certs:
        story.append(Paragraph(f"• {cert}", styles['Normal']))
    
    story.append(Spacer(1, 8))
    
    # Awards
    story.append(Paragraph("AWARDS", section_style))
    story.append(Paragraph("🏆 <b>Antech Tax Benefits Reward</b> for High Performance Employees | 2024", styles['Normal']))
    story.append(Spacer(1, 8))
    
    # Education
    story.append(Paragraph("EDUCATION", section_style))
    story.append(Paragraph("<b>Bachelor of Science in Electrical Engineering</b>", styles['Normal']))
    story.append(Paragraph("Azad University, Bushehr, Iran | 2003 - 2008", styles['Normal']))
    story.append(Spacer(1, 8))
    
    # Additional Information
    story.append(Paragraph("ADDITIONAL INFORMATION", section_style))
    additional_info = [
        "Languages: English (Fluent), Persian (Native)",
        "Work Authorization: US Citizen", 
        "Availability: Open to relocation and remote work",
        "Specializations: Data Engineering, Machine Learning, Software Architecture, Real-time Data Processing, Pattern Recognition"
    ]
    
    for info in additional_info:
        story.append(Paragraph(f"• {info}", styles['Normal']))
    
    # Build PDF
    doc.build(story)
    print(f"✅ Successfully created technical resume PDF: {pdf_filename}")
    return pdf_filename

if __name__ == "__main__":
    create_technical_resume()







