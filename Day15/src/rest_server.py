from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/person', methods=['GET'])
def get_person():
    name = request.args.get('name')
    age = request.args.get('age')

    if not name or not age:
        return jsonify({"error": "Name and age parameters are required"}), 400

    person = {
        "name": name,
        "age": age
    }

    return jsonify(person)


if __name__ == '__main__':
    app.run(port=8080)
