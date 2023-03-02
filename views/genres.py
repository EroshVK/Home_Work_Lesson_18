from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
from implemented import genre_service

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        result = GenreSchema(many=True).dump(genres)
        return result, 200


@genres_ns.route('/<int:gid>')
class GenresView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        genre_data = GenreSchema().dump(genre)
        return genre_data, 200
