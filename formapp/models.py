from django.db import models

# Create your models here.
class EmploymentForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    position = models.CharField(max_length=50)
    resume = models.FileField(upload_to='resumes/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Employment Form'
        verbose_name_plural = 'Employment Forms'