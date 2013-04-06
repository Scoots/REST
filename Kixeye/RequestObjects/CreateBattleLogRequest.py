import json

class CreateBattleLogRequest(object):

  """ This class will contain all of the information that is used for a CreateBattleLog request """
  """ Based on its members it will create its own JSON POST parameters """

  # Members required for sending a CreateUserRequest
  attacker = None
  defender = None
  winner = None
  startTime = None
  endTime = None

  def __init__(self, attacker, defender, winner, start, end):
    self.attacker = attacker
    self.defender = defender
    self.winner = winner
    self.start = start
    self.end = end

  def GetJSON(self):
    return json.dumps(self.__dict__)
