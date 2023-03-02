from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session
        self.model = Genre

    def get_all(self):
        return self.session.query(self.model).all()

    def get_by_id(self, did):
        return self.session.query(self.model).get(did)

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, data):
        gid = data['id']
        genre = self.get_by_id(gid)
        genre.name = data['name']
        self.session.add(genre)
        self.session.commit()

    def delete(self, gid):
        genre = self.get_by_id(gid)
        self.session.delete(genre)
        self.session.commit()
