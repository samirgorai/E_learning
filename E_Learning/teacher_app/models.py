from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Teacher_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,)
    teacher_name=models.CharField(max_length=20)
    teacher_image=models.ImageField(upload_to="student/student_image_DIR/",default='teacher/teacher_image_DIR/default.jpg')
    teacher_age=models.DateField()
    teacher_sex=models.CharField(max_length=1,default="O")
    teacher_email=models.EmailField()
    
    def __str__(self) -> str:
        return self.teacher_name
    
    