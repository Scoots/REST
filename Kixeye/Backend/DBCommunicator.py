import httplib
import json

class DBCommunicator(object):
  """ This will allow the APIs to interface with our database """

  m_serverInfo = None

  def __init__(self, serverInfo):
    self.m_serverInfo = serverInfo

  def SendWebRequest(self, method, url, params, headers):
    try:
      connection = httplib.HTTPConnection(self.m_serverInfo)
      connection.request(method=method, url=url, body=params, headers=headers)
    except Exception, e:
      print "Failed to call method %s" %method
      return False, connection
    return True, connection