from piston.handler import BaseHandler
from django.http import HttpResponse
from django.db import connection
from KixeyeWebService.models import User
import json
from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder

class CreateUserHandler(BaseHandler):
  allowed_methods = ('POST',)

  def create(self, request):
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
      # Set err, time, message
      response.write(self.__CreateUserFailureJSON("ERROR_NO_NICKNAME"))
      return response

    ## Connect to our database and call the sproc
    cur = connection.cursor()
    cur.callproc("kixeye.CreateUser", [first, last, nickname,])
    results = cur.fetchone()
    cur.close()

    # If we don't have any rows, error
    if len(results) < 2:
      response.write(self.__CreateUserFailureJSON("ERROR_INVALID_MYSQL_RETURN"))
      return response

    # Set err, time, userid
    response.write(self.__CreateUserSuccessJSON(results[0], results[1]))
    return response

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

class ModifyUserHandler(BaseHandler):
  allowed_methods = ('PUT',)

  def modify(self, request, expression):
    response = HttpResponse()
    response.content_type = 'application/json'

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

    cur = connection.cursor()
    if field == "first_name":
      cur.callproc("kixeye.ModifyUserFirstName", [value,])
      cur.close()
    elif field == "last_name":
      cur.callproc("kixeye.ModifyUserLastName", [value,])
      cur.close()
    elif field == "nickname":
      cur.callproc("kixeye.ModifyUserNickname", [value,])
      cur.close()
    else:
      cur.close()
      # If none of those are the fields, then the user input is bad
      # Need to return a failure JSON response
      # Set response.content to the json
      response.write(self.__ModifyUserFailureJSON("ERROR_BAD_FIELD"))
      return response

    # Set response.content to the json
    response.write(self.__ModifyUserSuccessJSON())
    return response

  def __ModifyUserSuccessJSON(self):
    return json.dumps(
                      {
                      'error': "false",
                      'time': datetime.utcnow(),
                      },
                      cls=DatetimeEncoder,
                      sort_keys=True,
                      indent=4,
                      separators=(',',': '))

  def __ModifyUserFailureJSON(self, message):
    return json.dumps(
                      {
                      'error': "true",
                      'time': datetime.utcnow(),
                      'msg': message
                      },
                      cls=DatetimeEncoder,
                      sort_keys=True,
                      indent=4,
                      separators=(',',': '))
    

class CreateBattleLogHandler(BaseHandler):
  allowed_methods = ('POST',)

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

    startTime = self.__TryParseDatetime(start)
    if start is None:
      response.write(self.__AddBattleFailureJSON("ERROR_BAD_START"))
      return response

    end = request.data.get('end')
    if end is None:
      response.write(self.__AddBattleFailureJSON("ERROR_NO_END"))
      return response

    endTime = self.__TryParseDatetime(end)
    if end is None:
      response.write(self.__AddBattleFailureJSON("ERROR_BAD_END"))
      return response

    # We got passed all our error checking, send the sproc call!
    params = [attacker, defender, winner, startTime, endTime,]

    ## Connect to our database and call the sproc
    cur = connection.cursor()
    cur.callproc("kixeye.AddBattle", params)
    cur.close()

    # Set err, time
    response.write(self.__AddBattleSuccessJSON())
    return response

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

  # Utility function for pulling out datetime values
  def __TryParseDatetime(self, val, default=None):
    try:
      return datetime.strptime(val, "%Y-%m-%d")
    except ValueError:
      return default