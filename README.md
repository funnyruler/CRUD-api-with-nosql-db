# nosql-api
Api with nosql database - mongodb.
# App description
This app uses docker for deployment. Docker will install and deploy `python3.10`, `mongodb` service.
# Functionality
This app have `POST`, `GET`, `PUT` methods.

`/` - is a start page off this app

`/add_value` - is a `POST` route to add value in mongodb, need to pass `json` as a body value in format `{"testkey": "testvalue", "another_key": "another_value"}`.
In case of success you will see appropriate message, otherwise - error message.

`/get_value` - is a `GET` route to get value from mongodb by key, you need to pass named param `key` in url 
to get value by this key, e.g, `/get_value?key=testkey`.

`/change_value` - is a `PUT` route to change existing value by key, you need to pass 
a key which value you want to change and new value to change it, by json in format `{"key_to_change": "key", "new_value": "test1"}`.
In case of success you will see appropriate message with count of changed values, otherwise - error message.
# Configuration
Configuration of flask app in `/flask_app/.env`

By default, mongodb create database with name `testapp_db` and collection with name 
`testapp_collection` you can change this values in `\docker-entrypoint-initdb.d\mongo-init.js` 
and `.env` file.
# Deploying
To deploy this app you need to install docker and git:
```
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt-cache policy docker-ce
sudo apt install docker-ce
sudo apt install docker-compose
sudo apt-get install git-all
```
Next you need to clone repository, build and run docker image:
```
cd /home/your_folder
git clone https://github.com/funnyruler/nosql-api.git
cd nosql-api
docker-compose up --build
```
