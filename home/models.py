# models.py
from django.db import models

from django.db import models

class Contact(models.Model):
    # Auto-generated primary key
    id = models.AutoField(primary_key=True)

    # Fields for collecting data
    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(max_length=100, verbose_name="Email Address")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Phone Number")
    subject = models.CharField(max_length=150, verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Submitted")
    
    # Optional status field (Pending, Responded, Closed)
    status_choices = [
        ('pending', 'Pending'),
        ('responded', 'Responded'),
        ('closed', 'Closed'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending', verbose_name="Status")

    def __str__(self):
        return f"Message from {self.full_name} ({self.email})"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ['-created_at']  # Sort by most recent first
