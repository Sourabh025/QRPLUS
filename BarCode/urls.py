"""BarCode URL Configuration

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
from scan import camera
from django.contrib import admin
from django.urls import path
from scan import views as v
from django.http import StreamingHttpResponse
from camera import gen,VideoCamera

urlpatterns = [

    path('admin/', admin.site.urls),
    path('scan/',v.scan,name="scan"),
    path('home/',v.home),
     path('monitor/', lambda r: StreamingHttpResponse(gen(VideoCamera()),
                                                     content_type='multipart/x-mixed-replace; boundary=frame')),

]
