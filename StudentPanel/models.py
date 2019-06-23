from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# change class name in Title


class StudentPersonalDetail(models.Model):

    GENDER = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other', 'other')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=20, choices=GENDER, default='Other')
    uid = models.CharField(max_length=120)
    image = models.ImageField(null=True, upload_to='student')  # Image Upload
    mobile = models.CharField(max_length=11)
    alternate_mobile = models.CharField(max_length=11)
    father_name = models.CharField(max_length=120)
    mother_name = models.CharField(max_length=120)
    temperory_address = models.TextField()
    permanent_address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    is_authrise = models.BooleanField(default=False)
    authrised_by = models.BooleanField(default=False)


class StudentEducationalQualifications(models.Model):

    # highschool Detail
    #  add OnetoOne mapping to StudentPersonalDetail
    studentpersonaldetail = models.OneToOneField(
        StudentPersonalDetail,
        on_delete=models.CASCADE,
        primary_key=True
    )
    high_school_name = models.CharField(max_length=125)
    high_school_board = models.CharField(max_length=25)
    inter_school_name = models.CharField(max_length=25)
    inter_school_board = models.CharField(max_length=25)
    bachlors_collage_name = models.CharField(max_length=25)
    pg_collage_name = models.CharField(max_length=25)
    highschool_grade = models.CharField(max_length=10, default='Null')
    highschool_obtain_marks = models.CharField(max_length=20)
    highschool_max_marks = models.CharField(max_length=20)
    # interschool Detail
    inter_grade = models.CharField(max_length=120, default='Null')
    inter_obtain_marks = models.CharField(max_length=20)
    inter_max_marks = models.CharField(max_length=20)

    # Bachelors Degree
    bachalors_pursuing = models.CharField(
        max_length=20)  # choice field
    bachalors_obtain_marks = models.CharField(max_length=120)
    bachalors_max_marks = models.CharField(max_length=120)
    # pg degree
    pg_pursuing = models.CharField(max_length=20)  # choise field
    pg_obtain_marks = models.CharField(max_length=20)
    pg_total_marks = models.CharField(max_length=20)


class StudentJobApplicationDetail(models.Model):
    # OnetoOne StudentPersonalDetail
    studentpersonaldetail = models.OneToOneField(
        StudentPersonalDetail,
        on_delete=models.CASCADE,
        primary_key=True
    )

    SKILLS = (
        ('SOFTWERE DEVELOPER', 'Softwere Developer'),
        ('HARDWERE DEVELOPER', 'Hardwere Developer'),
        ('WEB DEVELOPER', 'Web Developer'),
        ('CIVIL ENGINEER', 'Civil Engineer'),
    )
    skills = models.CharField(max_length=120, choices=SKILLS)
    achievement = models.CharField(max_length=120)
    resume = models.FileField(null=True, upload_to='stu_resume')
