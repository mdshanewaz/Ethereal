from django.db import models

# Create your models here.

performance_scale  = (
        ('Exceeding Expectations', 'E'),
        ('Meeting Expectations', 'M'),
        ('Approching Expectations', 'A'),
    )

class StudentModel(models.Model):
    grade = (
        ('Nursery', 'Nursery'),
        ('Lower KG', 'Lower KG'),
        ('Upper KG', 'Upper KG'),
    )

    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_class = models.CharField(choices=grade, max_length=20)
    student_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.student_id

class EnglishliteracyModel(models.Model):
    student_name = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name="English_Literacy")
    class_test_1 = models.IntegerField(null=True, blank=True)
    class_test_2 = models.IntegerField(null=True, blank=True)
    semester_examination = models.IntegerField(null=True, blank=True)
    total_mark =  models.IntegerField(null=True, blank=True)
    grade = models.CharField(max_length=10, null=True, blank=True)
    phonics = models.CharField(choices=performance_scale, max_length=50)
    vocabulary = models.CharField(choices=performance_scale, max_length=50)
    reading = models.CharField(choices=performance_scale, max_length=50)
    writing = models.CharField(choices=performance_scale, max_length=50)

    def __str__(self):
        return f"English Literacy marks of {self.student_name.student_name}"
    
    def save(self, *args, **kwargs):
        self.total_mark = self.class_test_1 + self.class_test_2 + self.semester_examination

        if self.total_mark >= 90:
            self.grade = "*A"
        elif self.total_mark >= 80 and self.total_mark < 89:
            self.grade = "A"
        elif self.total_mark >= 70 and self.total_mark <79:
            self.grade = "B"
        elif self.total_mark >= 60 and self.total_mark <69:
            self.grade = "C"
        elif self.total_mark >= 50 and self.total_mark <59:
            self.grade = "D"
        elif self.total_mark >= 40 and self.total_mark <49:
            self.grade = "E"
        else:
            self.grade = "U"

        super().save(*args, **kwargs)
    
class NumeracyModel(models.Model):
    student_name = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name="Numeracy")
    class_test_1 = models.IntegerField(null=True, blank=True)
    class_test_2 = models.IntegerField(null=True, blank=True)
    semester_examination = models.IntegerField(null=True, blank=True)
    total_mark =  models.IntegerField(null=True, blank=True)
    counting = models.CharField(choices=performance_scale, max_length=50)
    arithmetic = models.CharField(choices=performance_scale, max_length=50)
    shapes = models.CharField(choices=performance_scale, max_length=50)
    measurment = models.CharField(choices=performance_scale, max_length=50)

    def __str__(self):
        return f"Numeracy marks of {self.student_name.student_name}"
    
    def save(self, *args, **kwargs):
        self.total_mark = self.class_test_1 + self.class_test_2 + self.semester_examination

        super().save(*args, **kwargs)
    
class AwarenessModel(models.Model):
    student_name = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name="Awareness_Skill")
    class_test_1 = models.IntegerField(null=True, blank=True)
    class_test_2 = models.IntegerField(null=True, blank=True)
    semester_examination = models.IntegerField(null=True, blank=True)
    total_mark =  models.IntegerField(null=True, blank=True)
    health = models.CharField(choices=performance_scale, max_length=50)
    social = models.CharField(choices=performance_scale, max_length=50)
    safety = models.CharField(choices=performance_scale, max_length=50)
    mindfulness = models.CharField(choices=performance_scale, max_length=50)

    def __str__(self):
        return f"Awareness Skill & Wellness marks of {self.student_name.student_name}"
    
    def save(self, *args, **kwargs):
        self.total_mark = self.class_test_1 + self.class_test_2 + self.semester_examination

        super().save(*args, **kwargs)

class BengaliliteracyModel(models.Model):
    student_name = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name="Bengali_Literacy")
    class_test_1 = models.IntegerField(null=True, blank=True)
    class_test_2 = models.IntegerField(null=True, blank=True)
    semester_examination = models.IntegerField(null=True, blank=True)
    total_mark =  models.IntegerField(null=True, blank=True)
    phonics = models.CharField(choices=performance_scale, max_length=50)
    vocabulary = models.CharField(choices=performance_scale, max_length=50)
    reading = models.CharField(choices=performance_scale, max_length=50)
    writing = models.CharField(choices=performance_scale, max_length=50)

    def __str__(self):
        return f"Bengali Literacy marks of {self.student_name.student_name}"
    
    def save(self, *args, **kwargs):
        self.total_mark = self.class_test_1 + self.class_test_2 + self.semester_examination

        super().save(*args, **kwargs)

class QuranModel(models.Model):
    student_name = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name="Quran_and_Tarbiyah")
    class_test_1 = models.IntegerField(null=True, blank=True)
    class_test_2 = models.IntegerField(null=True, blank=True)
    semester_examination = models.IntegerField(null=True, blank=True)
    total_mark =  models.IntegerField(null=True, blank=True)
    phonics = models.CharField(choices=performance_scale, max_length=50)
    writing = models.CharField(choices=performance_scale, max_length=50)
    memorizing = models.CharField(choices=performance_scale, max_length=50)

    def __str__(self):
        return f"Quran and Tarbiyah marks of {self.student_name.student_name}"
    
    def save(self, *args, **kwargs):
        self.total_mark = self.class_test_1 + self.class_test_2 + self.semester_examination

        super().save(*args, **kwargs)
    
class ArtModel(models.Model):
    student_name = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name="Art")
    class_test_1 = models.IntegerField(null=True, blank=True)
    class_test_2 = models.IntegerField(null=True, blank=True)
    semester_examination = models.IntegerField(null=True, blank=True)
    total_mark =  models.IntegerField(null=True, blank=True)
    creativity = models.CharField(choices=performance_scale, max_length=50)
    artistic = models.CharField(choices=performance_scale, max_length=50)
    craftsmanship = models.CharField(choices=performance_scale, max_length=50)

    def __str__(self):
        return f"Art and Craft marks of {self.student_name.student_name}"
    
    def save(self, *args, **kwargs):
        self.total_mark = self.class_test_1 + self.class_test_2 + self.semester_examination

        super().save(*args, **kwargs)

class ExtracurricularModel(models.Model):
    student_name = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name="Extra_Curricular")
    class_test_1 = models.IntegerField(null=True, blank=True)
    class_test_2 = models.IntegerField(null=True, blank=True)
    semester_examination = models.IntegerField(null=True, blank=True)
    total_mark =  models.IntegerField(null=True, blank=True)
    participation = models.CharField(choices=performance_scale, max_length=50)
    teamwork = models.CharField(choices=performance_scale, max_length=50)

    def __str__(self):
        return f"Extra_Curricular marks of {self.student_name.student_name}"
    
    def save(self, *args, **kwargs):
        self.total_mark = self.class_test_1 + self.class_test_2 + self.semester_examination

        super().save(*args, **kwargs)

class PhysicaleducationModel(models.Model):
    student_name = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name="Physical_Education")
    class_test_1 = models.IntegerField(null=True, blank=True)
    class_test_2 = models.IntegerField(null=True, blank=True)
    semester_examination = models.IntegerField(null=True, blank=True)
    total_mark =  models.IntegerField(null=True, blank=True)
    motor_skills = models.CharField(choices=performance_scale, max_length=50)

    def __str__(self):
        return f"Physical Education marks of {self.student_name.student_name}"
    
    def save(self, *args, **kwargs):
        self.total_mark = self.class_test_1 + self.class_test_2 + self.semester_examination

        super().save(*args, **kwargs)
    
class HolisticModel(models.Model):
    evaluation_scale  = (
        ('Satisfied', 'S'),
        ('Progressive', 'P'),
        ('Needs Improvement', 'NI'),
    )

    student_name = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name="Holostic_Evaluation")
    communication = models.CharField(choices=evaluation_scale, max_length=50)
    assignment_completion = models.CharField(choices=evaluation_scale, max_length=50)
    behavior_with_teachers = models.CharField(choices=evaluation_scale, max_length=50)
    behavior_classmates = models.CharField(choices=evaluation_scale, max_length=50)
    discipline = models.CharField(choices=evaluation_scale, max_length=50)
    collaboration = models.CharField(choices=evaluation_scale, max_length=50)
    problem_solving = models.CharField(choices=evaluation_scale, max_length=50)
    organizational_skills = models.CharField(choices=evaluation_scale, max_length=50)
    prayer = models.CharField(choices=evaluation_scale, max_length=50)
    moral_values = models.CharField(choices=evaluation_scale, max_length=50)
    hygiene = models.CharField(choices=evaluation_scale, max_length=50)

class PunctualityModel(models.Model):
    student_name = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name="Attendance")
    total_class = models.IntegerField(null=True, blank=True)
    present = models.IntegerField(null=True, blank=True)
    present_percent = models.FloatField(null=True, blank=True)
    absent = models.IntegerField(null=True, blank=True)
    absent_percent = models.FloatField(null=True, blank=True)
    late = models.IntegerField(null=True, blank=True)
    late_percent = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Attendance {self.student_name.student_name}"
    
    def save(self, *args, **kwargs):
        # Calculate absent only if total_class and present are provided
        if self.total_class is not None and self.present is not None:
            late_count = self.late or 0  # handle None case
            self.absent = self.total_class - self.present
            # Ensure absent doesn't go negative
            if self.absent < 0:
                self.absent = 0

            self.present_percent = (self.present/self.total_class)*100

            self.late_percent = 100-self.present_percent

            self.late_percent = (self.late/self.total_class)*100

        super().save(*args, **kwargs)

class CommentModel(models.Model):
    student_name = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name="Teacher_Comments")
    comment = models.TextField()

    def __str__(self):
        return f"Comment for {self.student_name.student_name}"