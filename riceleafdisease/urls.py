from django.urls import path
from django.conf import settings

from django.conf.urls.static import static


from . import views 

urlpatterns = [
     path('', views.home, name='home'),
     path('login/', views.login_page, name='login_page'),
     path('logout/', views.logoutuser, name='logoutuser'),
     path('signup/', views.signup, name='signup'),
     path('uploadimage/', views.upload_image, name='upload'),
     path('modeltrainign/', views.trainmodel, name='train'),
    
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)