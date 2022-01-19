from django.db import models


class ToDo(models.Model):

    choices_priority = [
        ('Urgent', 'Urgent'),
        ('Medium', 'Medium'),
        ('Later', 'Later'),
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    priority = models.CharField(max_length=6, choices=choices_priority)
    is_active = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} + {self.priority}'
