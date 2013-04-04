import json

class ModifyUserRequest(object):
  """ This class will contain all of the information that is used for a ModifyUser request """
  """ Based on its members it will create its own JSON POST parameters """

  # Members required for sending a ModifyUserRequest
  m_user = None
  m_field = None
  m_value = None

  def __init__(self, user, field, value):
    self.m_user = user
    self.m_field = field
    self.m_value = value

  def GetJSON(self):
    print json.dumps(
                      {
                        'field': self.m_field,
                        'value': self.m_value
                      },
                      sort_keys=True,
                      indent=4,
                      separators=(',', ': '))
    return json.dumps(
                      {
                        'field': self.m_field,
                        'value': self.m_value
                      },
                      sort_keys=True,
                      indent=4,
                      separators=(',', ': '))


