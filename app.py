from flask import Flask,redirect,render_template,request,url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app,expose_headers=["ngrok-skip-browser-warning"])

@app.after_request
def after_response(response):
    response.headers['ngrok-skip-browser-warning'] = 'true'
    return response

@app.route('/g')
def home ():
    return "Hello world"

@app.route('/')
def refults():
    return render_template('index.html')

@app.route('/semresults',methods=['POST'])
def semresults():
    return render_template('sem.html')

if __name__ == '__main__':
    app.run(debug=True)