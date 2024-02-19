from rest_framework import serializers

from .models import *


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
        fields = ('id', 'title', 'content', 'course', 'expected_output', 'lesson_nr', 'language')

    def generate_lesson_nr(self, course_instance):
        latest_lesson = Lesson.objects.filter(course=course_instance).order_by('-lesson_nr').first()

        if latest_lesson:
            return latest_lesson.lesson_nr + 1
        else:
            return 1


class LessonSerializerCreate(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    course = serializers.CharField()
    expected_output = serializers.CharField()
    lesson_nr = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        fields = ('title', 'content', 'course', 'expected_output', 'lesson_nr')

    def create(self, validated_data):
        course_instance = Course.objects.get(pk=validated_data['course'])
        validated_data['lesson_nr'] = self.generate_lesson_nr(course_instance)
        lesson_nr = validated_data.get('lesson_nr')
        validated_data['course'] = course_instance

        if lesson_nr is None:
            validated_data['lesson_nr'] = self.generate_lesson_nr(course_instance)

        return Lesson.objects.create(**validated_data)

    def generate_lesson_nr(self, course_instance):
        latest_lesson = Lesson.objects.filter(course=course_instance).order_by('-lesson_nr').first()

        if latest_lesson:
            return latest_lesson.lesson_nr + 1
        else:
            return 1


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
    next_lesson = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = (
            'id', 'title', 'owner', 'language', 'description', 'short_desc', 'url', 'avg_rating', 'count_rating',
            'ratings', 'lessons', 'next_lesson')

    def get_next_lesson(self, obj):
        # Access values from the context
        context = self.context
        additional_value = context.get('next_lesson', None)

        # Add your logic to calculate the next lesson using the additional value
        return additional_value  # Replace this with your actual logic


class CompileSerializer(serializers.Serializer):
    compile_code = serializers.CharField(max_length=10000)
    expected_result = serializers.CharField(max_length=1000)
    language = serializers.CharField(max_length=100)

    class Meta:
        fields = "__all__"
