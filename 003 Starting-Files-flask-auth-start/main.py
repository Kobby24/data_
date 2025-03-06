import werkzeug.security
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        new_user = User()
        if User.query.filter_by(email=request.form['email']).first():
            flash("You've already signed up with that email, log in instead")
            return redirect(url_for('login'))
        else:
            new_user.email = request.form['email']
            new_user.password = generate_password_hash(request.form['password'], 'pbkdf2:sha256', 8)
            new_user.name = request.form['name']
            db.session.add(new_user)
            db.session.commit()
            user = User.query.filter_by(email=request.form['email']).first()
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method  == 'POST':
        form = request.form['email']
        user = User.query.filter_by(email=form).first()
        if user and check_password_hash(user.password,request.form['password']):
            login_user(user)
            return redirect(url_for('secrets'))
        elif not user:
            flash("That Email doesn't exist, please try again")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password,request.form['password']):
            flash("Incorrect Password")
            return redirect(url_for('login'))
    return render_template("login.html")





@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html",name=current_user.name,login=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route('/download')
@login_required
def download():
    return send_from_directory('static', 'files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
