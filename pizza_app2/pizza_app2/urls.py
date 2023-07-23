from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pizza_app2.common.urls')),
    path('accounts/', include('pizza_app2.accounts.urls')),
    path('products/', include('pizza_app2.products.urls')),
]
