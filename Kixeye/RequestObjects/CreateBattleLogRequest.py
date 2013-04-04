import json

class CreateBattleLogRequest(object):

  """ This class will contain all of the information that is used for a CreateBattleLog request """
  """ Based on its members it will create its own JSON POST parameters """

  # Members required for sending a CreateUserRequest
  m_attacker = None
  m_defender = None
  m_winner = None
  m_startTime = None
  m_endTime = None

  def __init__(self, attacker, defender, winner, start, end):
    self.m_attacker = attacker
    self.m_defender = defender
    self.m_winner = winner
    self.m_startTime = start
    self.m_endTime = end

  def GetJSON(self):
    print json.dumps(
                      {
                        'attacker': self.m_attacker,
                        'defender': self.m_defender,
                        'winner': self.m_winner,
                        'start': self.m_startTime,
                        'end': self.m_endTime
                      },
                      sort_keys=True,
                      indent=4,
                      separators=(',', ': '))
    return json.dumps(
                      {
                        'attacker': self.m_attacker,
                        'defender': self.m_defender,
                        'winner': self.m_winner,
                        'start': self.m_startTime,
                        'end': self.m_endTime
                      },
                      sort_keys=True,
                      indent=4,
                      separators=(',', ': '))
