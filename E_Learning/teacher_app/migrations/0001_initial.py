# Generated by Django 4.2.5 on 2024-02-02 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=20)),
                ('teacher_image', models.ImageField(default='teacher/teacher_image_DIR/default.jpg', upload_to='student/student_image_DIR/')),
                ('teacher_age', models.DateField()),
                ('teacher_sex', models.CharField(default='O', max_length=1)),
            ],
        ),
    ]