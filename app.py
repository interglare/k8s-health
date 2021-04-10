from flask import Flask,jsonify
app = Flask(__name__)

@app.route("/")
@app.route("/health")
def main():
    content = {
      "status": "OK"
    }
    resp = jsonify(content)
    resp.status_code = 200
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8000')
