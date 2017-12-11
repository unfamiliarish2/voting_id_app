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

# Text to put at the end of each page's <title>.
admin.site.site_title = 'Lift Up Democracy'

# Text to put in each page's <h1> (and above login form).
admin.site.site_header = admin.site.site_title + ' Admin'

# Text to put at the top of the admin index page.
admin.site.index_title = admin.site.site_header

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
    
    url(r'^thank_you', views.thankYou, name="thankYou"),

    url(r'^demographics$', views.getDemographicForm, name="getDemographicForm"),
    url(r'^demographics_post$', views.submitDemographicInfo, name="submitDemographicInfo"),

]
