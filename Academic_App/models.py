from django.db import models

# Create your models here.

CATEGORY_CHOICES = ( 
    ("Islam", "Islam"), 
    ("Hinduism", "Hinduism"), 
    ("Buddhism", "Buddhism"), 
    ("Christianity", "Christianity"),
)

class PersonalModel(models.Model):
    MARITAL_CHOICES = (("married", "Married"), ("single", "Single"))
    GENDER_CHOICES = (("male", "Male"), ("female", "Female"))

    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    permanent_address = models.TextField()
    present_address = models.TextField()
    contact_num_1 = models.CharField(max_length=20)
    contact_num_2 = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    married = models.CharField(max_length=10, choices=MARITAL_CHOICES)
    spous_name = models.CharField(max_length=100, blank=True, null=True)
    religon = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to='Career/', blank=True, null=True)
    signature = models.ImageField(upload_to='Signature/', blank=True, null=True)

    def __str__(self):
        return self.name

class EducationModel(models.Model):
    exam_choice = (
        ('SSC', 'SSC'),
        ('HSC', 'HSC'),
        ('Graduation', 'Graduation'),
        ('Post Graduation', 'Post Graduation')
    )
    application = models.ForeignKey(PersonalModel, on_delete=models.CASCADE, related_name="educations")
    exam = models.CharField(max_length=50, choices=exam_choice)  # SSC, HSC, etc.
    year = models.PositiveIntegerField()
    result = models.CharField(max_length=20)
    group_subject = models.CharField(max_length=100)
    institute = models.CharField(max_length=200)
    board_university = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.exam} - {self.application.name}"

class TrainingModel(models.Model):
    application = models.ForeignKey(PersonalModel, on_delete=models.CASCADE, related_name="trainings")
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    result = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    institute = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} - {self.application.name}"

class ExperienceModel(models.Model):
    application = models.ForeignKey(PersonalModel, on_delete=models.CASCADE, related_name="experiences")
    position = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    institute = models.CharField(max_length=200)
    responsibility = models.TextField()

    def __str__(self):
        return f"{self.position} - {self.application.name}"

class SkillModel(models.Model):
    application = models.ForeignKey(PersonalModel, on_delete=models.CASCADE, related_name="skills")
    description = models.TextField()

    def __str__(self):
        return f"Skill - {self.application.name}"

class ReferenceModel(models.Model):
    application = models.ForeignKey(PersonalModel, on_delete=models.CASCADE, related_name="references")
    name = models.CharField(max_length=100)
    contact_info = models.TextField()

    def __str__(self):
        return f"Reference - {self.name}"



