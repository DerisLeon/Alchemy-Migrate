from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pwebii:suasenha@localhost:5432/aemotor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Usuario(db.Model):
    __tablename__ = "tb_usuario"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nascimento = db.Column(db.Date, nullable=True)
    created = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return '<Usuario %r>' % self.username


class Endereco(db.Model):
    __tablename__ = "tb_endereco"
    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Endereco %r>' % self.logradouro
    
class Prefeitura(db.Model):
    __tablename__ = "tb_prefeitura"
    id = db.Column(db.Integer, primary_key=True)
    prefeito = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Prefeitura %r>' % self.prefeito