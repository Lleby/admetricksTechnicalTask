from django.contrib import admin
from django.urls import path
from instagramProfile.views import InstagramScraperViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_instagram_profiles/', InstagramScraperViewSet.add_user_profile),
]
