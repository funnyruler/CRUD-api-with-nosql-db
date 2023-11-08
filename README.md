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

`/change_value` - is a `PUT` rote to change existing value
To deploy this app you need preinstalled docker on your machine
