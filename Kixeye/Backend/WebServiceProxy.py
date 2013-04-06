import httplib
import json

class WebServiceProxy(object):
  """ This will allow the APIs to interface with our web service """

  m_serverInfo = None

  def __init__(self, serverInfo):
    self.m_serverInfo = serverInfo

  def SendWebRequest(self, method, url, params, headers):
    try:
      connection = httplib.HTTPConnection(self.m_serverInfo)

      if connection is None:
        print "Connection not established"
        return None

      connection.request(method=method, url=url, body=params, headers=headers)

      response = connection.getresponse()
      connection.close()
      return response

    except Exception, e:
      print "Failed to call method {0}: {1}".format(method, e)
      return None