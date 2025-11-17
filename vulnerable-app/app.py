from flask import Flask
import requests
app = Flask(__name__)
@app.route("/run/<code>")
def run_code(code):
    return str(eval(code))
@app.route("/get")
def fetch():
    return requests.get("http://example.com").text
if __name__ == "__main__":
    app.run(debug=True)
