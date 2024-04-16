from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from django.views.generic import TemplateView, RedirectView

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView, RedirectView

from django.contrib.sitemaps.views import sitemap

from blog.sitemaps import PostSitemap
from courses.views import CourseListView

from django.conf.urls.i18n import i18n_patterns

sitemaps = {
    'posts': PostSitemap,
}


urlpatterns = [
    path('', include('home_page.urls', namespace='home')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),

     # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),  name='password_change_done'),

    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

  
 
    path('all/', CourseListView.as_view(), name='course_list'),

    path('api/', include('courses.api.urls', namespace='api')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('account/', include('account.urls', namespace='accounts')),
    path('accounts/', include('allauth.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('course/', include('courses.urls', namespace='courses')),

    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('team/', include('team.urls', namespace='tasks')),
    path('service/', include('shop.urls', namespace='shop')),

    path('student-pref/',include('studentPreferences.urls', namespace='studentPreference')),
    path('exams/',include('questions.urls', namespace='question')),
 
    path('students/', include('students.urls',  namespace='students')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')

    
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

