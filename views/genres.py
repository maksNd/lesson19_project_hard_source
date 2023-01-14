from flask_restx import Resource, Namespace
from flask import request

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        data_for_genre = request.json
        genre = genre_service.create(data_for_genre)
        return '', 201, {"location": f"/genres/{genre.id}"}


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    def put(self, rid):
        data_for_genre = request.json
        if "id" not in data_for_genre:
            data_for_genre["id"] = rid
        genre_service.update(data_for_genre)
        return "", 204

    def delete(self, rid):
        genre_service.delete(rid)
        return '', 204
