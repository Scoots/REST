from django.conf.urls import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from KixeyeAPI.handlers import CreateUserHandler, UserIdHandler, CreateBattleLogHandler
import views

auth = None #HttpBasicAuthentication(realm="KixeyeRealm")
createUserResource = Resource(CreateUserHandler, authentication=auth)
userIdResource = Resource(UserIdHandler, authentication=auth)
createBattleLogResource = Resource(CreateBattleLogHandler, authentication=auth)

urlpatterns = patterns('',
    url(r'^users/$', createUserResource),
    url(r'^users/(?P<expression>.*)/$', userIdResource),
    url(r'^battles/$', createBattleLogResource),
    url(r'^battles?(?P<expression>.*)$', views.GetBattles),
)
