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

    name = models.CharField(max_length=100, null=True, blank=True)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    permanent_address = models.TextField(null=True, blank=True)
    present_address = models.TextField(null=True, blank=True)
    contact_num_1 = models.CharField(max_length=20, null=True, blank=True)
    contact_num_2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    married = models.CharField(max_length=10, null=True, blank=True, choices=MARITAL_CHOICES)
    spouse_name = models.CharField(max_length=100, blank=True, null=True)
    religon = models.CharField(max_length=100, null=True, blank=True, choices=CATEGORY_CHOICES)
    # nationality = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=6, null=True, choices=GENDER_CHOICES, blank=True)
    photo = models.ImageField(upload_to='photo', blank=True, null=True)
    signature = models.ImageField(upload_to='signature', blank=True, null=True)

    def __str__(self):
        return self.name

class EducationModel(models.Model):
    application = models.ForeignKey(PersonalModel, on_delete=models.CASCADE, related_name="educations")
    masters = models.PositiveIntegerField(null=True, blank=True)
    result_1 = models.CharField(max_length=20, null=True, blank=True)
    group_subject_1 = models.CharField(max_length=100, null=True, blank=True)
    board_faculty_1 = models.CharField(max_length=100, null=True, blank=True)
    institute_1 = models.CharField(max_length=200, null=True, blank=True)
    bachelor = models.PositiveIntegerField(null=True, blank=True)
    result_2 = models.CharField(max_length=20, null=True, blank=True)
    group_subject_2 = models.CharField(max_length=100, null=True, blank=True)
    board_faculty_2 = models.CharField(max_length=100, null=True, blank=True)
    institute_2 = models.CharField(max_length=200, null=True, blank=True)
    hsc = models.PositiveIntegerField(null=True, blank=True)
    result_3 = models.CharField(max_length=20, null=True, blank=True)
    group_subject_3 = models.CharField(max_length=100, null=True, blank=True)
    board_faculty_3 = models.CharField(max_length=100, null=True, blank=True)
    institute_3 = models.CharField(max_length=200, null=True, blank=True)
    ssc = models.PositiveIntegerField(null=True, blank=True)
    result_4 = models.CharField(max_length=20, null=True, blank=True)
    group_subject_4 = models.CharField(max_length=100, null=True, blank=True)
    institute_4 = models.CharField(max_length=200, null=True, blank=True)
    board_faculty_4 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.application.name}"

class TrainingModel(models.Model):
    application = models.ForeignKey(PersonalModel, on_delete=models.CASCADE, related_name="trainings")
    title_1 = models.CharField(max_length=100, null=True, blank=True)
    year_1 = models.PositiveIntegerField(null=True, blank=True)
    result_1 = models.CharField(max_length=50, null=True, blank=True)
    duration_1 = models.CharField(max_length=50, null=True, blank=True)
    institute_1 = models.CharField(max_length=200, null=True, blank=True)
    title_2 = models.CharField(max_length=100, null=True, blank=True)
    year_2 = models.PositiveIntegerField(null=True, blank=True)
    result_2 = models.CharField(max_length=50, null=True, blank=True)
    duration_2 = models.CharField(max_length=50, null=True, blank=True)
    institute_2 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.application.name}"

class ExperienceModel(models.Model):
    application = models.ForeignKey(PersonalModel, on_delete=models.CASCADE, related_name="experiences")
    position_1 = models.CharField(max_length=100, null=True, blank=True)
    duration_1 = models.CharField(max_length=50, null=True, blank=True)
    department_1 = models.CharField(max_length=100, null=True, blank=True)
    institute_1 = models.CharField(max_length=200, null=True, blank=True)
    responsibility_1 = models.TextField(null=True, blank=True)
    position_2 = models.CharField(max_length=100, null=True, blank=True)
    duration_2 = models.CharField(max_length=50, null=True, blank=True)
    department_2 = models.CharField(max_length=100, null=True, blank=True)
    institute_2 = models.CharField(max_length=200, null=True, blank=True)
    responsibility_2 = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.application.name}"

class SkillModel(models.Model):
    application = models.ForeignKey(PersonalModel, on_delete=models.CASCADE, related_name="skills")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Skill - {self.application.name}"

class ReferenceModel(models.Model):
    application = models.ForeignKey(PersonalModel, on_delete=models.CASCADE, related_name="references")
    name_1 = models.CharField(max_length=100, null=True, blank=True)
    contact_info_1 = models.TextField(null=True, blank=True)
    name_2 = models.CharField(max_length=100, null=True, blank=True)
    contact_info_2 = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Reference - {self.application.name}"