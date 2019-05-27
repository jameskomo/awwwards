from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('home/', views.home, name='wowawards-home'),
    path('profile/', views.home, name='wowawards-profile'),
    path('new_post/', views.new_post, name='wowawards-new-post'),
    url(r'^search/', views.search_image, name='images-search'),
    url(r'^api/projects/$', views.ProjectsList.as_view()),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
    url(r'^search/', views.search_results, name='search_results'),
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)