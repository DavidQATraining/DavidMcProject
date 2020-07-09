from flask import Flask, redirect, url_for, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_login import login_manager, LoginManager, current_user, login_user, login_required, UserMixin, logout_user
from flask_bcrypt import Bcrypt
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from datetime import datetime

from forms import FightersForm, RegistrationForm, LoginForm

app = Flask(__name__)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
login_manager.login_view = 'login'

# 2a02:c7f:8ee9:1800:95f3:9430:14e8:cf52     94.11.43.81        my IP
# 3a617fb3dde7803d7e4513616c2973ee secret key


# make more secure
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Fighters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    weightclass = db.Column(db.String(20), nullable=False)
    record = db.Column(db.String(8), nullable=False)
    lastfive = db.Column(db.String(5), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return "".join(
            [
                'Name: ' + self.f_name + ' ' + self.l_name + '\n'
                'Age: ' + self.age + '\n'
                'Weightclass: ' + self.weightclass + '\n'
                'Record: ' + self.record + '\n'
                'Last Five: ' + self.age + '\n'

            ]
        )


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    fighters = db.relationship('Fighters', backref='author', lazy=True)

    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])


def validate_email(self, email):
    user = Users.query.filter_by(email=email.data).first()

    if user:
        raise ValidationError('Email already in use')




@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    #if current_user.is_authenticated:
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(f_name=form.f_name.data, l_name=form.l_name.data, email=form.email.data, password=hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
    #return redirect(url_for('home'))


@app.route('/')
@app.route('/home')
def home():
    post_data = Fighters.query.all()
    return render_template('home.html', title='Homepage', posts=post_data)


@app.route('/about')
def about():
    return render_template('aboutpage.html', title='About')


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = FightersForm()

    if form.validate_on_submit():
        post_data = Fighters(
            f_name=form.f_name.data,
            l_name=form.l_name.data,
            age=form.age.data,
            weightclass=form.weightclass.data,
            record=form.record.data,
            lastfive=form.lastfive.data,
            user_id=Users.get_id(current_user)
        )
        db.session.add(post_data)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('addfighter.html', title='Add a fighter', form=form)


# GET - which displays data
# POST - which sends data from website to application
# DELETE - deletes some data
# Insert - sends data, but more used for updating

@app.route('/createFighter')
def createFighter():
    db.create_all()
    fighter = Fighters(f_name='Jorge', l_name='Masvidal', age=35, weightclass='Welterweight', record='35-13-0',
                       lastfive='WWWLL', user_id=1)
    fighter1 = Fighters(f_name='Kamaru', l_name='Usman', age=33, weightclass='Welterweight', record='16-1-0',
                        lastfive='WWWWW', user_id=1)
    db.session.add(fighter)
    db.session.add(fighter1)

    db.session.commit()
    return 'Added the table and populated it with some records'


@app.route('/createUser')
def createUser():
    db.create_all()
    user = Users(f_name='David', l_name='McCartney', email='DavidMc@email.com', password='pass1')
    db.session.add(user)

    db.session.commit()
    return 'Added the table and populated it with some records'


@app.route('/delete')
def delete():
    db.drop_all()
    # db.session.query(Posts).delete()
    db.session.commit()
    return 'Everything is gone! Whoops!'


if __name__ == '__main__':
    app.run()
