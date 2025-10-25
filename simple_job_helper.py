#!/usr/bin/env python3
"""
Simple Job Application Helper
Opens job search URLs and provides application guidance
"""

import webbrowser
import time
import json

def open_job_search_tabs():
    """Open multiple job search tabs with optimized URLs"""
    print("🌐 OPENING JOB SEARCH TABS")
    print("=" * 40)
    
    # Optimized LinkedIn URLs
    linkedin_urls = [
        "https://www.linkedin.com/jobs/search/?keywords=Senior%20Software%20Architect&location=Remote&f_TPR=r604800&f_E=4%2C5%2C6%2C7",
        "https://www.linkedin.com/jobs/search/?keywords=AI%20Data%20Engineer&location=Remote&f_TPR=r604800&f_E=4%2C5%2C6%2C7",
        "https://www.linkedin.com/jobs/search/?keywords=Machine%20Learning%20Engineer&location=Remote&f_TPR=r604800&f_E=4%2C5%2C6%2C7",
        "https://www.linkedin.com/jobs/search/?keywords=Senior%20Data%20Engineer&location=Remote&f_TPR=r604800&f_E=4%2C5%2C6%2C7",
        "https://www.linkedin.com/jobs/search/?keywords=Technical%20Lead&location=Remote&f_TPR=r604800&f_E=4%2C5%2C6%2C7"
    ]
    
    # Indeed URLs
    indeed_urls = [
        "https://www.indeed.com/jobs?q=Senior+Software+Architect&l=Remote&fromage=7&sort=date",
        "https://www.indeed.com/jobs?q=AI+Data+Engineer&l=Remote&fromage=7&sort=date",
        "https://www.indeed.com/jobs?q=Machine+Learning+Engineer&l=Remote&fromage=7&sort=date",
        "https://www.indeed.com/jobs?q=Senior+Data+Engineer&l=Remote&fromage=7&sort=date",
        "https://www.indeed.com/jobs?q=Technical+Lead&l=Remote&fromage=7&sort=date"
    ]
    
    # Other job boards
    other_urls = [
        "https://www.glassdoor.com/Job/remote-senior-software-architect-jobs-SRCH_KO0,32.htm",
        "https://angel.co/jobs#find/f!%7B%22types%22%3A%5B%22full-time%22%5D%2C%22roles%22%3A%5B%22Software%20Engineer%22%5D%7D",
        "https://www.hired.com/",
        "https://www.levels.fyi/",
        "https://www.toptal.com/"
    ]
    
    all_urls = linkedin_urls + indeed_urls + other_urls
    
    print(f"Opening {len(all_urls)} job search tabs...")
    
    for i, url in enumerate(all_urls, 1):
        try:
            webbrowser.open(url)
            print(f"  {i}. Opened: {url}")
            time.sleep(1)  # Wait 1 second between opening tabs
        except Exception as e:
            print(f"  {i}. Error opening: {url}")
    
    print("\n✅ All job search tabs opened!")
    print("💡 TIP: Use Ctrl+Tab to switch between tabs efficiently")

def create_application_tracker():
    """Create a simple application tracker"""
    print("\n📊 CREATING APPLICATION TRACKER")
    print("=" * 40)
    
    tracker_data = {
        "applications": [],
        "interviews": [],
        "offers": [],
        "rejections": [],
        "statistics": {
            "total_applications": 0,
            "response_rate": 0,
            "interview_rate": 0,
            "offer_rate": 0
        }
    }
    
    with open("job_tracker.json", "w") as f:
        json.dump(tracker_data, f, indent=2)
    
    print("✅ Application tracker created: job_tracker.json")
    print("📝 Use this to track your applications and progress")

def show_application_tips():
    """Show application tips and strategies"""
    print("\n💡 APPLICATION TIPS & STRATEGIES")
    print("=" * 40)
    
    tips = [
        "🎯 TARGET 3-5 APPLICATIONS PER DAY",
        "⏰ SPEND 1 HOUR MORNING APPLYING",
        "📝 CUSTOMIZE EACH COVER LETTER",
        "🔍 USE KEYWORDS FROM JOB POSTING",
        "📞 FOLLOW UP AFTER 1 WEEK",
        "🤝 CONNECT WITH HIRING MANAGERS ON LINKEDIN",
        "📚 RESEARCH COMPANY BEFORE APPLYING",
        "💼 UPLOAD BOTH RESUMES (TECHNICAL & PROFESSIONAL)",
        "⭐ APPLY WITHIN 24 HOURS OF POSTING",
        "📈 TRACK ALL APPLICATIONS AND OUTCOMES"
    ]
    
    for tip in tips:
        print(f"  {tip}")
    
    print("\n🎯 DAILY ROUTINE:")
    print("  Morning (1 hour): Apply to 3-5 positions")
    print("  Afternoon (30 min): Follow up on pending applications")
    print("  Evening (30 min): Research companies and prepare for interviews")
    
    print("\n📈 WEEKLY GOALS:")
    print("  • Apply to 20-25 positions")
    print("  • Get 2-3 phone screens")
    print("  • Connect with 10 new professionals")
    print("  • Research 5 new companies")

def show_cover_letter_template():
    """Show a cover letter template"""
    print("\n📝 COVER LETTER TEMPLATE")
    print("=" * 40)
    
    template = """
Dear Hiring Manager,

I am writing to express my strong interest in the {POSITION} position at {COMPANY}. With 15+ years of experience designing and implementing enterprise-scale systems, I am excited about the opportunity to contribute to your technical architecture and drive innovation.

In my current role as AI/ML Engineer at Athlete Management Technologies, I have architected and implemented enterprise-scale ML pipelines processing 10TB+ of sensor data daily, serving 10,000+ athletes with 99.9% uptime. My expertise in microservices architecture, real-time data processing, and cloud infrastructure aligns perfectly with your requirements.

Key highlights of my experience:
• Architected 15+ enterprise-scale healthcare systems serving 5,000+ clients
• Designed microservices architecture improving scalability by 300%
• Led technical migration from legacy systems to modern architecture
• Implemented real-time data processing pipelines reducing latency by 90%

I am particularly drawn to {COMPANY} because of your commitment to {COMPANY_FOCUS}. I would welcome the opportunity to discuss how my technical expertise and architectural vision can contribute to your team's success.

Thank you for your consideration.

Best regards,
Amin Parva
    """
    
    print(template)
    print("\n🔧 CUSTOMIZE:")
    print("  • Replace {POSITION} with actual job title")
    print("  • Replace {COMPANY} with company name")
    print("  • Replace {COMPANY_FOCUS} with company's tech focus")

def main():
    """Main function to run the job application helper"""
    print("🚀 JOB APPLICATION HELPER")
    print("=" * 50)
    print("This tool will help you apply to jobs more efficiently!")
    print()
    
    # Open job search tabs
    open_job_search_tabs()
    
    # Create application tracker
    create_application_tracker()
    
    # Show tips and strategies
    show_application_tips()
    
    # Show cover letter template
    show_cover_letter_template()
    
    print("\n🎯 READY TO START APPLYING!")
    print("=" * 50)
    print("1. Use the opened tabs to find jobs")
    print("2. Customize the cover letter template")
    print("3. Track your applications in job_tracker.json")
    print("4. Follow up on applications after 1 week")
    print("5. Connect with hiring managers on LinkedIn")
    
    print("\n💪 SUCCESS METRICS:")
    print("• Target: 20-25 applications per week")
    print("• Goal: 2-3 phone screens per week")
    print("• Aim: 1-2 on-site interviews per month")
    print("• Target: 1 job offer per month")

if __name__ == "__main__":
    main()







