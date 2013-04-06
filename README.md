Download MySQL
Download Python Tools For Windows (needed to open the solution in Visual Studio)
Download django
	After getting the tar.gz I unzipped and ran setup.py install to get the info into site_packages
Download django-piston
	https://bitbucket.org/jespern/django-piston/downloads/
	python setup.py install


Using MySQL database
Downloaded MySQLdb for python
	http://sourceforge.net/projects/mysql-python/files/latest/download
	
Before running, I needed to
	cd <BaseDir>/KixeyeWebService
	python manage.py sql KixeyeAPI
	python manage.py syncdb
	
MySQL -> Edit -> Preferences -> SQL Queries -> Safe Updates turned off
	Did this because I don't know how to set foreign keys in MySQL
	

Made a USER, BATTLE, and USER_STATISTICS table to contain all of the data
i dont know how to set foreign keys in mysql