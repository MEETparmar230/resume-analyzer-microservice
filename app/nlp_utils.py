import spacy
import re

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_skills(text: str, skills_list: list = None):
    """
    Extract skills from text.
    - If skills_list is provided, match against it.
    - If skills_list is empty or None, try to extract skills from text using comma separation.
    """
    if skills_list:
        # Match against given skills list
        found_skills = []
        for skill in skills_list:
            pattern = re.compile(rf"\b{skill}\b", re.IGNORECASE)
            if pattern.search(text):
                found_skills.append(skill)
        return list(set(found_skills))
    else:
        # Extract potential skills from free-text (comma-separated)
        text = re.sub(r"(Required skills:|Skills:)", "", text, flags=re.IGNORECASE)
        skills = [s.strip() for s in text.split(",") if s.strip()]
        return skills

def match_score(resume_skills, job_skills):
    """Compare resume skills with job skills list."""
    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))
    
    score = (len(matched) / len(job_skills)) * 100 if job_skills else 0
    
    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched,
        "missing_skills": missing,
        "match_score": round(score, 2)
    }
