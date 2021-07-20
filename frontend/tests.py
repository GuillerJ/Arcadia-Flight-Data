from datetime import datetime, timedelta
import unittest
from app import app, db
from app.modelos import Usuario

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = Usuario(usuario='Pepe')
        u.set_password('pepa')
        self.assertFalse(u.check_password('si'))
        self.assertTrue(u.check_password('pepa'))

    def test_avatar(self):
        u = Usuario(usuario='zxcv', correo='zxcv@zxcv.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
                                         'd4c74594d841139328695756648b6bd6'
                                         '?d=identicon&s=128'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
