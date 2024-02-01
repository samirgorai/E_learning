from django.db import models

# Create your models here.

class Student_details(models.Model):
    student_name=models.CharField(max_length=20)
    student_image=models.ImageField(upload_to="student/student_image_DIR/",default='student/student_image_DIR/default.jpg')
    student_age=models.DateField()
    student_sex=models.CharField(max_length=1,default="O")
    
    def __str__(self) -> str:
        return self.student_name