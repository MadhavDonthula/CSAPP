from django.db import models

class ReferenceText(models.Model): 
    text = models.TextField()

class Transcription(models.Model):
    audio_file = models.FileField(upload_to="audio/")
    transcribed_text = models.TextField()
    reference_text = models.ForeignKey(ReferenceText, on_delete=models.CASCADE)

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    reference_text = models.TextField()

    def __str__(self):
        return self.name