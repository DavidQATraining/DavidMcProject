from flask import Flask, redirect, url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ

from forms import FightersForm
app = Flask(__name__)

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

@app.route('/')
@app.route('/home')
def home():
    post_data = Fighters.query.all()
    return render_template('homepage.html', title='Homepage', posts=post_data)


@app.route('/about')
def about():
    return render_template('aboutpage.html', title='About')


@app.route('/add', methods=['GET', 'POST'])
def create():
    form = FightersForm()
    if form.validate_on_submit():
        post_data = Fighters(
            f_name=form.f_name.data,
            l_name=form.l_name.data,
            age=form.age.data,
            weightclass=form.weightclass.data,
            record=form.record.data,
            lastfive=form.lastfive.data
        )
        db.session.add(post_data)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('create.html', title='Create a thing', form=form)

# GET - which displays data
# POST - which sends data from website to application
# DELETE - deletes some data
# Insert - sends data, but more used for updating

@app.route('/create')
def create():
    db.create_all()
    post = Fighters(f_name='David', l_name='McCartney', age=22, content='blah blah blah')
    post1 = Fighters(f_name='Bavid', l_name='Cartney', title='What teh geez', content='whooh blah blah')
    db.session.add(post)
    db.session.add(post1)
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




