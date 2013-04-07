from django.http import HttpResponse
from django.db import connection
from models import User
from datetime import datetime

# Theoretically this goes to the database, pulls out the applicable User rows
# and returns them as an HTTPResponse
def GetUser(request, expression):

  #myVar = User.objects.raw('SELECT * FROM kixeye.user AS u WHERE u.user_id = 7')

  # Check if the expression is a user id
  userId = __TryParseInt(expression)
  if userId is not None:
    # Go digging through the database to find the appropriate set of data to return
    results = __CallSproc("kixeye.GetUserFromId", [userId,])

    # If we don't have any rows, error
    if len(results) < 1:
      return HttpResponse("No rows returned for params {0}".format([userId,]))
    
    # Only grab the first row
    return HttpResponse(results[0])

  # If it isn't an id, see if we are searching by nickname
  nickname = request.GET.get('nickname')
  if nickname is not None:
    # Go digging through the database to find the appropriate set of data to return
    results = __CallSproc("kixeye.GetUserFromNickname", [nickname,])

    # If we don't have any rows, error
    if len(results) < 1:
      return HttpResponse("No rows returned for params {0}".format([nickname,]))
    
    # Figure out how to redirect
    # I will need to change my sproc to return the user id instead of all user data
    return HttpResponse(results)

  return HttpResponse("You're not looking at user_id or nickname")

def GetBattles(request, expression):
  # Go digging through the database to find the appropriate data set
  start = request.GET.get('start')
  end = request.GET.get('end')

  startTime = __TryParseDatetime(start)
  endTime = __TryParseDatetime(end)
  if startTime is None or endTime is None:
    return HttpResponse("Invalid format for start ({0}) or end ({1})".format(start, end))
  
  results = __CallSproc('kixeye.GetBattles', [startTime, endTime,])
  # If we don't have any rows, error
  if len(results) < 1:
    return HttpResponse("No rows returned for params {0}".format([startTime, endTime,]))

  return HttpResponse(results)

# Utility function for pulling out int values
def __TryParseInt(val, base=10, default=None):
  try:
    return int(val, base)
  except ValueError:
    return default

# Utility function for pulling out datetime values
def __TryParseDatetime(val, default=None):
  try:
    return datetime.strptime(val, "%Y-%m-%d")
  except ValueError:
    return default

def __CallSproc(sprocName, params):
  ## Connect to our database and call the sproc
  cur = connection.cursor()
  cur.callproc(sprocName, params)
  results = cur.fetchall()
  cur.close()
  return results
