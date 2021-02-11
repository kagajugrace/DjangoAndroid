from  django.urls import path 
from  .views import * 
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('', views.welcome, name=''),
    # path('post-data/', views.posts,name='post'),
    path('pharmacy/',views.pharmacy,name='pharmacy'),
    path('medicine/',views.medicine,name='medicine'),
    path('kipharma/',views.kipharma,name='kipharma'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)