
from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path
from database import initialize_database, save_bill, get_all_bills

app = Flask(__name__)

PROJECT_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = PROJECT_DIR / "frontend"

initialize_database()


@app.get("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.get("/<path:filename>")
def frontend_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)


@app.post("/api/bills")
def create_bill():
    data = request.get_json(silent=True) or {}

    description = str(data.get("description") or "Shared bill").strip()
    amount = data.get("amount")
    people = data.get("people")

    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        return jsonify({"error": "Enter a valid bill amount."}), 400

    if amount <= 0 or amount > 1_000_000_000:
        return jsonify({"error": "Bill amount must be positive and within the limit."}), 400

    if not isinstance(people, int) or isinstance(people, bool) or not 1 <= people <= 10000:
        return jsonify({"error": "Enter a valid number of people."}), 400

    if not description:
        description = "Shared bill"

    share = round(amount / people, 2)

    bill_id = save_bill(description, amount, people, share)

    return jsonify({
        "id": bill_id,
        "description": description,
        "amount": amount,
        "people": people,
        "share": share
    }), 201


@app.get("/api/bills")
def list_bills():
    return jsonify(get_all_bills())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
