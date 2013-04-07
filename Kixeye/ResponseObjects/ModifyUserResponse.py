import json

class ModifyUserResponse(object):
  """ The object that is returned from a ModifyUserRequest """

  # These members are for both success and failure cases
  # In the case of success, the m_errorDescription member will be None
  m_error = 'true'
  m_time = None
  m_errorDescription = "No JSON supplied"

  def __init__(self, JSONStr = ""):
    # In this case we made this object to report an error
    if JSONStr == "":
      return

    content = json.loads(str(JSONStr))
    for key, value in content.iteritems():
      if key == "error":
        self.m_error = value
      elif key == "time":
        self.m_time = value
      elif key == "msg":
        self.m_errorDescription = value

