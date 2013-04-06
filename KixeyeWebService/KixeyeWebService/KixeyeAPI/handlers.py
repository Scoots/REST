from piston.handler import BaseHandler
from django.http import HttpResponse
import django.db

class CreateUserHandler(BaseHandler):
  allowed_methods = ('POST',)
  # Set model here
  def read(self, request, user_id):
    # Call SProc to set the appropriate user data
    cur = django.db.connections['default'].cursor()

    # Here is where we would get our JSON params for the SProc
    params = None
    cur.callproc('CreateUser', [params,])
    results = cur.fetchall()
    cur.close()
    return HttpResponse("Set up JSON for return values here")
  
class ModifyUserHandler(BaseHandler):
  allowed_methods = ('PUT',)

  def read(self, request, user_id):
    # Call SProc to set the appropriate user data
    cur = django.db.connections['default'].cursor()

    # Here is where we would get our JSON params for the SProc
    #After we get it we need to do logic to determine which sproc to call
    params = None

    # Get the field that we wish to change, should be the column name
    field = None
    if field == "first_name":
      cur.callproc('ModifyUserFirstName', [params,])
      results = cur.fetchall()
      cur.close()
      return HttpResponse("Set up JSON for return values here")
    if field == "last_name":
      cur.callproc('ModifyUserLastName', [params,])
      results = cur.fetchall()
      cur.close()
      return HttpResponse("Set up JSON for return values here")
    if field == "nickname":
      cur.callproc('ModifyUserNickname', [params,])
      results = cur.fetchall()
      cur.close()
      return HttpResponse("Set up JSON for return values here")
    
    # If none of those are the fields, then the user input is bad
    # Close the connection and return the appropriate error
    cur.close()
    return HttpResponse("Set up JSON for return values here")

class CreateBattleLogHandler(BaseHandler):
  allowed_methods = ('POST',)
  
  def read(self, request, user_id):
    # Call SProc to set the appropriate user data
    cur = django.db.connections['default'].cursor()

    # Here is where we would get our JSON params for the SProc
    # Need to do error checking on the various pieces to make sure
    # they are formatted correctly
    params = None
    
    cur.callproc('AddBattle', [params,])
    results = cur.fetchall()
    cur.close()
    return HttpResponse("Set up JSON for return values here")

# Utility function for pulling out int values
def __TryParseInt(val, base=10, default=None):
  try:
    return int(val, base)
  except ValueError:
    return default