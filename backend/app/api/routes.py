# backend/app/api/routes.py

# from fastapi import APIRouter

# router = APIRouter()

# @router.get("/")
# def home():
#     return {
#         "message": "AI Recruitment Intelligence API is running = Routes.py"
#     }

from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import Dict
import io
from PyPDF2 import PdfReader
from docx import Document

router = APIRouter()

@router.get("/")
def home():
    return {"message": "AI Recruitment Intelligence API is running", "status": "active"}

def extract_text_from_file(file: UploadFile) -> str:
    """Extract text from PDF, DOC, or DOCX files"""
    content = file.file.read()
    filename = file.filename.lower()
    
    try:
        if filename.endswith('.pdf'):
            reader = PdfReader(io.BytesIO(content))
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text.strip()
            
        elif filename.endswith(('.docx', '.doc')):
            doc = Document(io.BytesIO(content))
            text = "\n".join([para.text for para in doc.paragraphs])
            return text.strip()
        
        else:
            raise HTTPException(400, detail="Unsupported file type")
    except Exception as e:
        raise HTTPException(500, detail=f"Error extracting text: {str(e)}")


@router.post("/analyze")
async def analyze_candidate(
    cv: UploadFile = File(...),
    job_description: UploadFile = File(...)
):
    allowed_extensions = {'.pdf', '.doc', '.docx'}
    
    if not any(cv.filename.lower().endswith(ext) for ext in allowed_extensions):
        raise HTTPException(400, detail="CV must be PDF, DOC, or DOCX")
    if not any(job_description.filename.lower().endswith(ext) for ext in allowed_extensions):
        raise HTTPException(400, detail="Job Description must be PDF, DOC, or DOCX")
    
    # استخراج النص
    cv_text = extract_text_from_file(cv)
    jd_text = extract_text_from_file(job_description)
    
    return {
        "status": "success",
        "cv_filename": cv.filename,
        "job_description_filename": job_description.filename,
        "cv_text_length": len(cv_text),
        "jd_text_length": len(jd_text),
        "message": "Text extracted successfully. Ready for AI matching.",
        "cv_excerpt": cv_text[:500] + "..." if len(cv_text) > 500 else cv_text,
        "jd_excerpt": jd_text[:500] + "..." if len(jd_text) > 500 else jd_text
    }