import os
import random

from flask import Flask, render_template, redirect, request
# from data import db_session
from flask_restful import Api

from data import db_session
from data.constellations import Constellation
from data.forms import AnswerForm, Search
from data.resource import constellations_resource

app = Flask(__name__)

app.config["SECRET_KEY"] = "fsvfdbfjhfgbff"


# api = Api(app)
# api.add_resource(cuisine_resource.CuisineListResource, "/api/get/cuisine")
# api.add_resource(cuisine_resource.CuisineResource, "/api/get/cuisine/<id>")
# api.add_resource(cuisine_resource.CuisineCategoryResource, "/api/get/cuisine/<category>")

# api.add_resource(products_resource.ProductsResource, "/api/get/products/<id>")
# api.add_resource(products_resource.ProductsListResource, "/api/get/products")

api = Api(app)
# >>>>>>> db241f785e97f53f636dfc906e1bfe12201a5677

api.add_resource(constellations_resource.CatalogResource, "/api/get/cons/<id>")
api.add_resource(constellations_resource.CatalogListResource, "/api/get/cons")


def main():
    db_session.global_init("db/kringe.db")


@app.route("/base")
def base():
    return render_template("base.html", title="base")


@app.route("/test", methods=['GET', 'POST'])
def test():
    form = AnswerForm()
    if request.method == "POST":
        pass

    data = []
    answers = []

    db_sess = db_session.create_session()

    catalog = db_sess.query(Constellation).all()

    d = []

    for i in range(20):
        d1 = random.choice(range(1, 89))
        while d1 in d:
            d1 = random.choice(range(1, 89))
        d.append(d1)
        data.append(catalog[d1])

        question = []

        question.append(catalog[d1].title)
        id = random.choice(range(1, 89))
        a = [d1]
        while len(question) != 3 and id not in a:
            a.append(id)
            question.append(catalog[id].title)

        random.shuffle(question)
        answers.append(question)

    return render_template('test.html', data=data, answers=answers)


@app.route("/catalog", methods=['GET', 'POST'])
def catalog():
    form = Search()
    db_sess = db_session.create_session()
    if request.method == "POST":
        if form.validate_on_submit():
            data = db_sess.query(Constellation).filter(Constellation.title.like(f"%{form.title}%")).all()
    if request.method == "GET":
        data = db_sess.query(Constellation).all()

    return render_template('catalog.html', form=form, data=data, dlina=len(data))


@app.route("/learn/<int:type>", methods=['GET', 'POST'])
def learn(id):
    if request.method == "POST":
        pass
    data = []
    answers = []

    d = []

    db_sess = db_session.create_session()

    data = db_sess.query(Constellation).filter(Constellation.id == id).all()[0].to_dict()

    for i in range(20):
        d1 = random.choice(range(1, 89))
        while d1 in d:
            d1 = random.choice(range(1, 89))
        d.append(d1)
        data.append(catalog[d1])

        question = []

        question.append(catalog[d1].title)
        id = random.choice(range(1, 89))
        a = [d1]
        while len(question) != 3 and id not in a:
            a.append(id)
            question.append(catalog[id].title)

        random.shuffle(question)
        answers.append(question)
        if request.method == "GET":
            pass

    return render_template('learn.html', data=data)


app.add_url_rule('/test/<int:id>', view_func=test, methods=['GET', 'POST'])
app.add_url_rule('/learn/<int:id>', view_func=learn, methods=['GET', 'POST'])

if __name__ == "__main__":
    main()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
