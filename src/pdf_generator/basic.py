from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime
import os

def create_resume_pdf(data, filename="resume.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y_position = height - 50  # Start from top
    line_height = 15

    # Set font for the resume
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, y_position, data.get("name", "Your Name"))
    y_position -= line_height * 2

    c.setFont("Helvetica", 12)
    if data.get("email"):
        c.drawCentredString(width / 2, y_position, data["email"])
        y_position -= line_height
    if data.get("phone"):
        c.drawCentredString(width / 2, y_position, data["phone"])
        y_position -= line_height * 2

    # Education Section
    if data.get("education"):
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y_position, "Education")
        y_position -= line_height
        c.setFont("Helvetica", 12)
        for edu in data["education"]:
            c.drawString(50, y_position, edu)
            y_position -= line_height
        y_position -= line_height

    # Work Experience Section
    if data.get("work_experience"):
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y_position, "Work Experience")
        y_position -= line_height
        c.setFont("Helvetica", 12)
        for work in data["work_experience"]:
            c.drawString(50, y_position, work)
            y_position -= line_height
        y_position -= line_height

    # Skills Section
    if data.get("skills"):
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y_position, "Skills")
        y_position -= line_height
        c.setFont("Helvetica", 12)
        for skill in data["skills"]:
            c.drawString(50, y_position, skill)
            y_position -= line_height

    c.save()
    print(f"Resume saved as {filename}")

def get_user_input():
    resume_data = {}
    
    # Name
    name = input("Enter your full name (or type 'skip' to skip): ").strip()
    if name.lower() != "skip":
        resume_data["name"] = name
    else:
        resume_data["name"] = "Your Name"

    # Email
    email = input("Enter your email (or type 'skip' to skip): ").strip()
    if email.lower() != "skip":
        resume_data["email"] = email

    # Phone
    phone = input("Enter your phone number (or type 'skip' to skip): ").strip()
    if phone.lower() != "skip":
        resume_data["phone"] = phone

    # Education
    print("\nEnter your education details (e.g., Degree, University, Year).")
    print("Type 'done' when finished or 'skip' to skip this section.")
    education = []
    while True:
        edu = input("Education entry: ").strip()
        if edu.lower() == "done":
            break
        elif edu.lower() == "skip":
            education = []
            break
        elif edu:
            education.append(edu)
    if education:
        resume_data["education"] = education

    # Work Experience
    print("\nEnter your work experience (e.g., Job Title, Company, Dates).")
    print("Type 'done' when finished or 'skip' to skip this section.")
    work_experience = []
    while True:
        work = input("Work experience entry: ").strip()
        if work.lower() == "done":
            break
        elif work.lower() == "skip":
            work_experience = []
            break
        elif work:
            work_experience.append(work)
    if work_experience:
        resume_data["work_experience"] = work_experience

    # Skills
    print("\nEnter your skills (e.g., Python, Communication).")
    print("Type 'done' when finished or 'skip' to skip this section.")
    skills = []
    while True:
        skill = input("Skill: ").strip()
        if skill.lower() == "done":
            break
        elif skill.lower() == "skip":
            skills = []
            break
        elif skill:
            skills.append(skill)
    if skills:
        resume_data["skills"] = skills

    return resume_data

def main():
    print("Welcome to the Simple Resume Builder!")
    resume_data = get_user_input()
    filename = f"resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    create_resume_pdf(resume_data, filename)

if __name__ == "__main__":
    main()