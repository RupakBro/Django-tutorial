"""MySite04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('app1_0.urls')),
    path('app1_1/', include('app1_1.urls')),
    path('app2_1/', include('app2_1.urls')),
    path('app2_2/', include('app2_2.urls')),
    path('app3_1/', include('app3_1.urls')),
    path('app4_1/', include('app4_1.urls')),
    path('app4_2/', include('app4_2.urls')),
    path('app5_1/', include('app5_1.urls')),
    path('app6_1/', include('app6_1.urls')),
    path('app7_1/', include('app7_1.urls')),
    path('app8_1/', include('app8_1.urls')),
    path('app9_1/', include('app9_1.urls')),
    path('app9_2/', include('app9_2.urls')),
    path('app9_3/', include('app9_3.urls')),
    path('app9_4/', include('app9_4.urls')),
    path('app10_1/', include('app10_1.urls')),
    path('app11_1/', include('app11_1.urls')),
    path('app12_1/', include('app12_1.urls')),
    path('app12_2/', include('app12_2.urls')),
    path('app13_1/', include('app13_1.urls')),
    path('app14_1/', include('app14_1.urls')),
    path('app15_1/', include('app15_1.urls')),
    path('app16_1/', include('app16_1.urls')),
    path('app16_2/', include('app16_2.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)