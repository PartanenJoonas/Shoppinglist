from flask import Flask, render_template, request, send_file, redirect

app = Flask(__name__)
app.static_folder = 'static'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
