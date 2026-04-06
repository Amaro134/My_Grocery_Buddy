from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# Define the URL patterns for the main app

urlpatterns = [
    path('home/',  views.homePage, name='home'),
    path('', views.landingPage, name='landingpage'), 
    # path('profile', views.profilePage, name='profile')
    path("update-profile/", views.update_profile, name="update_profile"),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)