import json

class CreateUserRequest(object):
  """ This class will contain all of the information that is used for a CreateUser request """
  """ Based on its members it will create its own JSON POST parameters """

  # Members required for sending a CreateUserRequest
  first = None
  last = None
  nickname = None

  def __init__(self, first, last, nick):
    self.first = first
    self.last = last
    self.nickname = nick

  def GetJSON(self):
    print json.dumps(self.__dict__)
    return json.dumps(self.__dict__)
