from flask import Flask, request, jsonify

app = Flask(__name__)

# root get
@app.route("/")
def root():
    return {"message": "Hello World"}


# set port
if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
