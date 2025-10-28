from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
from app.nlp_utils import extract_skills, match_score
from app.db import supabase
import fitz 
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

        # predefined roles
        role_skill_map = {
            "mern developer": ["React", "Node", "MongoDB", "Express", "JavaScript", "HTML", "CSS"],
            "mern stack developer": ["React", "Node", "MongoDB", "Express", "JavaScript", "HTML", "CSS"],
            "java developer": ["Java", "Spring Boot", "SQL", "REST API", "Hibernate"],
            "data analyst": ["Python", "Pandas", "SQL", "Excel", "Visualization"],
        }

        normalized_role = job_role.replace("_", " ").strip().lower() if job_role else ""
        job_skills = []

        # Try from Supabase
        if normalized_role:
            try:
                data = supabase.table("jobs").select("skills, title").execute()
                matched_row = next((r for r in data.data if normalized_role in r["title"].lower()), None)
                if matched_row:
                    job_skills = matched_row["skills"]
                    if isinstance(job_skills, str):
                        job_skills = [s.strip() for s in job_skills.split(",")]
            except Exception as e:
                print("⚠️ Supabase fetch error:", e)

        # Fallback to predefined
        if not job_skills and normalized_role:
            job_skills = role_skill_map.get(normalized_role, [])

        # Merge description
        if job_description:
            desc_skills = extract_skills(job_description)
            job_skills = list(set(job_skills + desc_skills))

        # Extract from resume
        resume_skills = extract_skills(text)

        # Match
        result = match_score(resume_skills, job_skills)

        return {
            "resume_text": text[:800],
            "job_role": job_role,
            "job_description": job_description,
            "skills_match": result
        }

    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}



@app.get("/")
async def root():
    return {"message": "✅ Resume Analyzer API is running successfully"}
