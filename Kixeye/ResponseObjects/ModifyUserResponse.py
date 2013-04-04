class ModifyUserResponse(object):
  """ The object that is returned from a ModifyUserRequest """

  # These members are for both success and failure cases
  # In the case of success, the m_errorDescription member will be None
  m_error = True
  m_time = None
  m_errorDescription = "No JSON supplied"

  def GetFromJSON(JSONString):
    # Take a string and set the variables appropriately
    m_error = true

