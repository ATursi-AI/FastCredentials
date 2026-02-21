from django.db import models
from django.contrib.auth.models import User
import uuid
import re

class Course(models.Model):
    CATEGORY_CHOICES = (
        ('medical', 'Medical & Healthcare'),
        ('workplace', 'Workplace Compliance'),
        ('safety', 'Safety & Trade'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='medical')
    # NEW PRIORITY FIELD
    priority = models.IntegerField(default=0, help_text="Higher number = Shows higher on homepage (e.g. 100 for Top, 0 for standard)")
    duration_minutes = models.IntegerField(default=30)
    icon_name = models.CharField(max_length=50, default='bi-shield-check')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=19.99)
    
    class Meta:
        # This automatically sorts them by Priority (High to Low), then A-Z
        ordering = ['-priority', 'title']

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="Main text content for this slide/module.")
    video_url = models.URLField(blank=True, null=True, help_text="Optional video link.")
    order = models.IntegerField(default=1)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    def get_embed_url(self):
        """
        Converts standard YouTube links into high-compatibility embed links 
        specifically for local development environments.
        """
        if not self.video_url:
            return None
            
        # Regex to capture the 11-character YouTube ID
        regex = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
        match = re.search(regex, self.video_url)
        
        if match:
            video_id = match.group(1)
            # The 'origin' and 'enablejsapi' flags are the proven fix for local Django servers
            return f"https://www.youtube.com/embed/{video_id}?origin=http://127.0.0.1:8000&enablejsapi=1&rel=0"
            
        return self.video_url

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    # NEW: Links the question to a specific slide for "Smart Failure" recommendations
    related_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True, related_name='questions', help_text="The slide that teaches the answer to this question.")
    text = models.CharField(max_length=500)
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)
    correct_option = models.IntegerField(help_text="1, 2, 3, or 4")

    def __str__(self):
        return self.text

class Certificate(models.Model):
    cert_id = models.CharField(max_length=50, unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='certificates/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    stripe_charge_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title} ($ {self.amount})"
