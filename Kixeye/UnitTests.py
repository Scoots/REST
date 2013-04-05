from RequestObjects.CreateUserRequest import CreateUserRequest
from RequestObjects.ModifyUserRequest import ModifyUserRequest
from RequestObjects.CreateBattleLogRequest import CreateBattleLogRequest
from REST import REST

import time

rest = REST()

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
rest.CreateUser(createUserRequest)
rest.CreateUser(modifyUserRequest)
rest.CreateUser(createBattleLogRequest)

rest.ModifyUser(modifyUserRequest)
rest.ModifyUser(createUserRequest)
rest.ModifyUser(createBattleLogRequest)

rest.CreateBattleLog(createBattleLogRequest)
rest.CreateBattleLog(createUserRequest)
rest.CreateBattleLog(createBattleLogRequest)

rest.Connect("shopp", "Password")

# All fail with incorrect object
print
print "All checks below should fail with incorrect object errors"
rest.CreateUser(modifyUserRequest)
rest.CreateUser(createBattleLogRequest)

rest.ModifyUser(createUserRequest)
rest.ModifyUser(createBattleLogRequest)

rest.CreateBattleLog(createUserRequest)
rest.CreateBattleLog(modifyUserRequest)

# All fail because of invalid request data
print
print "All checks below should fail with invalid request data"
print "They won't actually fail until the website itself fails"
rest.ModifyUser(modifyUserRequest)

# Updating the modify user request data
modifyUserRequest.m_field = "first"

# All pass
print
print "All checks below should pass by printing out their JSON requests"
rest.CreateUser(createUserRequest)
rest.ModifyUser(modifyUserRequest)
rest.CreateBattleLog(createBattleLogRequest)

time.sleep(10)