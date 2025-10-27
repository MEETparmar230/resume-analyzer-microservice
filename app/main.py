from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
from app.nlp_utils import extract_skills, match_score
from app.db import supabase
import fitz  # PyMuPDF
import traceback

app = FastAPI(title="Resume Analyzer NLP")

@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(None),
    resume_text: str = Form(None),
    job_role: str = Form(None),
    job_description: str = Form(None)
):
    try:
        text = ""

        # 1️⃣ Extract text from uploaded PDF or direct text input
        if file:
            contents = await file.read()
            with fitz.open(stream=contents, filetype="pdf") as doc:
                for page in doc:
                    text += page.get_text("text")
            text = text.strip()
        elif resume_text:
            text = resume_text.strip()
        else:
            return {"error": "No resume file or text provided"}

        # 2️⃣ Initialize job skills
        job_skills = []
        role_skill_map = {
            "mern stack developer": ["MongoDB", "Express.js", "React.js", "Node.js", "JavaScript", "HTML", "CSS"],
            "java developer": ["Java", "Spring Boot", "SQL", "REST API", "Hibernate"],
            "data analyst": ["Python", "Pandas", "SQL", "Excel", "Visualization"],
        }

        # 3️⃣ Fetch job skills from Supabase or fallback
        if job_role:
            try:
                normalized_role = job_role.replace("_", " ").strip().lower()
                data = supabase.table("jobs").select("skills, title").execute()

                # Try to find a job title that approximately matches
                matched_row = next(
                    (row for row in data.data if normalized_role in row["title"].lower()),
                    None
                )

                if matched_row:
                    job_skills = matched_row["skills"]

                    # Handle case if Supabase stores skills as comma-separated string
                    if isinstance(job_skills, str):
                        job_skills = [s.strip() for s in job_skills.split(",")]

                else:
                    job_skills = []
            except Exception as e:
                print(f"⚠️ Could not fetch from Supabase: {e}")

            # Fallback to predefined map if Supabase lookup fails
            if not job_skills:
                job_skills = role_skill_map.get(normalized_role, [])

        # 4️⃣ If still empty, extract skills from job description text
        if not job_skills and job_description:
            job_skills = extract_skills(job_description)

        # 5️⃣ Extract resume skills and compute matching score
        resume_skills = extract_skills(text, job_skills)
        result = match_score(resume_skills, job_skills)

        # 6️⃣ Return structured response
        return {
            "resume_text": text[:800],  # preview text
            "job_role": job_role,
            "job_description": job_description,
            "skills_match": result
        }

    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}


@app.get('/')
async def root():
    return {"message": "✅ Resume Analyzer API is running successfully"}
