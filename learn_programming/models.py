from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg


class User(AbstractUser):
    bio = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()


class Language(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)


class Course(models.Model):
    title = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    language = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    short_desc = models.CharField(max_length=150, null=False)
    url = models.CharField(max_length=255, null=True)

    @property
    def avg_rating(self):
        return Opinion.objects.filter(course_id=self.id).aggregate(Avg('rating'))['rating__avg']

    @property
    def count_rating(self):
        return len(Opinion.objects.filter(course_id=self.id))

    @property
    def ratings(self):
        return Opinion.objects.filter(course_id=self.id)

    @property
    def lessons(self):
        return Lesson.objects.filter(course_id=self.id)


class Lesson(models.Model):
    title = models.CharField(max_length=255, null=False)
    content = models.TextField(null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    expected_output = models.TextField(null=False)
    lesson_nr = models.SmallIntegerField()

    class Meta:
        unique_together = ('course', 'lesson_nr')


class LessonXUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    finished = models.BooleanField()

    class Meta:
        unique_together = ('user', 'lesson')


class Opinion(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.SmallIntegerField(

    )

    class Meta:
        unique_together = ('user', 'course')

