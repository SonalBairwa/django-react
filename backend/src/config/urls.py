
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    url('^api/', include(('articles.api.urls', 'articles'), namespace='articles'))

]
