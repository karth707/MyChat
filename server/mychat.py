from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form action="/getIP" method="post">
            <p><input type=text name=IP>
            <p><input type=submit value=submit>
     </form> '''

@app.route('/getIP', methods=['POST'])
def getip():
    return request.form['IP']

app.run()


