from django.urls import path
from django.views.decorators.cache import cache_page
from .views import VerificationView
from .api import UsernameValidation,EmailValidationView,Cheating
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views
from . import views

app_name = 'students'

urlpatterns = [
    path('register/',
         views.StudentRegistrationView.as_view(),
         name='student_registration'),
    path('enroll-course/',
         views.StudentEnrollCourseView.as_view(),
         name='student_enroll_course'),
    path('courses/',
         views.StudentCourseListView.as_view(),
         name='student_course_list'),
    path('course/<pk>/',
         cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
         name='student_course_detail'),
    path('course/<pk>/<module_id>/',
         cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
         name='student_course_detail_module'),

    path('username-validate',UsernameValidation.as_view(),name="username-validate"),
    path('cheat/<str:professorname>',Cheating.as_view(),name="cheat"),
    path('email-validate',EmailValidationView.as_view(),name="email-validate"),
    path('activate/<uidb64>/<token>',VerificationView.as_view(),name = 'activate'),


    
]
