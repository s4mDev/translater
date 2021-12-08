from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return render_template('index.html',name=name)


@app.route('/hello/<name>')
def hello_with_name(name):
    return f"hello {name}"



if __name__ == '__main__':
    app.run()
