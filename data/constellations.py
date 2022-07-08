import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Constellation(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "constellations"

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    polusharie = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    declination = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ascent = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    info = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    lat = sqlalchemy.Column(sqlalchemy.String, nullable=True)
