from django.db import models

class ReferenceText(models.Model): 
    text = models.TextField()

class Transcription(models.Model):
    audio_file = models.FileField(upload_to="audio/")
    transcribed_text = models.TextField()
    reference_text = models.ForeignKey(ReferenceText, on_delete=models.CASCADE)

class Assignment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class QuestionAnswer(models.Model):
    assignment = models.ForeignKey(Assignment, related_name="questions", on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"Question: {self.question[:30]}"
    
