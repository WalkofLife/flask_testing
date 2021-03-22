from flask import Flask

app = Flask(__name__)

@app.route('/')
def base_route():
    return 'Hello World'

@app.route('/hello/<int:number>', methods = ['POST',"GET"])
def hello(number):
    if number <10: return f"hello {number}",200
    if number >10: return f"hello {number}",202


if __name__ == '__main__':
    app.run(debug = True)
    