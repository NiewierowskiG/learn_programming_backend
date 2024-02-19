from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('user/<int:pk>/', UserView.as_view()),
    path('languages/', LanguageListView.as_view()),
    path('language/<int:pk>/', LanguageView.as_view()),
    path('courses/', CourseListView.as_view()),
    path('course/<int:pk>/', CourseView.as_view()),
    path('lessons/', LessonListView.as_view()),
    path('lesson/<int:pk>/', LessonView.as_view()),
    path('lessonxusers/', LessonXUserListView.as_view()),
    path('lessonxuser/<int:pk>/', LessonXUserView.as_view()),
    path('opinions/', OpinionListView.as_view()),
    path('opinion/<int:pk>/', OpinionView.as_view()),
    path('whoami/', WhoAmI.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('compile/', CompileView.as_view()),
    path('nextlesson/<int:id>/', NextLessonView.as_view()),
    path('finishlesson/<int:id>/', FinishLessonView.as_view()),
    path('startcourse/<int:id>/', StartCourseView.as_view()),
    path('usercourses/', UserCoursesStartedView.as_view()),
]
