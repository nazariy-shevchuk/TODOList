from django.db import models

# Create your models here.
class Task(models.Model): # db model is called Task
    TODO = 0
    DONE = 1

    STATUS_CHOICES = ( # Create a tuple of status choises
        (TODO, 'To do'),
        (DONE, 'Done')
    )

    description = models.CharField(max_length=255)  # The tasks description is limited to 255 characters
    status = models.IntegerField(choices=STATUS_CHOICES, default=TODO)  # The task's status, default status = TODO
