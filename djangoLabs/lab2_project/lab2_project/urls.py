from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    
    path('amazon/', include('amazon.urls')), 
    path('admin/', admin.site.urls),
]
