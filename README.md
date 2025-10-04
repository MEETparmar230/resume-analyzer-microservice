
# Resume Analyzer Microservice

A **FastAPI-based microservice** that extracts skills from resumes and matches them with job requirements using NLP. This service can be integrated with any frontend or backend application to provide skill-matching insights in real-time.

---

## Features

- Extracts skills from resumes (PDF or text input)
- Matches extracted skills against predefined job roles or custom job descriptions
- Calculates skill match score and highlights missing skills
- Easy integration with other services (microservice architecture)

---

## Tech Stack

- **Backend:** FastAPI
- **NLP:** spaCy
- **Database:** PostgreSQL (Supabase)
- **Containerization:** Docker
- **Deployment:** AWS (EC2)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/resume-analyzer-microservice.git
cd resume-analyzer-microservice
```
### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
### 4. Configure environment variables

```bash
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_api_key
```
### 5. Initialize the database

```bash
python run_init.py
```
### 6. Run the API locally

```bash
uvicorn app.main:app --reload
```
The API will be available at http://127.0.0.1:8000.

---

## API Endpoints

### POST /analyze
Analyze a resume and match with a job role or custom description.

Request Body:
```bash
{
  "resume_text": "John Doe is a MERN stack developer skilled in React, Node.js, MongoDB, and Express.",
  "job_role": "mern_developer",
  "job_description": "Optional custom job description"
}
```

Response:
```bash
{
  "resume_skills": ["React", "Node.js", "MongoDB", "Express"],
  "job_skills": ["React", "Node.js", "MongoDB", "Express", "Redux", "JWT"],
  "matched_skills": ["React", "Node.js", "MongoDB", "Express"],
  "missing_skills": ["Redux", "JWT"],
  "match_score": 66.67
}
```

### GET /

Basic health check:
```bash
{
  "Message": "Resume Analyzer API is running"
}
```
---

## Docker Deployment

# 1. Build Docker image
```bash
docker build -t resume-analyzer-microservice.
```

# 2. Run Docker container
```bash
docker run -p 8000:8000 --env-file .env resume-analyzer-microservice
```
---

## Future Plans

- Add PDF parsing directly within the service
- Integrate ML-based skill extraction for better accuracy
- Scale as a microservice for multiple frontend apps
- CI/CD automation for seamless deployments

---

## Author

Meet Parmar

Portfolio: [Portfolio Site](https://my-portfolio-site-theta-five.vercel.app/)

Email: meetparmar2362004@gmail.com