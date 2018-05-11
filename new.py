from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('login.html')

@app.route('/nextpage',methods=['POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        file=open("C:/Users/Kamal's/Desktop/flaskapp/templates/new.txt",'w')
        file.write(username)
        file.write(password)
    return render_template('nextpage.html')
if __name__ == '__main__':
	app.run(debug=True)