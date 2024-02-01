from django.db import models

# Create your models here.

class Teacher_details(models.Model):
    teacher_name=models.CharField(max_length=20)
    teacher_image=models.ImageField(upload_to="student/student_image_DIR/",default='teacher/teacher_image_DIR/default.jpg')
    teacher_age=models.DateField()
    teacher_sex=models.CharField(max_length=1,default="O")
    
    def __str__(self) -> str:
        return self.teacher_name
    
    