# Inventory-management-with-Django
Inventory management with Django

## Environment setup:
```Bash
sudo apt install mysql-server
```
##Virtual Environment Setup
```Bash
python3 -m venv env
. env/bin/activate
```
## Install Django 
```Bash
pip install django
```
## For mysql database
```Bash
sudo apt install python3-dev
sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev
pip install mysqlclient
```
## For migrate
```Bash
python manage.py migrate
```
## Run
```Bash
python manage.py runserver yourserverip:port
```