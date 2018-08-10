from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView


admin.autodiscover()


urlpatterns = [ 
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='tables/')),
    url(r'', include('testapp.urls')),
]