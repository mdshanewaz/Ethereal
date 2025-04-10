from django.db import models

# Create your models here.

class FacultyModel(models.Model):
    faculty_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    name = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=300, null=True, blank=True)
    img = models.ImageField(upload_to='About_App/', null=True, blank=True)
    gender = models.CharField(choices=faculty_gender, max_length=10)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def get_image(self):
        if self.img:
            return self.img.url
        elif self.gender == 'Male':
            return '/media/default/default_male.jpg'
        else:
            return '/media/default/default_female.png'

    def __str__(self):
        return str(self.name)