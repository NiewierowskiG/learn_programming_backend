from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Course, Lesson, Language, LessonXUser, Opinion

class UserTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_user_list(self):
        url = '/api/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        url = '/api/users/'
        data = {'username': 'newuser', 'password': 'newpassword', 'email': 'test@test.com', 'password2': 'newpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_user_model().objects.count(), 2)


class LanguageTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.language = Language.objects.create(name='Python')

    def test_language_list(self):
        url = '/api/languages/'
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_language(self):
        url = '/api/languages/'
        self.client.force_authenticate(user=self.user)
        data = {'name': 'Python'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Language.objects.count(), 2)


class CourseTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.language = Language.objects.create(name='Python')
        self.course = Course.objects.create(title='Test Course', owner=self.user, language=self.language, description='Course Description', short_desc='Short Description', url='http://example.com')

    def test_course_list(self):
        url = '/api/courses/'
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        url = '/api/courses/'
        self.client.force_authenticate(user=self.user)
        data = {'title': 'New Course', 'owner': self.user.id, 'language': self.language.id, 'description': 'New Course Description', 'short_desc': 'New Short Description', 'url': 'http://newexample.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 2)

    def test_update_course(self):
        url = f'/api/course/{self.course.id}/'
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Updated Course', 'owner': self.user.id, 'language': self.language.id, 'description': 'Updated Course Description', 'short_desc': 'Updated Short Description', 'url': 'http://updatedexample.com'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.course.refresh_from_db()
        self.assertEqual(self.course.title, 'Updated Course')

    def test_delete_course(self):
        url = f'/api/course/{self.course.id}/'
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)

class LessonTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.language = Language.objects.create(name='Python')
        self.course = Course.objects.create(title='Test Course', owner=self.user, language=self.language, description='Course Description', short_desc='Short Description', url='http://example.com')
        self.lesson = Lesson.objects.create(title='Test Lesson', content='Lesson Content', course=self.course, expected_output='Expected Output', lesson_nr=1)

    def test_lesson_list(self):
        url = '/api/lessons/'
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_lesson(self):
        url = '/api/lessons/'
        self.client.force_authenticate(user=self.user)
        data = {'title': 'New Lesson', 'content': 'New Lesson Content', 'course': self.course.id, 'expected_output': 'New Expected Output', 'lesson_nr': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 2)

    def test_get_lesson(self):
        url = f'/api/lesson/{self.lesson.id}/'
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lesson(self):
        url = f'/api/lesson/{self.lesson.id}/'
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Updated Lesson', 'content': 'Updated Lesson Content', 'course': self.course.id, 'expected_output': 'Updated Expected Output', 'lesson_nr': 1}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, 'Updated Lesson')

    def test_delete_lesson(self):
        url = f'/api/lesson/{self.lesson.id}/'
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.count(), 0)