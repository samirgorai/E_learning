# Generated by Django 4.2.5 on 2024-02-10 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_details',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('student_name', models.CharField(max_length=20)),
                ('student_image', models.ImageField(default='student/student_image_DIR/default.jpg', upload_to='student/student_image_DIR/')),
                ('student_dob', models.DateField()),
                ('student_sex', models.CharField(default='O', max_length=1)),
                ('student_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
