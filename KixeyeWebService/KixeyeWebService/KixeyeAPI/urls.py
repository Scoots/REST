from django.conf.urls import patterns, include, url
from piston.resource import Resource
from handlers import CreateUserHandler, ModifyUserHandler, CreateBattleLogHandler

createUserResource = Resource(CreateUserHandler)
modifyUserResource = Resource(ModifyUserHandler)
createBattleLogResource = Resource(CreateBattleLogHandler)

urlpatterns = patterns( '',
    url(r'^users/$', createUserResource),
    url(r'^users/(?P<expression>.*)$', modifyUserResource),
    url(r'^battles/(?P<expression>.*)$', createBattleLogResource),
)