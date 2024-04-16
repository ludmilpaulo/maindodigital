from django.urls import path
from . import views



app_name = 'home_page'

urlpatterns = [
    path('',views.home , name='home_page' ),
    path('about-us/', views.aboutus_list, name='about_us'),
    path('<int:id>/<slug:slug>', views.hire_detail_view, name='hire_detail'),
    path('send/',views.send_email , name='send_email' ),
    path('success/' , views.send_success , name='send_success'),

]