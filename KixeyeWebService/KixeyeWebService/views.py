from django.http import HttpResponse
import django.db
from models import User

# Theoretically this goes to the database, pulls out the applicable User rows
# and returns them as an HTTPResponse
def GetUser(request, expression):
  ## Connect to our database
  #cur = django.db.connections['default'].cursor()
  #cur.callproc('GetUserFromId', [7,])
  #results = cur.fetchall()
  #cur.close()
  
  #var = django.db.connections['kixeyeapi'].cursor()

  # Check if the expression is a user id
  userId = __TryParseInt(expression)
  if userId is not None:
    # Go digging through the database to find the appropriate set of data to return
    return HttpResponse("You're looking at user_id {0}.".format(userId))

  # If it isn't an id, see if we are searching by nickname
  nickname = request.GET.get('nickname')
  if nickname is not None:
    # Go digging through the database to find the appropriate set of data to return
    return HttpResponse("You're looking at nickname {0}.".format(nickname))

  #return [User(*row) for row in results]
  return HttpResponse("You're not looking at user_id or nickname")

def GetBattles(request, expression):
  # Go digging through the database to find the appropriate data set
  start = request.GET.get('start')
  end = request.GET.get('end')
  
  return HttpResponse("StartTime: {0}   :   EndTime: {1}".format(start, end))

# Utility function for pulling out int values
def __TryParseInt(val, base=10, default=None):
  try:
    return int(val, base)
  except ValueError:
    return default