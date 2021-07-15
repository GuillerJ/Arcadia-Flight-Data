from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from hashlib import md5



amigos = db.Table('relacion',
        db.Column('usuario_id', db.Integer, db.ForeignKey('usuario.id')),
        db.Column('relacionUsuario_id', db.Integer, db.ForeignKey('usuario.id')),
        db.Column('fechaCreacion', db.DateTime, index=True, default=datetime.now)
)

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(64), index=True, unique=True)
    correo = db.Column(db.String(120), index=True, unique=True)
    clave_h = db.Column(db.String(128))
    ultimaConexion = db.Column(db.DateTime, index=True, default=datetime.now)
    descripcion = db.Column(db.String(140))
    #relacion_o = db.relationship('Relacion', backref='id', lazy='dynamic')


    def __repr__(self):
        return '<Usuario {}>'.format(self.usuario)

    def set_password(self, password):
        self.clave_h = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.clave_h, password)

    def avatar(self, size):
        digest = md5(self.correo.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


@login.user_loader
def load_user(id):
    return Usuario.query.get(int(id))
