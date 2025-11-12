from django.contrib import admin
from academic_app.models import PersonalModel, EducationModel, TrainingModel, ExperienceModel, SkillModel, ReferenceModel

# Register your models here.

admin.site.register(PersonalModel)
admin.site.register(EducationModel)
admin.site.register(TrainingModel)
admin.site.register(ExperienceModel)
admin.site.register(SkillModel)
admin.site.register(ReferenceModel)
