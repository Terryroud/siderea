import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Star(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "stars"

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    m = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    constellation = sqlalchemy.Column(sqlalchemy.Integer)
    mabs = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)


