from app import app
from setup_db import db
from dao.model.user import User


def create_data(app, db):
    with app.app_context():
        db.create_all()

        u1 = User(username="vasya", password="my_little_pony", role="user")
        u2 = User(username="oleg", password="qwerty", role="user")
        u3 = User(username="oleg", password="P@ssw0rd", role="admin")

        with db.session.begin():
            db.session.add_all([u1, u2, u3])


create_data(app, db)
