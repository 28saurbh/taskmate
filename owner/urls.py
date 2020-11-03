from django.contrib import admin
from django.urls import path, include
from owner import urls, views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('add', views.add, name='add'),
    path('edit_img/<int:id>', views.edit_img, name='edit_img'),
    path('edit_about_img/<int:id>', views.edit_about_img, name= 'about_img'),
    path('edit_skill/<int:id>', views.edit_skill, name= 'edit_skill'),
    path('delete_skill/<int:id>', views.delete_skill, name='delete_skill'),
    path('msg', views.msg, name='msg'),
    path('delete_msg/<int:id>', views.delete_msg, name='delete_msg')
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
