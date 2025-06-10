import os
import tempfile

# Text extraction libraries
import docx2txt
import pandas as pd
import PyPDF2
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .recommendation import recommend_from_resume


# --- Utility: Extract text from uploaded resume ---
def extract_text_from_resume(file):
    ext = os.path.splitext(file.name)[1].lower()
    text = ""

    if ext == '.pdf':
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    elif ext in ['.docx', '.doc']:
        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
            for chunk in file.chunks():
                tmp.write(chunk)
            tmp_path = tmp.name
        text = docx2txt.process(tmp_path)
        os.remove(tmp_path)

    return text


# --- Main view: Handles both query string and resume upload ---
@csrf_exempt
def course_recommendation(request):
    query = request.GET.get('q', '')
    recommended_courses = []

    # Resume upload logic
    if request.method == "POST" and request.FILES.get('resume'):
        resume_file = request.FILES['resume']
        resume_text = extract_text_from_resume(resume_file)

        if resume_text.strip():
            # Use embedding to recommend courses
            recommended_courses = recommend_from_resume(resume_text)

    elif query:
        # Fallback: recommend from text input query
        recommended_courses = recommend_courses(query)

    # Convert DataFrame to list of dicts if needed
    if isinstance(recommended_courses, pd.DataFrame):
        recommended_courses = recommended_courses.to_dict(orient='records')

    # AJAX response
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'courses': recommended_courses})

    # Normal render
    return render(request, 'myapp/index.html', {
        'recommended_courses': recommended_courses,
        'query': query
    })


# Optional fallback for home route
def index(request):
    return render(request, 'myapp/index.html')
