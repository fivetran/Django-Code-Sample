"""vandelay_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from vandelay_app import views
# from theme import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.redirect_to_index,name="redirect_to_index"),
    path('pbf/',views.index,name="index"),
    path('tailwind/',views.tailwind,name="tailwind"),
    # path('tw_demo/',views.twindex,name="twindex"),
    path('pbf/connect-card/',views.connect_card_process,name="index"),
    path('pbf/close/',views.close,name="close"),
    path('pbf_reset/',views.reset,name="reset"),
]
