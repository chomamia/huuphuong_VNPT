from flask import Flask, render_template, request
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'huuphuongtp2@gmail.com'
app.config['MAIL_PASSWORD'] = 'qsyikfunngmdogxn'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/', methods= ['GET', 'POST'])
def home():
    if request.method == 'POST':
        nameTitle = request.form["title"]
        email = request.form["email"]
        msg = Message(nameTitle, sender='huuphuongtp2@gmail.com', recipients=[email])
        msg.body = request.form["decription"]
        mail.send(msg)
        return "Sent email"
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)