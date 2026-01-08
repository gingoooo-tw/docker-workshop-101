from flask import Flask, request, jsonify

app = Flask(__name__)

@app.post("/echo")
def echo():
    """回傳使用者送來的 JSON"""
    data = request.get_json()
    return jsonify({
        "status": "success",
        "received": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)