from RequestObjects.CreateUserRequest import CreateUserRequest
from RequestObjects.ModifyUserRequest import ModifyUserRequest
from RequestObjects.CreateBattleLogRequest import CreateBattleLogRequest
from Backend.DBCommunicator import DBCommunicator
import json

class REST:
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
    if not self.__m_authenticated:
      # Log and throw error
      print "Not authenticated"
      returnObj.m_errorDescription = "ERROR_NOT_AUTHENTICATED"
      return returnObj

    if not type(userRequest) == CreateUserRequest:
      # Log and throw error
      print "Invalid type, was not a CreateUserRequest"
      returnObj.m_errorDescription = "ERROR_INVALID_TYPE"
      return returnObj

    params = userRequest.GetJSON()
    headers = {"Content-type": "application/json"}

    # Send the JSON request, wait for the response and return it
    #success, connection = self.__m_dbCommunicator.SendWebRequest("POST", __m_BaseURL + "/users", params, headers)
    #response = connection.getresponse()
    returnObj = CreateUserResponse()
    #if response.status == 200: # This means it was successful
      #parse the data here
      #returnObj.GetFromJSON(data)
    return returnObj

  #-----------------------------------------------------------------------
  # CreateUser function
  # Takes a ModifyUserRequest and returns a ModifyUserResponse
  #-----------------------------------------------------------------------
  def ModifyUser(self, userRequest):
    if not self.__m_authenticated:
      # Log and throw error
      print "Not authenticated"
      returnObj.m_errorDescription = "ERROR_NOT_AUTHENTICATED"
      return returnObj

    if not type(userRequest) == ModifyUserRequest:
      # Log and throw error
      print "Invalid type, was not a ModifyUserRequest"
      returnObj.m_errorDescription = "ERROR_INVALID_TYPE"
      return returnObj

    params = userRequest.GetJSON()
    headers = {"Content-type": "application/json"}

    # Send the JSON request, wait for the response and return it
    #self.__m_dbCommunicator.SendWebRequest("PUT",__m_BaseURL + "/users/" + str(userRequest.m_user), params, headers)
    #response = connection.getresponse()
    returnObj = ModifyUserResponse()
    #if response.status == 200: # This means it was successful
      #parse the data here
      #returnObj.GetFromJSON(data)
    return returnObj
  
  #-----------------------------------------------------------------------
  # CreateBattleLog function
  # Takes a CreateBattleLogRequest and returns a CreateBattleLogResponse
  #-----------------------------------------------------------------------
  def CreateBattleLog(self, userRequest):
    returnObj = CreateBattleLogResponse()
    if not self.__m_authenticated:
      # Log and throw error
      print "Not authenticated"
      returnObj.m_errorDescription = "ERROR_NOT_AUTHENTICATED"
      return returnObj

    if not type(userRequest) == CreateBattleLogRequest:
      # Log and throw error
      print "Invalid type, was not a CreateBattleLogRequest"
      returnObj.m_errorDescription = "ERROR_INVALID_TYPE"
      return returnObj

    params = userRequest.GetJSON()
    headers = {"Content-type": "application/json"}

    # Send the JSON request, wait for the response and return it
    #self.__m_dbCommunicator.SendWebRequest("POST", __m_BaseURL + "/battles", params, headers)
    #response = connection.getresponse()
    #if response.status == 200: # This means it was successful
      #parse the data here
      #returnObj.GetFromJSON(data)
    return returnObj