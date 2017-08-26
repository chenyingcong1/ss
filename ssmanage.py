from flask import Flask,url_for,render_template,redirect,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')

    elif request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if username=='123'and password=='abc':
            return redirect(url_for('main'))
        else:
            return redirect(url_for('login',method='GET'))

@app.route('/main/',methods=['GET','POST'])
def main():
    if request.method=='GET':
        return render_template('dashboard.html')


if __name__ == '__main__':
    app.run()
