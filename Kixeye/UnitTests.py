from RequestObjects.CreateUserRequest import CreateUserRequest
from RequestObjects.ModifyUserRequest import ModifyUserRequest
from RequestObjects.CreateBattleLogRequest import CreateBattleLogRequest
from API import API

import time

api = API()

createUserRequest = CreateUserRequest("Sam", "Hopp", "Scoots")
modifyUserRequest = ModifyUserRequest(1, "name", "NewName")
createBattleLogRequest = CreateBattleLogRequest(
                          1,
                          2,
                          1,
                          '2013-04-03',
                          '2013-04-04')

# All fail with non-authenticated
print "All checks below should fail with a not-authenticated error"
api.CreateUser(createUserRequest)
api.CreateUser(modifyUserRequest)
api.CreateUser(createBattleLogRequest)

api.ModifyUser(modifyUserRequest)
api.ModifyUser(createUserRequest)
api.ModifyUser(createBattleLogRequest)

api.CreateBattleLog(createBattleLogRequest)
api.CreateBattleLog(createUserRequest)
api.CreateBattleLog(createBattleLogRequest)

api.Connect("shopp", "Password")

# All fail with incorrect object
print
print "All checks below should fail with incorrect object errors"
api.CreateUser(modifyUserRequest)
api.CreateUser(createBattleLogRequest)

api.ModifyUser(createUserRequest)
api.ModifyUser(createBattleLogRequest)

api.CreateBattleLog(createUserRequest)
api.CreateBattleLog(modifyUserRequest)

# All fail because of invalid request data
print
print "All checks below should fail with invalid request data"
print "They won't actually fail until the website itself fails"
api.ModifyUser(modifyUserRequest)

# Updating the modify user request data
modifyUserRequest.m_field = "first"

# All pass
print
print "All checks below should pass by printing out their JSON requests"
api.CreateUser(createUserRequest)
api.ModifyUser(modifyUserRequest)
api.CreateBattleLog(createBattleLogRequest)

time.sleep(10)