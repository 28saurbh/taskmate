from django.contrib import admin
from django.urls import path, include
from home_app import urls, views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='welcome'),
    path('login', auth_view.LoginView.as_view(template_name='login.html'), name = 'login'),

]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
