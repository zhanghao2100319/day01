from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def index():
    return "hello world"


print("hello world")


@app.route("/delete")
def delete():
    return "hello"


num = 3

if __name__ == "__main__":
    app.run()
