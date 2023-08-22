from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from decode_qr import decode_qr_from_base64

app = Flask(__name__)
CORS(app)

@app.route("/decode_qr", methods=["POST"])
def decode_qr():
    try:
        print("Received POST request")

        base64_data = request.json.get("img")
        qr_data = decode_qr_from_base64(base64_data)
        print(qr_data)

        return jsonify({"qr_data": qr_data})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
