from flask import Flask, render_template, request, send_file, redirect
from flask_htpasswd import HtPasswdAuth
import subprocess
import os as os

app = Flask(__name__)
app.static_folder = 'static'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['FLASK_HTPASSWD_PATH'] = '/home/pi/.htpasswd'
app.config['FLASK_AUTH_ALL'] = True

htpasswd = HtPasswdAuth(app)

@app.route('/', methods=['GET', 'POST'])

def home():
    
    input_item=""
    if request.method == 'POST':
        input_item = request.form['item']
        with open("static/ostoslista.txt", "a+") as f:
            f.write(str(input_item) +"\n")
            
    return render_template("index.html")
    
    
@app.route('/static/ostoslista.txt')
def asd():
    return send_file('static/ostoslista.txt')

@app.route('/config.json')
def qwe():
    return send_file('static/js/config.json')

@app.route('/newlist')
def newfile():
    subprocess.call(['/home/pi/ostoslista_app/newfile.bash'], shell=True)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
