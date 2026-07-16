from flask import Flask, jsonify
from flask_cors import CORS

from main import get_company_analysis  # function you already have
from setup_database import setup_database

app = Flask(__name__)
CORS(app)  # allow frontend to call backend

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "Bluestocks API is running"})

@app.route("/api/company/<company_id>", methods=["GET"])
def company_data(company_id):
    try:
        result = get_company_analysis(company_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    setup_database()
    app.run(debug=False, host="127.0.0.1", port=5000)
