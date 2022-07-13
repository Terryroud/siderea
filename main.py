import os
import random

from flask import Flask, render_template, redirect, request, make_response
from data import db_session
from flask_restful import Api

from data import db_session
from data.constellations import Constellation
from data.forms import AnswerForm, Search
from data.resource import constellations_resource

app = Flask(__name__)

app.config["SECRET_KEY"] = "fsvfdbfjhfgbff"

api = Api(app)

api.add_resource(constellations_resource.CatalogResource, "/api/get/cons/<id>")
api.add_resource(constellations_resource.CatalogListResource, "/api/get/cons")


def main():
    db_session.global_init("db/kringe.db")


@app.route("/base")
def base():
    return render_template("base.html", title="base")


@app.route("/test", methods=['GET', 'POST'])
def test():
    data = []
    answers = []

    d = []

    db_sess = db_session.create_session()

    if request.method == "POST":
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


@app.route("/catalog", methods=['GET', 'POST'])
def catalog():
    form = Search()
    db_sess = db_session.create_session()
    if request.method == "POST":
        if form.validate_on_submit():
            data = db_sess.query(Constellation).filter(Constellation.title.like(f"%{form.title}%")).all()
    if request.method == "GET":
        data = db_sess.query(Constellation).all()

    return render_template('catalog.html', form=form, data=data)


@app.route("/learn", methods=['GET', 'POST'])
def learn():
    data = []
    answers = []

    d = []

    db_sess = db_session.create_session()

    if request.method == "POST":
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


@app.route("/teach/<int:type>", methods=['GET', 'POST'])
def teach(type):
    db_sess = db_session.create_session()

    if request.method == 'GET':
        type *= -1
        if type > 0:
            timer = 1
        else:
            timer = 0
            type *= -1

        if type == 4:  # северное полушарие
            data = db_sess.query(Constellation).filter(Constellation.polusharie == 1).all()
            answers = getAnswers(data)

        if type == 1:  # южное полушарие
            data = db_sess.query(Constellation).filter(Constellation.polusharie == 2).all()
            answers = getAnswers(data)

        if type == 2:  # все созвездия
            data = db_sess.query(Constellation).all()
            answers = getAnswers(data)

        if type == 3:  # 20 штук
            answers = []
            d = []
            data = []
            catalog = db_sess.query(Constellation).all()

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
                    question.append(catalog[id].id)

                random.shuffle(question)
                answers.append(question)
    else:

        data = eval(request.cookies.get(request.form.get('id')))
        cnt = 0
        obs = 0
        for i in data:
            obs += 1
            if i == data[i]:
                cnt += 1
        prc = cnt / obs

        return redirect(f"/result/{prc}")

    id = random.choice(range(0, 9876543))

    return render_template('teach.html', data=data, answers=answers, timer=timer, id=id)


def getAnswers(data):
    answers = []
    for i in data:
        question = []
        question.append(i.title)
        id = random.choice(range(1, 89))
        a = [i.id]
        while len(question) != 3 and id not in a:
            a.append(id)
            question.append(data[id].id)
        random.shuffle(question)
        answers.append(question)


@app.route('/cookie/<int:id>/<int:vopros>/<int:otvet>')
def cookie(id, vopros, otvet):
    res = make_response()
    info = {vopros: otvet}
    it = eval(request.cookies.get(str(id)))
    for i in it:
        info[i] = it[i]
    res.set_cookie(f'{id}', f"{info}", max_age=60 * 60 * 24 * 365 * 2)
    return res


@app.route('/getcookie')
def getcookie():
    cookies = eval(request.cookies.get('data'))
    if cookies is None:
        return []
    return cookies


app.add_url_rule('/test/<int:id>', view_func=test, methods=['GET', 'POST'])
app.add_url_rule('/learn/<int:id>', view_func=learn, methods=['GET', 'POST'])

if __name__ == "__main__":
    main()
    app.run()
    # app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
