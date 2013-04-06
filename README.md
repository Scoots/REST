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
	You can run the python client unit tests by running UnitTests.py.  It is very rudimentary and was just meant to test the communcation when sending the HttpRequest objects.  Since I never got this working, the layer is largely unfinished.
	
Known Issues:
	- Error 400 received on all requests sent to the KixeyeAPI URL
	- No username/password authentication on API calls
	- The date for the /battles?start=<start>&end=<end> request must be in YYYY-mm-dd format