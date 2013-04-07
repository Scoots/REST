from django.conf.urls import *
import views

urlpatterns = patterns('',
    url(r'^users/(?P<expression>.*)/$', views.GetUser),
    url(r'^battles(?P<expression>.*)$', views.GetBattles),
       (r'^KixeyeAPI/', include('KixeyeWebService.KixeyeAPI.urls')),
)
