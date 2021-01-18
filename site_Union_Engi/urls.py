from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('articles/', include('articles.urls')),
    path('passage/', include('passage.urls')),
    path('documentation/', include('documentation.urls')),
    path('contacts/', include('contacts.urls')),
    path('send/', include('send.urls'))
]
