from flask import Flask, url_for, request, redirect, render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

with app.test_request_context():
    print url_for('hello', name='saul')