from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,)
    student_name=models.CharField(max_length=20)
    student_image=models.ImageField(upload_to="student/student_image_DIR/",default='student/student_image_DIR/default.jpg')
    student_dob=models.DateField()
    student_sex=models.CharField(max_length=1,default="O")
    student_email=models.EmailField()
    
    def __str__(self) -> str:
        return self.student_name