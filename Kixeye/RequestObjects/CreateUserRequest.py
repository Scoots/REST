class CreateUserRequest(object):
  """ This class will contain all of the information that is used for a CreateUser request """
  """ Based on its members it will create its own JSON POST parameters """

  # Members required for sending a CreateUserRequest
  m_firstName = None
  m_lastName = None
  m_nickname = None

  def __init__(self, first, last, nick):
    self.m_firstName = first
    self.m_lastName = last
    self.m_nickname = nick

  def PrintJSON(self):
    print self.m_firstName
    print self.m_lastName
    print self.m_nickname
