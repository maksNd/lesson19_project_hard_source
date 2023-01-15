from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_data):
        user = User(**user_data)
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user_data):
        user = self.get_one(user_data.get('id'))
        user.id = user_data.get('id')
        user.username = user_data.get('username')
        user.password = user_data.get('password')
        user.role = user_data.get('role')

        self.session.add(user)
        self.session.commit()

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def check_login_pasword(self, login, password):
        user = self.session.query(User).filter(User.username == login).first()
        if user is None:
            return False
        if user.password != password:
            return False
        return True

    # def check_user(self, login, password):
    #     if self.get_by_login(login).password == password:
    #         return True
    #     return False

# from setup_db import db
# from flask import Flask
# app = Flask(__name__)
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# db.init_app(app)
# test_user = UserDAO(db.session)
#
# with app.app_context():
#     print(test_user.get_all())
