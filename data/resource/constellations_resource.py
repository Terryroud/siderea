from data.constellations import Constellation

from flask import jsonify
from flask_restful import Resource, abort
from data.constellations import Constellation
from data import db_session


class CatalogResource(Resource):
    def get(self, id: int):
        session = db_session.create_session()
        con = session.query(Constellation).get(id)
        info = con.to_dict()
        return jsonify(info)


class CatalogListResource(Resource):
    def get(self):
        session = db_session.create_session()
        data = session.query(Constellation).all()
        a = []
        for item in data:
            info = item.to_dict()
            a.append(info)
        return jsonify(a)


