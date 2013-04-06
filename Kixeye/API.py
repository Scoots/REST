from RequestObjects.CreateUserRequest import CreateUserRequest
from RequestObjects.ModifyUserRequest import ModifyUserRequest
from RequestObjects.CreateBattleLogRequest import CreateBattleLogRequest
from ResponseObjects.CreateUserResponse import CreateUserResponse
from ResponseObjects.ModifyUserResponse import ModifyUserResponse
from ResponseObjects.CreateBattleLogResponse import CreateBattleLogResponse
from Backend.DBCommunicator import DBCommunicator
import json

class API:
  """The API that the user can call to make the requests to send JSON requests"""

  __m_authenticated = False
  __m_dbCommunicator = DBCommunicator("PASS_YOUR_SERVER_INFO_HERE")
  __m_BaseURL = "myURL"

  #-----------------------------------------------------------------------
  # Fake connect function
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
    # Check if we are authenticated
    if not self.__m_authenticated:
      print "Not authenticated"
      returnObj = CreateUserResponse()
      returnObj.m_errorDescription = "ERROR_NOT_AUTHENTICATED"
      return returnObj

    # Check if we have the appropriate request
    if not type(userRequest) == CreateUserRequest:
      # Log and throw error
      print "Invalid type, was not a CreateUserRequest"
      returnObj = CreateUserResponse()
      returnObj.m_errorDescription = "ERROR_INVALID_TYPE"
      return returnObj

    # Get our JSON parameters and our headers
    params = userRequest.GetJSON()
    headers = {"Content-type": "application/json"}

    # Send the JSON request, wait for the response and return it
    #success, connection = self.__m_dbCommunicator.SendWebRequest("POST", __m_BaseURL + "/users", params, headers)
    success = True
    # If the web request failed, report an error
    if not success:
      returnObj = CreateUserResponse()
      returnObj.m_errorDescription = "ERROR_FAILED_TO_CALL_METHOD"
      return returnObj

    # Return the response object
    return CreateUserResponse()#connection.getresponse())

  #-----------------------------------------------------------------------
  # CreateUser function
  # Takes a ModifyUserRequest and returns a ModifyUserResponse
  #-----------------------------------------------------------------------
  def ModifyUser(self, userRequest):
    # Check if we are authenticated
    if not self.__m_authenticated:
      print "Not authenticated"
      returnObj = ModifyUserResponse()
      returnObj.m_errorDescription = "ERROR_NOT_AUTHENTICATED"
      return returnObj

    # Check if we have the appropriate request
    if not type(userRequest) == ModifyUserRequest:
      # Log and throw error
      print "Invalid type, was not a CreateUserRequest"
      returnObj = ModifyUserResponse()
      returnObj.m_errorDescription = "ERROR_INVALID_TYPE"
      return returnObj

    # Get our JSON parameters and our headers
    params = userRequest.GetJSON()
    headers = {"Content-type": "application/json"}

    # Send the JSON request, wait for the response and return it
    #success, connection = self.__m_dbCommunicator.SendWebRequest("POST", __m_BaseURL + "/users", params, headers)
    success = True
    # If the web request failed, report an error
    if not success:
      returnObj = ModifyUserResponse()
      returnObj.m_errorDescription = "ERROR_FAILED_TO_CALL_METHOD"
      return returnObj

    # Return the response object
    return ModifyUserResponse()#connection.getresponse())
  
  #-----------------------------------------------------------------------
  # CreateBattleLog function
  # Takes a CreateBattleLogRequest and returns a CreateBattleLogResponse
  #-----------------------------------------------------------------------
  def CreateBattleLog(self, userRequest):
    # Check if we are authenticated
    if not self.__m_authenticated:
      print "Not authenticated"
      returnObj = CreateBattleLogResponse()
      returnObj.m_errorDescription = "ERROR_NOT_AUTHENTICATED"
      return returnObj

    # Check if we have the appropriate request
    if not type(userRequest) == CreateBattleLogRequest:
      # Log and throw error
      print "Invalid type, was not a CreateUserRequest"
      returnObj = CreateBattleLogResponse()
      returnObj.m_errorDescription = "ERROR_INVALID_TYPE"
      return returnObj

    # Get our JSON parameters and our headers
    params = userRequest.GetJSON()
    headers = {"Content-type": "application/json"}

    # Send the JSON request, wait for the response and return it
    #success, connection = self.__m_dbCommunicator.SendWebRequest("POST", __m_BaseURL + "/users", params, headers)
    success = True
    # If the web request failed, report an error
    if not success:
      returnObj = CreateBattleLogResponse()
      returnObj.m_errorDescription = "ERROR_FAILED_TO_CALL_METHOD"
      return returnObj

    # Return the response object
    return CreateBattleLogResponse()#connection.getresponse())