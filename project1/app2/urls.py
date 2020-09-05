"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from app2 import views 

urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('test/',views.view_test),
#    path('good/',views.view_good,name='good'),
	#Act/Deact page
    path('control/light',views.control_light,name='control_light'),
    path('control/circulator',views.control_circulator,name='control_circulator'),
    path('control/aircon',views.control_aircon,name='control_aircon'),
]
