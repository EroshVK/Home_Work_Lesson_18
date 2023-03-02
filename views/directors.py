from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from implemented import director_service

directors_ns = Namespace('directors')


@directors_ns.route('/')
class GenresView(Resource):
    def get(self):
        directors = director_service.get_all()
        result = DirectorSchema(many=True).dump(directors)
        return result, 200


@directors_ns.route('/<int:did>')
class MoviesView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        genre_data = DirectorSchema().dump(director)
        return genre_data, 200