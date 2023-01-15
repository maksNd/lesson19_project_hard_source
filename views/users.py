from flask_restx import Resource, Namespace
from flask import request, abort

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        users = user_service.get_all()
        result = UserSchema(many=True).dump(users)
        return result, 200

    def post(self):
        data_for_user = request.json
        user = user_service.create(data_for_user)
        return '', 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        result = UserSchema().dump(user)
        return result, 200

    def put(self, uid):
        data_for_user = request.json
        if 'id' not in data_for_user:
            data_for_user['id'] = uid
        user_service.update(data_for_user)
        return '', 204

    def delete(self, uid):
        user_service.delete(uid)
        return '', 204


@user_ns.route('/auth')
class UserAuth(Resource):
    def post(self):
        data = request.json
        login = data.get('username')
        password = data.get('password')
        if user_service.check_user({'login': login, 'password': password}) is False:
            abort(400)
        else:
            return user_service.generate_tokens(), 200

    def put(self):
        refresh_token = request.json
        if user_service.check_refresh_token(refresh_token) is False:
            abort(400)
        else:
            return user_service.generate_tokens(), 200
