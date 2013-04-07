from RequestObjects.CreateUserRequest import CreateUserRequest
from RequestObjects.ModifyUserRequest import ModifyUserRequest
from RequestObjects.CreateBattleLogRequest import CreateBattleLogRequest
from ResponseObjects.CreateUserResponse import CreateUserResponse
from ResponseObjects.ModifyUserResponse import ModifyUserResponse
from ResponseObjects.CreateBattleLogResponse import CreateBattleLogResponse
from Backend.WebServiceProxy import WebServiceProxy
import json

class API:
  """The API that the user can call to make the requests to send JSON requests"""

  __m_authenticated = False

  # Change this value to wherever the server is running
  __m_BaseURL = "127.0.0.1:8001"
  __m_proxy = WebServiceProxy(__m_BaseURL)

  #-----------------------------------------------------------------------
  # Fake connect function
  # I haven't fully tested the web auth stuff, this was my hack to
  # 'pretend' I was forcing authentication.  I realize it is very different
  # on the web service.  It should be enabled, but again, largely untested
  #-----------------------------------------------------------------------
  def Connect(self, name, password):
    if self.__m_authenticated:
      # Don't do anything if we are already authenticated
      print "Already authenticated"
      return

    # I am just saying we are authenticated
    self.__m_authenticated = True

  #-----------------------------------------------------------------------
  # CreateUser function
  # Takes a CreateUserRequest and returns a CreateUserResponse
  #-----------------------------------------------------------------------
  def CreateUser(self, userRequest):
    # Object returned if there was an error
    errorObj = CreateUserResponse()

    # Check if we are authenticated
    if not self.__m_authenticated:
      errorObj.m_errorDescription = "ERROR_NOT_AUTHENTICATED"
      return errorObj

    # Check if we have the appropriate request
    if not type(userRequest) == CreateUserRequest:
      # Log and throw error
      errorObj.m_errorDescription = "ERROR_INVALID_TYPE"
      return errorObj

    # Get our JSON parameters and our headers
    params = userRequest.GetJSON()
    headers = {"Content-type": "application/json"}
    
    # Send the JSON request, wait for the response and return it
    result = self.__m_proxy.SendWebRequest("POST", "/users/", params, headers)

    if result is None:
      errorObj.m_errorDescription = "ERROR_FAILED_CONNECTION"
      return errorObj
    
    if not result.status == 200:
      errorObj.m_errorDescription = "ERROR_{0}_FROM_SERVICE".format(result.status)
      return errorObj

    # Return the response object
    return CreateUserResponse(result.read())

  #-----------------------------------------------------------------------
  # CreateUser function
  # Takes a ModifyUserRequest and returns a ModifyUserResponse
  #-----------------------------------------------------------------------
  def ModifyUser(self, userRequest):
    # Object returned if there was an error
    errorObj = ModifyUserResponse()

    # Check if we are authenticated
    if not self.__m_authenticated:
      errorObj.m_errorDescription = "ERROR_NOT_AUTHENTICATED"
      return errorObj

    # Check if we have the appropriate request
    if not type(userRequest) == ModifyUserRequest:
      # Log and throw error
      errorObj.m_errorDescription = "ERROR_INVALID_TYPE"
      return errorObj

    # Get our JSON parameters and our headers
    params = userRequest.GetJSON()
    headers = {"Content-type": "application/json"}

    # Send the JSON request, wait for the response and return it
    result = self.__m_proxy.SendWebRequest("PUT", "/users/{0}/".format(userRequest.m_user), params, headers)

    if result is None:
      errorObj.m_errorDescription = "ERROR_FAILED_CONNECTION"
      return errorObj

    if not result.status == 200:
      errorObj.m_errorDescription = "ERROR_{0}_FROM_SERVICE".format(result.status)
      return errorObj
    
    # Return the response object
    return ModifyUserResponse(result.read())
  
  #-----------------------------------------------------------------------
  # CreateBattleLog function
  # Takes a CreateBattleLogRequest and returns a CreateBattleLogResponse
  #-----------------------------------------------------------------------
  def CreateBattleLog(self, userRequest):
    # Object returned if there was an error
    errorObj = CreateBattleLogResponse()

    # Check if we are authenticated
    if not self.__m_authenticated:
      errorObj.m_errorDescription = "ERROR_NOT_AUTHENTICATED"
      return errorObj

    # Check if we have the appropriate request
    if not type(userRequest) == CreateBattleLogRequest:
      # Log and throw error
      errorObj.m_errorDescription = "ERROR_INVALID_TYPE"
      return errorObj

    # Get our JSON parameters and our headers
    params = userRequest.GetJSON()
    headers = {"Content-type": "application/json"}

    # Send the JSON request, wait for the response and return it
    result = self.__m_proxy.SendWebRequest("POST", "/battles/", params, headers)

    if result is None:
      errorObj.m_errorDescription = "ERROR_FAILED_CONNECTION"
      return errorObj
    
    if not result.status == 200:
      print "ERROR_{0}_FROM_SERVICE".format(result.status)
      errorObj.m_errorDescription = "ERROR_{0}_FROM_SERVICE".format(result.status)
      return errorObj

    # Return the response object
    return CreateBattleLogResponse(result.read())