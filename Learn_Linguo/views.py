from django.shortcuts import render
import base64
import io
import whisper
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Assignment

def home(request):
    assignments = Assignment.objects.all()
    return render(request, "Learn_Linguo/home.html", {"assignments": assignments} )

def record_audio(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    return render(request, "Learn_Linguo/record_audio.html", {"assignment": assignment})

def save_audio(request):
    if request.method == "POST":
        audio_data = request.POST.get("audio_data", "")
        assignment_id = request.POST.get("assignment_id", "")

        if not assignment_id.isdigit():
            return HttpResponse("Error: Invalid assignment ID format")
        
        assignment_id = int(assignment_id)

    try: 
        if audio_data:
            audio_bytes = base64.b64decode(audio_data)
            with open("temp_audio.wav", "wb") as f:
                f.write(audio_bytes)

            model = whisper.load_model("base")
            result = model.transcribe("temp_audio.wav")
            transcribed_text = result["text"]
            assignment = get_object_or_404(Assignment, id=assignment_id)
            reference_text = assignment.reference_text

            missing_words = compare_texts(transcribed_text, reference_text)

            return HttpResponse(f"Transcribed Text: {transcribed_text}\n Reference Text: {reference_text} \n Missing Words: {missing_words}")
        else:
            return HttpResponse("Error: Invalid audio data format")
    except Exception as e:
        return HttpResponse(f"Error:{str(e)}")
    return HttpResponse("No audio data received")

def compare_texts(transcribed_text, reference_text):
    def normalize_text(text):
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        return text
    transcribed_text = normalize_text(transcribed_text)
    reference_text = normalize_text(reference_text)
    transcribed_words = set(transcribed_text.split())
    reference_words = set(reference_text.split())
    missing_words = reference_words - transcribed_words
    return ", ".join(missing_words)



