from fastapi import FastAPI
from pydantic import BaseModel
from app.nlp_utils import extract_skills, match_score
from app.db import supabase

app = FastAPI(title="Resume Analyzer NLP")

class ResumeRequest(BaseModel):
    resume_text: str
    job_role: str = None
    job_description: str = None

@app.post("/analyze")
async def analyze_resume(req: ResumeRequest):
    # Fetch job skills from Supabase if job_role is provided
    if req.job_role:
        data = supabase.table("jobs").select("skills").eq("title", req.job_role).execute()
        job_skills = data.data[0]["skills"] if data.data else []
    elif req.job_description:
        # Extract skills from custom job description
        job_skills = extract_skills(req.job_description, skills_list=[])
    else:
        job_skills = []

    # Extract skills from resume based on job_skills
    resume_skills = extract_skills(req.resume_text, job_skills)

    # Calculate match score
    result = match_score(resume_skills, job_skills)
    return result

@app.get('/')
async def root():
    return {"Message": "Resume Analyser API is running"}
