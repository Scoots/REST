from django.conf.urls import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from handlers import CreateUserHandler, ModifyUserHandler, CreateBattleLogHandler

auth = HttpBasicAuthentication(realm="KixeyeRealm")
createUserResource = Resource(CreateUserHandler, authentication=auth)
modifyUserResource = Resource(ModifyUserHandler, authentication=auth)
createBattleLogResource = Resource(CreateBattleLogHandler, authentication=auth)

urlpatterns = patterns( '',
    url(r'^users/$', createUserResource),
    url(r'^users/(?P<expression>.*)$', modifyUserResource),
    url(r'^battles/(?P<expression>.*)$', createBattleLogResource),
)