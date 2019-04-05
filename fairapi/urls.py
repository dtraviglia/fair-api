"""fairapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from rest_framework import routers
from patientrecord import views as patient_record_views
from user import views as login_views
from auth0login import views as auth_views
from patientrecord import views as patient_record_views

router = routers.DefaultRouter()
router.register(r'user', login_views.UserViewSet),
router.register(r'groups', login_views.GroupViewSet)
router.register(r'patient-record', patient_record_views.PatientRecordViewSet)

urlpatterns = [
    path('', auth_views.index),
    path('', include(router.urls)),
    path('dashboard/', auth_views.dashboard),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]
