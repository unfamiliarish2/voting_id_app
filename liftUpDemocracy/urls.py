"""liftUpDemocracy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from publicSite import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('allauth.urls')),

    url(r'^helper$', views.getHelperForm, name="getHelperForm"),
    url(r'^helper_post$', views.submitHelperInfo, name="submitHelperInfo"),

    url(r'^helpee$', views.getHelpeeForm, name="getHelpeeForm"),
    url(r'^helpee_post$', views.submitHelpeeInfo, name="submitHelpeeInfo"),

    url(r'^location$', views.getLocationForm, name="getLocationForm"),
    url(r'^location_post', views.submitLocationInfo, name="submitLocationInfo"),

    url(r'^demographics$', views.getDemographicForm, name="getDemographicForm"),
    url(r'^demographics_post$', views.submitDemographicInfo, name="submitDemographicInfo"),

]
