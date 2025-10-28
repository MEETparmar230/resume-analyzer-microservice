import re

def extract_skills(text: str, known_skills=None):
    """
    Extracts likely technical skills from text by matching known keywords
    or scanning for tech-like patterns.
    """
    if not text:
        return []

    text = text.lower()

    # If known skills provided, match against them (fuzzy match)
    extracted = set()
    if known_skills:
        for skill in known_skills:
            skill_lower = skill.lower()
            # Loose matching: allows React == React.js
            pattern = re.escape(skill_lower).replace(r"\.", r".?")
            if re.search(rf"\b{pattern}\b", text):
                extracted.add(skill)
    else:
        # Generic tech keyword list if no known skills
        possible_skills = [
            "python", "java", "javascript", "react", "react.js", "next.js",
            "node", "node.js", "express", "express.js", "mongodb", "mysql",
            "html", "css", "tailwind", "git", "github", "rest api", "sql",
            "docker", "aws"
        ]
        for skill in possible_skills:
            pattern = re.escape(skill).replace(r"\.", r".?")
            if re.search(rf"\b{pattern}\b", text):
                extracted.add(skill)

    return sorted(extracted)


# ✅ New logic starts here
def normalize_skill(skill: str):
    """Normalize skill names for fair comparison."""
    return re.sub(r'[\s\.\-\_]+', '', skill.lower())


def match_score(resume_skills, job_skills):
    """
    Compare resume skills with job-required skills and compute match percentage.
    """
    # Normalize both lists
    resume_norm = [normalize_skill(s) for s in resume_skills]
    job_norm = [normalize_skill(s) for s in job_skills]

    matched = []
    missing = []

    # Compare each job skill against normalized resume skills
    for jskill, jnorm in zip(job_skills, job_norm):
        if any(
            abs(len(r) - len(jnorm)) <= 3 and (jnorm in r or r in jnorm)
            for r in resume_norm
        ):
            matched.append(jskill)
        else:
            missing.append(jskill)

    score = round(len(matched) / len(job_skills) * 100, 2) if job_skills else 0

    return {
        "resume_skills": sorted(resume_skills),
        "job_skills": sorted(job_skills),
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
        "match_score": score
    }
