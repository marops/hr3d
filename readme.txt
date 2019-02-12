Readme

1. Dumpdata. 

	a. Restore to new DB.

		./manage.py dumpdata --indent 2 -e auth.permission -e contenttypes > hr3d_db.json (you can also exclude on loaddata)

	b. Restore to same DB

		./manage.py dumpdata > hr3d_backup.json


2. Loaddata. Use ./manage.py loaddata <fixture> for restore to same DB. Add -e auth.permission -e contenttypes for restore to new project (not needed if excluded in dumpdata).