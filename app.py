from flask import Flask, jsonify, request

app = Flask(__name__)

studentdb = [
    {
        "student_id": ["123"],
        "first_name": ["ashish "],
        "last_name": ["kutchi"],
        "dob": ["November 27"],
        "amount_due": ["3 Million"]
    },
    {
        "student_id": ["456"],
        "first_name": ["sam"],
        "last_name": ["thomas"],
        "dob": ["february 15"],
        "amount_due": ["8 Million"]
    },
    {
        "student_id": ["789"],
        "first_name": ["anish"],
        "last_name": ["m"],
        "dob": ["may 8"],
        "amount_due": ["5 Million"]
    }
]

@app.route('/')
def he():
    return 'hello world'


@app.route('/sampledb')
def hello():
    return jsonify(studentdb)


@app.route('/sampledb', methods=['POST'])
def add_db():
    req = request.get_json()
    studentdb.append(req)
    return {'id': len(studentdb)}, 200

@app.route('/sampledb/<int:index>', methods=['PUT'])
def put_db(index):
    req = request.get_json()
    studentdb[index] = req
    return jsonify(studentdb[index]), 200

@app.route('/sampledb/<int:index>', methods=['DELETE'])
def delete_db(index):
    studentdb.pop(index)
    return 'None', 200



app.run()