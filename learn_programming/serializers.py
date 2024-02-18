from rest_framework import serializers

from .models import *
from secrets import compare_digest


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        password = attrs['password']
        password2 = attrs['password2']
        if str(password) != str(password2):
            raise serializers.ValidationError("Password and Confirm Password Does not match")
        attrs.pop('password2')
        return attrs

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'email', 'bio')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'owner', 'language', 'description', 'short_desc', 'url', 'avg_rating', 'count_rating')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'content', 'course', 'expected_output', 'lesson_nr')


class LessonXUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonXUser
        fields = ('id', 'user', 'lesson', 'finished')


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ('id', 'course', 'user', 'text', 'rating')


class CourseSerializerSingle(serializers.ModelSerializer):
    ratings = OpinionSerializer(many=True, read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            'id', 'title', 'owner', 'language', 'description', 'short_desc', 'url', 'avg_rating', 'count_rating',
            'ratings', 'lessons')
