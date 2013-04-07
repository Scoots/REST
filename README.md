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
	cd <BaseDir>/KixeyeWebService
	python manage.py sql KixeyeAPI
	python manage.py syncdb
	
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
	You can run the python client unit tests by running UnitTests.py.
	
Known Issues:
	- ModifyUser not working correctly.  The regular expression in the KixeyeAPI/users.py file is matching my PUT command with my r'^users/$' regular expression, and it doesn't know how to handle it
	- The date for the /battles?start=<start>&end=<end> request must be in YYYY-mm-dd format
	
Assumptions Made:
	- The API should be a separate call from the getters
		- This allows me to separate views from backend functionality
	- All times were supposed to be in UTC and didn't need to worry about timezone conversion