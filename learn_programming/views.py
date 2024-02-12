from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict


class UserListView(APIView):

    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class UserView(APIView):

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_200_OK)


class LanguageListView(APIView):
    def get(self, request):
        serializer = LanguageSerializer(Language.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class LanguageView(APIView):
    def get(self, request, pk):
        language = get_object_or_404(Language, pk=pk)
        serializer = LanguageSerializer(instance=language)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        language = get_object_or_404(Language, pk=pk)
        serializer = LanguageSerializer(instance=language, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        language = get_object_or_404(Language, pk=pk)
        language.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseListView(APIView):
    def get(self, request):
        serializer = CourseSerializer(Course.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CourseView(APIView):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializerSingle(instance=course)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(instance=course, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LessonListView(APIView):
    def get(self, request):
        serializer = LessonSerializer(Lesson.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class LessonView(APIView):
    def get(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        serializer = LessonSerializer(instance=lesson)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        serializer = LessonSerializer(instance=lesson, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LessonXUserListView(APIView):
    def get(self, request):
        serializer = LessonXUserSerializer(LessonXUser.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LessonXUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class LessonXUserView(APIView):
    def get(self, request, pk):
        lesson_x_user = get_object_or_404(LessonXUser, pk=pk)
        serializer = LessonXUserSerializer(instance=lesson_x_user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        lesson_x_user = get_object_or_404(LessonXUser, pk=pk)
        serializer = LessonXUserSerializer(instance=lesson_x_user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        lesson_x_user = get_object_or_404(LessonXUser, pk=pk)
        lesson_x_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OpinionListView(APIView):
    def get(self, request):
        serializer = OpinionSerializer(Opinion.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OpinionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class OpinionView(APIView):
    def get(self, request, pk):
        opinion = get_object_or_404(Opinion, pk=pk)
        serializer = OpinionSerializer(instance=opinion)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        opinion = get_object_or_404(Opinion, pk=pk)
        serializer = OpinionSerializer(instance=opinion, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        opinion = get_object_or_404(Opinion, pk=pk)
        opinion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WhoAmI(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
