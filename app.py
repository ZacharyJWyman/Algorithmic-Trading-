from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\19712\\OneDrive\\Desktop\\alpaca\\storage.db'

db = SQLAlchemy(app)

class Storage(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

db.create_all()

@app.route("/")
def index():
    syms = Storage.query.all()
    return render_template('index.html', syms = syms)

@app.route('/add', methods = ['POST'])
def add():
    sm = Storage(text = request.form['symbol'], complete = False)
    db.session.add(sm)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete', methods = ['POST'])
def delete():
    db.session.delete()
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)