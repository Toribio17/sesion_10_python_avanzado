from flask import Flask
app = Flask(__name__)
app.full_dispatch_request = True


@app.route('/hello/', methods=['GET', 'POST'])
def hello_world():
    print("hello")
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001)


