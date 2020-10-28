# Requirements
sudo apt install python3-dev libpq-dev

# Install
sudo apt install postgresql postgresql-contrib

# Create user
sudo -u postgres createuser --interactive

# Enter name of role to add: <user>
# Shall the new role be a superuser? (y/n) y

# Create database
createdb <db name>
# sudo -u daniel createdb music

# Root commands
sudo -u <user> <command> <datavase>
# sudo -u daniel createdb test04

# Install psycopg2
pip install psycopg2

# Change password
sudo -u <user> psql <db_name>
ALTER USER user_name WITH PASSWORD 'new_password';

# Install pgAdmin
# Setup the repository
# Install the public key for the repository (if not done previously):
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add

# Create the repository configuration file:
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

# Install for both desktop and web modes:
sudo apt install pgadmin4

# Install for desktop mode only:
sudo apt install pgadmin4-desktop

# Install for web mode only: 
sudo apt install pgadmin4-web 

# Configure the webserver, if you installed pgadmin4-web:
sudo /usr/pgadmin4/bin/setup-web.sh