from typing import Tuple
from django.db import models
from django.core.files.base import ContentFile
from django.contrib.auth.models import AbstractUser

from PIL import Image
from io import BytesIO

from django.db.models.fields.files import FieldFile
from django.forms.fields import FileField


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(null=True, default=None, blank=True)

    def save(self, *args, **kwargs):
        if bool(self.image) == True:
            self._process_img()

        super().save(*args, **kwargs)

    def _make_square(self, img):
        min_size = 128
        fill_color = (1, 1, 1)
        x, y = img.size
        size = max(min_size, x, y)
        new_im = Image.new('RGB', (size, size), fill_color)
        new_im.paste(img, (int((size - x) / 2), int((size - y) / 2)))
        return new_im

    def _process_img(self):
        pil_img = Image.open(self.image)
        pil_img = self._make_square(pil_img)

        f = BytesIO()
        try:
            pil_img.save(f, format='JPEG')
            self.image = ContentFile(f.getvalue(), self.image.name)
        finally:
            f.close()


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    members = models.ManyToManyField(User, related_name='head')
    head = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Task(models.Model):

    choices = [
        ('TODO',  'To do'),
        ('DOING',  'In Progress'),
        ('DONE',  'Done'),
    ]

    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateField(auto_now=True, null=False)
    due_on = models.DateField(null=True, default=None)
    department = models.ManyToManyField(Department)
    state = models.CharField(
        max_length=16, choices=choices, default='TODO', null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    assignee = models.ForeignKey(
        User, related_name='+', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class DepartmentFile(models.Model):
    file = models.FileField()
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, blank=True, null=True)
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, blank=True, null=True)
    uploader = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    upload_date = models.DateField(auto_now=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.file.name
