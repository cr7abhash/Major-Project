from django.db import models

# Create your models here.
ORDER_STATUS_CHOICES = (
    ('not read', 'Not read'),
    ('read', 'Read'),
    ('emailed', 'Emailed'),
    ('called', 'Called'),
    ('still continuing', 'Still Continuing'),
)

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    address = models.CharField(max_length=120, null=True, blank=True)
    contact = models.CharField(max_length=22, null=True, blank=True)
    message = models.TextField(max_length=500, null=False, blank=False)
    status = models.CharField(max_length=120, choices=ORDER_STATUS_CHOICES, default='not read')

    def __str__(self):
        return str(self.pk)+ " " + str(self.email)