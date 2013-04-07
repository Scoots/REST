Tools Used:
	MySQL/Workbench
	Visual Studio 2010
	Python Tools For Windows - Used for having python solutions
	django - Python framework for web applications, emphasizes MVC
	django-piston - framework for django for creating RESTful APIs
	MySQLdb - Python modules for interacting with MySQL databases
	
Download Information:
Download django
	After getting the tar.gz I unzipped and ran setup.py install to get the info into site_packages
Download django-piston
	https://bitbucket.org/jespern/django-piston/downloads/
	python setup.py install

Pre-Start Information:
Downloaded MySQLdb for python
	http://sourceforge.net/projects/mysql-python/files/latest/download
	
Before running:
	MySQL -> Edit -> Preferences -> SQL Queries -> Safe Updates turned off
		This was my first time using MySQL and did not know how to set up foreign keys
	
Database Information:
	Used MySQL
	Created 3 Tables
		user
			Contains information about the user that is largely unchanging
		user_statistics
			Contains information about the user that changes frequently
		battle
			Stores information about battles
	Created 8 stored procedures
		AddBattle
		CreateUser
		GetBattles
		GetUserFromId
		GetUserFromNickname
		ModifyUserFirstName
		ModifyUserLastName
		ModifyUserNickname
	Would have liked to set up foreign key relationships
		Anything involving an id should be a FK to the user table
		
How to Run:
	Run the MySQLDeployScript.sql
	Go to <BaseDir>/KixeyeWebService
	Call manage.py sql KixeyeAPI
	Call manage.py syncdb
	Start up the web service by running manage.py runserver 8001
		- This starts up the server running on port 8001, which is where the test client I made is currently pointing
		- If you want to step through the code as it is running:
			- Set KixeyeWebService as the startup project
			- Set manage.py as the start file
			- Run with F5
			- Open another Visual Studio, change the startup project to Kixeye and the startup file to UnitTests.py
			- Update line 16 in API.py to point at the port your server is running on
			- Set any breakpoints you want, change any values that the functions are calling
			- Run!
	
Known Issues:
	- The date for the /battles?start=<start>&end=<end> request must be in YYYY-mm-dd format
	- Doing a nickname search doesn't redirect you to multiple pages, it simply dumps all of the data for all of the people that matched your query
	- The nickname search allows you to type /users/s?nickname=<NAME>; As long as there is a letter after /users/ and the final syntax is ?nickname=<NAME> it will work
	- Doing a nickname search adds a slash into the URL (/users/search?nickname=<NICKNAME> turns into /users/search/?nickname=<NICKNAME>)
	
Assumptions Made:
	- All times were supposed to be in UTC and didn't need to worry about timezone conversion
	- The HttpResponse objects for the getters didn't need to be in awesome JSON format
	- We would want more control over our databases than just auto generating them from the models file
		- Because of this I did not use the django database work