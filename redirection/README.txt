THESE STEPS HAVE BEEN MODIFIED TO RUN ON AMAZON LINUX SERVER


STEP ONE : Installing and Enabling mod_wsgi file:

commands : sudo apt-get install libapache2-mod-wsgi python-dev && sudo a2enmod wsgi

STEP TWO: Create a FlaskApp

Commands: 

cd /var/www/html/
sudo mkdir FlaskApp
cd FlaskApp
sudo mkdir FlaskApp (we're creating another FlaskApp folder inside the FlaskApp folder)
cd FlaskApp
sudo mkdir templates 
sudo nano __init__.py

paste the following code : 


from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "IT WORKS!!"
if __name__ == "__main__":
    app.run()

save and close the file

Now the structure inside html folder is: 

|--html
|----FlaskApp
|---------FlaskApp
|--------------__init__.py
|--------------templates

STEP THREE : Install Flask

commands :

To install pip use : sudo apt-get install python-pip 
To install Flask : sudo pip install Flask 


STEP FOUR : Configure and Enable a Virtual Host 

commands: 

sudo nano /etc/httpd/conf.d/FlaskApp.conf

Paste the follwing configuration in the FlaskApp.conf file

<VirtualHost 127.0.0.1:80>
		ServerName flaskwsgi.com
		ServerAdmin youremailid.com
		WSGIScriptAlias / /var/www/html/FlaskApp/flaskapp.wsgi
		<Directory /var/www/html/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

Save and close the file

STEP FIVE : Enable Virtual Host 

command : sudo a2ensite FlaskApp.conf

STEP SIX: CREATE A .wsgi FILE

cd /var/www/html/FlaskApp
sudo nano flaskapp.wsgi

Add the follwing lines to the file:

#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/FlaskApp/")

from FlaskApp import app as application
application.secret_key = 'Add your secret key' 

Structure of Directory 

|---html
|--------FlaskApp
|----------------FlaskApp
|-----------------------templates
|-----------------------__init__.py
|----------------flaskapp.wsgi


STEP SEVEN : Create a entry in hosts file .

commands:

cd /etc
sudo nano hosts

change name for 127.0.0.1 from localhost to flaskwsgi.com

Save and close the file 

STEP EIGHT : Restart Apache

command : sudo service httpd restart
