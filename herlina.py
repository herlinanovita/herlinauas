from flask import Flask, jsonify, request

app = Flask(__name__)

datamhs = [
    {"id": 1, "Nama": "Herlina Novita", "Jurusan": "Sistem Informasi", "NIM": "2119113942"},
]

def find_next_id():
    return max(j["id"] for j in jurusan) + 1 if jurusan else 1

@app.route("/", methods=['GET'])
def get_data():
    return jsonify(datamhs)

@app.route("/", methods=['POST'])
def add_data():
    if request.is_json:
        new_data = request.get_json()
        new_data["id"] = find_next_id()
        jurusan.append(new_data)
        return jsonify(new_data), 201
    return jsonify({"error": "Request must be JSON"}), 415

if __name__ == "__main__":
    app.run(debug=True, port=5000)
