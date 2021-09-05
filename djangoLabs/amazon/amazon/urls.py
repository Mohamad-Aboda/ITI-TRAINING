from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    
    path('amazon/', include('products.urls')), 
    path('admin/', admin.site.urls),
]



