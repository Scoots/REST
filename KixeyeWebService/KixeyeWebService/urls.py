from django.conf.urls import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from KixeyeAPI.handlers import CreateUserHandler, UserIdHandler, CreateBattleLogHandler
import views

auth = None #HttpBasicAuthentication(realm="KixeyeRealm")
createUserResource = Resource(CreateUserHandler, authentication=auth)
userIdResource = Resource(UserIdHandler, authentication=auth)
createBattleLogResource = Resource(CreateBattleLogHandler, authentication=auth)

# Puts the patterns necessary for our POST, PUT, and GET requests
# Generally I would like my GETs to go through my view, but I
# added a GET call to the userIdHandler, since it is too similar for my
# regex to differentiate
urlpatterns = patterns('',
    url(r'^users/$', createUserResource),
    url(r'^users/(?P<expression>.*)$', userIdResource),
    url(r'^battles/$', createBattleLogResource),
    url(r'^battles?(?P<expression>.*)$', views.GetBattles),
)
