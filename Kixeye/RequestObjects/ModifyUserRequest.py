class ModifyUserRequest(object):
  """ This class will contain all of the information that is used for a ModifyUser request """
  """ Based on its members it will create its own JSON POST parameters """

  # Members required for sending a ModifyUserRequest
  m_field = None
  m_value = None

  def __init__(self, field, value):
    self.m_field = field
    self.m_value = value

  def PrintJSON(self):
    print self.m_field
    print self.m_value


