from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo,MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)
CORS(app)

# --------------- MongoDB connection ---------------
client=MongoClient('localhost',27017,username='borntocode143',password='m00Bju04mIg6trXO')
db=client["quiz"]



# Define the collection


# ---------------- API Endpoints -------------------
@app.route("/", methods=['GET'])
def home():
    return "<h1>home page</h1>"

@app.route("/submit_questions", methods=['POST'])
def submit_questions():
    try:
        data = request.get_json()
        result = db.insert_one(data)
        print("DB connected and data inserted")
        return jsonify({"message": "Question submitted", "id": str(result.inserted_id)}), 201
    except PyMongoError as e:
        print(f"An error occurred: {e}")
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
