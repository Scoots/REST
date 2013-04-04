import CreateUserRequest
import ModifyUserRequest
import CreateBattleLogRequest

class REST:
  """The API that the user can call to make the requests to send JSON requests"""

  __m_authenticated = None

  def Connect(self, name, password):
    if not self.__m_authenticated:
      # Don't do anything if we are already authenticated
      return

    # I am just saying we are authenticated
    self.__m_authenticated = true

  def CreateUser(self, userRequest):
    if not self.__m_authenticated:
      # Log and throw error
      return

    if not type(userRequest) == CreateUserRequest:
      # Log and throw error
      return
    # Send the JSON request, wait for the response and return it

  def ModifyUser(self, userRequest):
    if not self.__m_authenticated:
      # Log and throw error
      return

    if not type(userRequest) == ModifyUserRequest:
      # Log and throw error
      return
    # Send the JSON request, wait for the response and return it
  
  def CreateBattleLog(self, userRequest):
    if not self.__m_authenticated:
      # Log and throw error
      return

    if not type(userRequest) == CreateBattleLogRequest:
      # Log and throw error
      return
    # Send the JSON request, wait for the response and return it







  # Can add base database connection stuff here
  # If we were creating more APIs I would have put this in a base somewhere