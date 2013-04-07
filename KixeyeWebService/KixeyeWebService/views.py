from django.http import HttpResponse
from django.db import connection
from models import User
from datetime import datetime

#-----------------------------------------------------------------------
# View for looking at battles
#-----------------------------------------------------------------------
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

#-----------------------------------------------------------------------
# Utility function for pulling out int values
#-----------------------------------------------------------------------
def __TryParseInt(val, base=10, default=None):
  try:
    return int(val, base)
  except:
    return default
  
#-----------------------------------------------------------------------
# Utility function for pulling out datetime values
#-----------------------------------------------------------------------
def __TryParseDatetime(val, default=None):
  try:
    return datetime.strptime(val, "%Y-%m-%d")
  except:
    return default
  
#-----------------------------------------------------------------------
# Calls stored procedures in our default database
#-----------------------------------------------------------------------
def __CallSproc(sprocName, params):
  ## Connect to our database and call the sproc
  cur = connection.cursor()
  cur.callproc(sprocName, params)
  results = cur.fetchall()
  cur.close()
  return results
