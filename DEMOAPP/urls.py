from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about/', views.about_us, name='about'),
    path('submit_task/', views.submit_task, name='submit_task'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('submit_health/', views.submit_health, name='submit_health'),
    path('submit_photo/', views.submit_photo, name='submit_photo')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
