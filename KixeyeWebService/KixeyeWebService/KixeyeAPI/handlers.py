from piston.handler import BaseHandler
from django.http import HttpResponse
import django.db

class CreateUserHandler(BaseHandler):
  allowed_methods = ('POST',)

  def create(self, request):
    # Set params based on the request
    params = None

    # Call SProc to set the appropriate user data
    __CallSproc("kixeye.CreateUser", [params,])

    # I should be try/catching on errors on the call to Sproc
    # to set up the appropriate JSON return values
    return HttpResponse("Set up JSON for return values here")
  
class ModifyUserHandler(BaseHandler):
  allowed_methods = ('PUT',)

  def modify(self, request):
    # Here is where we would get our JSON params for the SProc
    #After we get it we need to do logic to determine which sproc to call
    params = None

    # Get the field that we wish to change, should be the column name
    field = None
    if field == "first_name":
      __CallSproc('kixeye.ModifyUserFirstName', [params,])
      return HttpResponse("Set up JSON for return values here")
    if field == "last_name":
      __CallSproc('kixeye.ModifyUserLastName', [params,])
      return HttpResponse("Set up JSON for return values here")
    if field == "nickname":
      __CallSproc('kixeye.ModifyUserNickname', [params,])
      return HttpResponse("Set up JSON for return values here")
    
    # If none of those are the fields, then the user input is bad
    # Close the connection and return the appropriate error
    return HttpResponse("Set up JSON for return values here")

class CreateBattleLogHandler(BaseHandler):
  allowed_methods = ('POST',)
  
  def create(self, request):
    # Here is where we would get our JSON params for the SProc
    # Need to do error checking on the various pieces to make sure
    # they are formatted correctly
    params = None
    
    __CallSproc('kixeye.AddBattle', [params,])
    return HttpResponse("Set up JSON for return values here")

def __CallSproc(sprocName, params):
  ## Connect to our database and call the sproc
  cur = connection.cursor()
  cur.callproc(sprocName, params)
  cur.close()