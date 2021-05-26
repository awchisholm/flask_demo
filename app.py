from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'This is an example Flask application serving static content by Andrew'

if __name__ == '__main__':
    app.run()