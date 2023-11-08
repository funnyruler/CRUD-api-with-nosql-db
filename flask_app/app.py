import json
from flask import Flask, request
from database import DataBase
from bson import json_util
from typing import Union


mongo_db = DataBase()
app = Flask(__name__)


@app.route('/')
async def index():
    return "This is test app with MongoDB with GET, POST, PUT methods!Documentation - "


@app.route('/add_value', methods=['POST'])
def add_value() -> str:
    request_data = request.get_json()
    if not request_data:
        return "You need to pass a key with value, which you want to add"
    insert_status, row = mongo_db.insert_row(request_data)
    if insert_status:
        return f"Your data inserted with id {row.inserted_id}\nData: {request_data}"
    else:
        return f"Your data didn't save cause of exception: {row}"


@app.route('/get_value', methods=['GET'])
def get_value() -> Union[dict, str]:
    key = request.args.get('key')
    if not key:
        return "You need to pass a key which value you want to get"
    find_result = json.loads(json_util.dumps(mongo_db.get_value(key)))
    if find_result:
        return find_result
    else:
        return "No values by this key"


@app.route('/change_value', methods=['PUT'])
def change_value() -> str:
    request_data = request.get_json()
    if not request_data or len(request_data) != 2:
        return "You need to pass a key with value, which you want to change"
    change_status, change_result = mongo_db.change_value(request_data)
    if change_status:
        return f"Changed {change_result} documents"
    else:
        return f"Can't changed documents cause of exception: {change_result}"


if __name__ == '__main__':
    mongo_db.create_collection()
    app.run(host='0.0.0.0', port=8080, debug=False)
