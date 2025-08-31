from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello_world():
    return 'Hello to python!'


if __name__ == "__main__":
    app.run(debug = True)