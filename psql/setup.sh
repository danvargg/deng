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