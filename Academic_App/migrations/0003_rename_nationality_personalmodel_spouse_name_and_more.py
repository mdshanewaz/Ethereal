# Generated by Django 5.0 on 2025-05-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academic_App', '0002_educationmodel_experiencemodel_personalmodel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalmodel',
            old_name='nationality',
            new_name='spouse_name',
        ),
        migrations.RemoveField(
            model_name='educationmodel',
            name='board_university',
        ),
        migrations.RemoveField(
            model_name='educationmodel',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='educationmodel',
            name='group_subject',
        ),
        migrations.RemoveField(
            model_name='educationmodel',
            name='institute',
        ),
        migrations.RemoveField(
            model_name='educationmodel',
            name='result',
        ),
        migrations.RemoveField(
            model_name='educationmodel',
            name='year',
        ),
        migrations.RemoveField(
            model_name='experiencemodel',
            name='department',
        ),
        migrations.RemoveField(
            model_name='experiencemodel',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='experiencemodel',
            name='institute',
        ),
        migrations.RemoveField(
            model_name='experiencemodel',
            name='position',
        ),
        migrations.RemoveField(
            model_name='experiencemodel',
            name='responsibility',
        ),
        migrations.RemoveField(
            model_name='personalmodel',
            name='spous_name',
        ),
        migrations.RemoveField(
            model_name='referencemodel',
            name='contact_info',
        ),
        migrations.RemoveField(
            model_name='referencemodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='trainingmodel',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='trainingmodel',
            name='institute',
        ),
        migrations.RemoveField(
            model_name='trainingmodel',
            name='result',
        ),
        migrations.RemoveField(
            model_name='trainingmodel',
            name='title',
        ),
        migrations.RemoveField(
            model_name='trainingmodel',
            name='year',
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='bachelor',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='board_faculty_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='board_faculty_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='board_faculty_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='board_faculty_4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='group_subject_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='group_subject_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='group_subject_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='group_subject_4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='hsc',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='institute_1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='institute_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='institute_3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='institute_4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='masters',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='result_1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='result_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='result_3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='result_4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='ssc',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experiencemodel',
            name='department_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='experiencemodel',
            name='department_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='experiencemodel',
            name='duration_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='experiencemodel',
            name='duration_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='experiencemodel',
            name='institute_1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='experiencemodel',
            name='institute_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='experiencemodel',
            name='position_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='experiencemodel',
            name='position_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='experiencemodel',
            name='responsibility_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experiencemodel',
            name='responsibility_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='referencemodel',
            name='contact_info_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='referencemodel',
            name='contact_info_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='referencemodel',
            name='name_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='referencemodel',
            name='name_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trainingmodel',
            name='duration_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='trainingmodel',
            name='duration_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='trainingmodel',
            name='institute_1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='trainingmodel',
            name='institute_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='trainingmodel',
            name='result_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='trainingmodel',
            name='result_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='trainingmodel',
            name='title_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trainingmodel',
            name='title_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trainingmodel',
            name='year_1',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trainingmodel',
            name='year_2',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalmodel',
            name='contact_num_1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='personalmodel',
            name='contact_num_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='personalmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personalmodel',
            name='father_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personalmodel',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='personalmodel',
            name='married',
            field=models.CharField(blank=True, choices=[('married', 'Married'), ('single', 'Single')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='personalmodel',
            name='mother_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personalmodel',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personalmodel',
            name='permanent_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalmodel',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
        migrations.AlterField(
            model_name='personalmodel',
            name='present_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalmodel',
            name='religon',
            field=models.CharField(blank=True, choices=[('Islam', 'Islam'), ('Hinduism', 'Hinduism'), ('Buddhism', 'Buddhism'), ('Christianity', 'Christianity')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personalmodel',
            name='signature',
            field=models.ImageField(blank=True, null=True, upload_to='signature'),
        ),
        migrations.AlterField(
            model_name='skillmodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
