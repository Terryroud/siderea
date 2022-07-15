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
    db_session.global_init(os.path.join("db", "qwer.db"))



@app.route("/base")
def base():
    db_sess = db_session.create_session()
    print(db_sess.query(Constellation).all())
    return render_template("base.html", title="base")


@app.route("/test", methods=['GET', 'POST'])
def test():
    return render_template('test.html')


@app.route("/catalog", methods=['GET', 'POST'])
def catalogg():
    form = Search()
    db_sess = db_session.create_session()
    if request.method == "POST":
        if form.validate_on_submit():
            data = db_sess.query(Constellation).filter(Constellation.title.like(f"%{form.search}%")).all()
    if request.method == "GET":
        data = db_sess.query(Constellation).all()
    data = db_sess.query(Constellation).all()
    print(data)
    return render_template('catalog.html', form=form, data=data, dlina=len(data))


@app.route("/learn", methods=['GET', 'POST'])
def learn():
    return render_template('learn.html')


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

                question.append(catalog[d1].id)
                id = random.choice(range(1, 89))
                a = [d1]
                while len(question) != 3 and id not in a:
                    a.append(id)
                    print(id)
                    question.append(catalog[id].id)

                random.shuffle(question)
                answers.append(question)
    else:

        id = request.form.get('id')
        print(id)
        data = getcookie(id)
        cnt = 0
        obs = 0
        for i in data:
            obs += 1
            if i == data[i]:
                cnt += 1
        prc = cnt / obs

        return redirect(f"/result/{prc}")

    id = random.choice(range(100000, 98966376543))
    print(list(map(lambda x: x.id, data)))
    print(len(data), len(answers))
    titles = []
    for i in answers:
        b = []
        for j in i:
            item = db_sess.query(Constellation).filter(Constellation.id==j).all()[0]
            b.append(item.title)
        titles.append(b)
    return render_template('teach.html', data=data, answers=answers, timer=timer, id=id, dlina=len(data), titles=titles)


def getAnswers(data):
    answers = []
    for i in data:
        question = []
        question.append(i.id)
        id = random.choice(range(1, 89))
        a = [i.id]
        while len(question) != 3 or id not in a:
            a.append(id)
            question.append(id)
            id = random.choice(range(1, 89))
            if len(question) == 3:
                break
        random.shuffle(question)
        answers.append(question)
    return answers


@app.route('/cookie/<int:id>/<int:vopros>/<int:otvet>')
def cookie(id, vopros, otvet):
    res = make_response()
    info = {vopros: otvet}
    if request.cookies.get(str(id)) is not None:
        it = eval(request.cookies.get(str(id)))
    else:
        it = {}
    for i in it:
        info[i] = it[i]
    res.set_cookie(f'{id}', f"{info}", max_age=60 * 60 * 24 * 365 * 2)
    print(info)
    return res


@app.route('/teach/cookie/<int:id>/<int:vopros>/<int:otvet>')
def cookie1(id, vopros, otvet):
    res = make_response()
    info = {vopros: otvet}
    it = eval(request.cookies.get(str(id)))
    for i in it:
        info[i] = it[i]
    res.set_cookie(f'{id}', f"{info}", max_age=60 * 60 * 24 * 365 * 2)
    print(info)
    return res


@app.route('/getcookie/<int:id>')
def getcookie(id):
    if request.cookies.get(id) != None:
        cookies = eval(request.cookies.get(id))
    else:
        cookies = None
    if cookies is None:
        return []
    return cookies


@app.route("/constellation/<int:id>", methods=['GET'])
def infocons(id):

    db_sess = db_session.create_session()
    data = db_sess.query(Constellation).filter(Constellation.id == id).all()[0].to_dict()

    return render_template('constellation.html', object=data)



@app.route('/result/<string:result>', methods=['GET'])
def result(result):
    
    return render_template('result.html', res=result)


app.add_url_rule('/test/<int:id>', view_func=test, methods=['GET', 'POST'])
app.add_url_rule('/learn/<int:id>', view_func=learn, methods=['GET', 'POST'])

if __name__ == "__main__":
    main()
    app.run()
    # app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
