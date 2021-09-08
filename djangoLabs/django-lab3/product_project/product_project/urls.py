
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('products/', include('product_app.urls')), 
    path('admin/', admin.site.urls),
]
