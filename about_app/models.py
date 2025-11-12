from django.db import models

# Create your models here.

class FacultyModel(models.Model):
    faculty_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    name = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=300, null=True, blank=True)
    education = models.CharField(max_length=500, null=True, blank=True)
    img = models.ImageField(upload_to='about_app/', null=True, blank=True)
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
    

class ContactModel(models.Model):
    grade = (
        ('Nursery', 'Nursery'),
        ('Lower KG', 'Lower KG'),
        ('Upper KG', 'Upper KG'),
        ('Grade One', 'Grade One'),
        ('Grade Two', 'Grade Two'),
        ('Grade Three', 'Grade Three'),
        ('Grade Four', 'Grade Four'),
        ('Grade Five', 'Grade Five'), 
        ('Grade Six', 'Grade Six'),
        ('Grade Seven', 'Grade Seven'),
        ('Grade Eight', 'Grade Eight'),
        ('Grade Nine', 'Grade Nine'),
        ('O Level', 'O Level'),
        ('As Level', 'As Level'),
        ('A Level', 'A Level'),
    )

    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    grade = models.CharField(choices=grade, max_length=20)
    message = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f"Message from {self.name}"
