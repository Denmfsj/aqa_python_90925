import random
import time

from flask import Flask, request, jsonify

from db_base import SQLiteActions

app = Flask(__name__)

SECRET_KEY = 'OLOLO_secret_key'


@app.route('/students/', methods=['GET'])
def get_students():


    limit = request.args.get('limit', 10)
    sort_by = request.args.get('sort_by', None)
    sort_type = None

    if sort_by:
        if sort_by.startswith('-'):
            sort_type = 'desc'
            sort_by = sort_by[1:]
        else:
            sort_type = 'asc'


    data = db.get_students(limit=limit, sort_by=sort_by, sort_type=sort_type)

    return jsonify(data), 200


@app.route('/auth/', methods=['POST'])
def get_token():
    is_user_data_correct_user = True
    user_data = request.get_json()

    if user_data.get('name') != 'test':
        is_user_data_correct_user = False

    if user_data.get('password') != 'test':
        is_user_data_correct_user = False

    if not is_user_data_correct_user:
        return jsonify("incorrect user name or password"), 403

    return SECRET_KEY, 200

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id: str):

    if not student_id.isnumeric():
        return jsonify({'error': 'student_id should be int'}), 400

    data = db.get_student(student_id)
    if not data:
        return jsonify({'error': 'Student with this id does not exist'}), 404

    return jsonify(data), 200


@app.route('/students/', methods=['POST'])
def create_students():

    auth_res = check_auth(request.headers)
    if auth_res is not None:
        return jsonify(auth_res[0]), auth_res[1]

    request_data = request.get_json()
    time.sleep(random.random() + 1.5) # sleep 1.5-2.5 sec
    error_msgs = []
    name = request_data.get('name')
    score = request_data.get('score', 0)

    if not name:
        error_msgs.append("You have to input name")
    if not 0 < score <= 100:
        error_msgs.append("Score must be between 1 and 100")

    if error_msgs:
        return jsonify(error_msgs), 400

    student = db.add_student(name=name, score=score)
    return jsonify(student), 201


@app.route('/students/<student_id>', methods=['PUT'])
def update_students(student_id):

    auth_res = check_auth(request.headers)
    if auth_res is not None:
        return jsonify(auth_res[0]), auth_res[1]

    request_data = request.get_json()

    name = request_data.get('name')
    score = request_data.get('score')
    score_name = request_data.get('score_name')

    student = db.get_student(student_id)

    if not name and not score and not score_name:
        return jsonify({'message': 'You have to put name and/or score and/or score_name of the student'}), 400

    name = name if name is not None else student['name']
    score = score if score is not None else student['score']
    score_name = score_name if score_name is not None else student['score_name']
    student = db.update_student(student_id=student_id, name=name, score=score, score_name=score_name)
    return jsonify(student), 200


@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):

    auth_res = check_auth(request.headers)
    if auth_res is not None:
        return jsonify(auth_res[0]), auth_res[1]

    db.delete_student(student_id)
    return jsonify({'message': f'Student {student_id} deleted'}), 204


def check_auth(headers):

    if headers.get('token') is None:
        return "You are not authorized", 401

    if headers.get('token') != SECRET_KEY:
        return "Token is incorrect", 403


if __name__ == '__main__':
    db = SQLiteActions('ololo1.db')
    host = '127.0.0.1'
    port = 8080
    app.run(host=host, port=port, debug=True)