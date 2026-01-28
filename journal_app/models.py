from django.db import models

class JournalEntry(models.Model):
    user_text = models.TextField()
    ai_advice = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entry on {self.created_at.strftime('%Y-%m-%d')}"