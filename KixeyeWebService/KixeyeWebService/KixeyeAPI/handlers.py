from piston.handler import BaseHandler
from django.http import HttpResponse
from django.db import connection, transaction
from KixeyeWebService.models import User
import json
from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder

#-----------------------------------------------------------------------
# Handler for when the CreateUser POST is called
#-----------------------------------------------------------------------
class CreateUserHandler(BaseHandler):
  allowed_methods = ('POST', )
  
  #-----------------------------------------------------------------------
  # Create function, called when POST is sent
  #-----------------------------------------------------------------------
  def create(self, request):
    # Creates an initial response and does error checking
    response = HttpResponse("", content_type='application/json')

    first = request.data.get('first')
    if first is None:
      response.write(self.__CreateUserFailureJSON("ERROR_NO_FIRST_NAME"))
      return response

    last = request.data.get('last')
    if last is None:
      response.write(self.__CreateUserFailureJSON("ERROR_NO_LAST_NAME"))
      return response

    nickname = request.data.get('nickname')
    if nickname is None:
      response.write(self.__CreateUserFailureJSON("ERROR_NO_NICKNAME"))
      return response

    # Set to None to keep it in scope
    results = CallSprocFetchOne("kixeye.CreateUser", [first, last, nickname,])

    # If we don't have any rows, error
    if len(results) < 2:
      response.write(self.__CreateUserFailureJSON("ERROR_INVALID_MYSQL_RETURN"))
      return response

    # Otherwise, success!
    response.write(self.__CreateUserSuccessJSON(results[0], results[1]))
    return response

  
  #-----------------------------------------------------------------------
  # Helper function for writing success JSON for the CreateUser call
  #-----------------------------------------------------------------------
  def __CreateUserSuccessJSON(self, userid, time):
    return json.dumps(
                      {
                      'error': "false",
                      'time': time,
                      'userid': userid
                      },
                      sort_keys=True,
                      indent=4,
                      separators=(',',': '))
  
  #-----------------------------------------------------------------------
  # Helper function for writing failure JSON for the CreateUser call
  #-----------------------------------------------------------------------
  def __CreateUserFailureJSON(self, message, time):
    return json.dumps(
                      {
                      'error': "true",
                      'time': datetime.datetime.utcnow(),
                      'msg': message
                      },
                      sort_keys=True,
                      indent=4,
                      separators=(',',': '))
  

#-----------------------------------------------------------------------
# Handler for when ModifyUser POST or GET is called
# I really want the GET in my views.py file
#-----------------------------------------------------------------------
class UserIdHandler(BaseHandler):
  allowed_methods = ('PUT', 'GET')
  
  #-----------------------------------------------------------------------
  # Read is called when GET is sent to this handler
  # This should REALLY be in my views, but I was unable to get my regex to match GET without
  # matching the PUT
  #-----------------------------------------------------------------------
  def read(self, request, expression):
    # Check if the expression is a user id
    userId = TryParseInt(expression)
    if userId is not None:
      # Go digging through the database to find the appropriate set of data to return
      results = CallSprocFetchAll("kixeye.GetUserFromId", [userId,])
      # If we don't have any rows, error
      if len(results) < 1:
        return HttpResponse("No rows returned for params {0}".format([userId,]))
    
      # Only grab the first row
      return HttpResponse(results[0])

    # If it isn't an id, see if we are searching by nickname
    nickname = request.GET.get('nickname')
    if nickname is not None:
      # Go digging through the database to find the appropriate set of data to return
      results = CallSprocFetchAll("kixeye.GetUserFromNickname", [nickname,])

      # If we don't have any rows, error
      if len(results) < 1:
        return HttpResponse("No rows returned for params {0}".format([nickname,]))
    
      # Figure out how to redirect
      # I will need to change my sproc to return the user id instead of all user data
      return HttpResponse(results)

    return HttpResponse("You're not looking at user_id or nickname")

  #-----------------------------------------------------------------------
  # Update is called when PUT is sent to this handler
  #-----------------------------------------------------------------------
  def update(self, request, expression):
    response = HttpResponse()
    response.content_type = 'application/json'

    # Get the id of the person we are modifying
    userId = TryParseInt(expression)
    if userId is None:
      response.write(self.__ModifyUserFailureJSON("ERROR_BAD_USER_ID"))
      return response

    # Get the field that we wish to change, should be the column name
    field = request.data.get('field')
    if field is None:
      response.write(self.__ModifyUserFailureJSON("ERROR_BAD_FIELD"))
      return response

    # Get the value we want the column to be
    value = request.data.get('value')
    if value is None:
      response.write(self.__ModifyUserFailureJSON("ERROR_BAD_VALUE"))
      return response
    
    ## Connect to our database and call the sproc
    if field == "first":
      CallSprocFetchOne("kixeye.ModifyUserFirstName", [userId, value,])
    elif field == "last":
      CallSprocFetchOne("kixeye.ModifyUserLastName", [userId, value,])
    elif field == "nickname":
      CallSprocFetchOne("kixeye.ModifyUserNickname", [userId, value,])
    else:
      # If none of those are the fields, then the user input is bad
      response.write(self.__ModifyUserFailureJSON("ERROR_BAD_FIELD"))
      return response

    # Set response.content to the json
    response.write(self.__ModifyUserSuccessJSON())
    return response
  
  #-----------------------------------------------------------------------
  # Helper function for writing success JSON for the ModifyUser call
  #-----------------------------------------------------------------------
  def __ModifyUserSuccessJSON(self):
    return json.dumps(
                      {
                      'error': "false",
                      'time': datetime.utcnow(),
                      },
                      cls=DjangoJSONEncoder,
                      sort_keys=True,
                      indent=4,
                      separators=(',',': '))
  
  #-----------------------------------------------------------------------
  # Helper function for writing failure JSON for the ModifyUser call
  #-----------------------------------------------------------------------
  def __ModifyUserFailureJSON(self, message):
    return json.dumps(
                      {
                      'error': "true",
                      'time': datetime.utcnow(),
                      'msg': message
                      },
                      cls=DjangoJSONEncoder,
                      sort_keys=True,
                      indent=4,
                      separators=(',',': '))
    
  
#-----------------------------------------------------------------------
# Handler for when the CreateBattleLog POST is called
#-----------------------------------------------------------------------
class CreateBattleLogHandler(BaseHandler):
  allowed_methods = ('POST',)
  
  #-----------------------------------------------------------------------
  # Create is called when POST is sent to this handler
  #-----------------------------------------------------------------------
  def create(self, request):
    response = HttpResponse("", content_type='application/json')

    # Do all of our JSON error checking
    attacker = request.data.get('attacker')
    if attacker is None:
      response.write(self.__AddBattleFailureJSON("ERROR_NO_ATTACKER"))
      return response

    defender = request.data.get('defender')
    if defender is None:
      response.write(self.__AddBattleFailureJSON("ERROR_NO_DEFENDER"))
      return response

    winner = request.data.get('winner')
    if winner is None:
      response.write(self.__AddBattleFailureJSON("ERROR_NO_WINNER"))
      return response

    start = request.data.get('start')
    if start is None:
      response.write(self.__AddBattleFailureJSON("ERROR_NO_START"))
      return response

    startTime = TryParseDatetime(start)
    if start is None:
      response.write(self.__AddBattleFailureJSON("ERROR_BAD_START"))
      return response

    end = request.data.get('end')
    if end is None:
      response.write(self.__AddBattleFailureJSON("ERROR_NO_END"))
      return response

    endTime = TryParseDatetime(end)
    if end is None:
      response.write(self.__AddBattleFailureJSON("ERROR_BAD_END"))
      return response

    # We got passed all our error checking, send the sproc call!
    params = [attacker, defender, winner, startTime, endTime,]
    CallSprocFetchOne("kixeye.AddBattle", params)

    # Set err, time
    response.write(self.__AddBattleSuccessJSON())
    return response
  
  #-----------------------------------------------------------------------
  # Helper function for writing success JSON for the AddBattle call
  #-----------------------------------------------------------------------
  def __AddBattleSuccessJSON(self):
    return json.dumps(
                      {
                      'error': "false",
                      'time': datetime.utcnow(),
                      },
                      cls=DjangoJSONEncoder,
                      sort_keys=True,
                      indent=4,
                      separators=(',',': '))
  
  #-----------------------------------------------------------------------
  # Helper function for writing failure JSON for the AddBattle call
  #-----------------------------------------------------------------------
  def __AddBattleFailureJSON(self, message):
    return json.dumps(
                      {
                      'error': "true",
                      'time': encoder.default(datetime.utcnow()),
                      'msg': message
                      },
                      cls=DjangoJSONEncoder,
                      sort_keys=True,
                      indent=4,
                      separators=(',',': '))
  
#-----------------------------------------------------------------------
# Utility function for pulling out datetime values
#-----------------------------------------------------------------------
def TryParseDatetime(val, default=None):
  try:
    return datetime.strptime(val, "%Y-%m-%d")
  except:
    return default
  
#-----------------------------------------------------------------------
# Utility function for pulling out int values
#-----------------------------------------------------------------------
def TryParseInt(val, base=10, default=None):
  try:
    return int(val, base)
  except:
    return default

#-----------------------------------------------------------------------
# Allows django to commit into our database immediately
#-----------------------------------------------------------------------
@transaction.commit_manually
def CallSprocFetchOne(function, params):
  results = None
  try:
    ## Connect to our database and call the sproc
    cur = connection.cursor()
    cur.callproc(function, params)
    results = cur.fetchone()
    cur.close()
  except:
    transaction.rollback()
    return results
  else:
    transaction.commit()
    return results

#-----------------------------------------------------------------------
# Allows django to commit into our database immediately
#-----------------------------------------------------------------------
@transaction.commit_manually
def CallSprocFetchAll(function, params):
  results = ()
  try:
    ## Connect to our database and call the sproc
    cur = connection.cursor()
    cur.callproc(function, params)
    results = cur.fetchall()
    cur.close()
  except:
    transaction.rollback()
    return results
  else:
    transaction.commit()
    return results
