import random

from flask import Flask, render_template, redirect, request
# from data import db_session
from data import db_session
from data.constellations import Constellation

app = Flask(__name__)

app.config["SECRET_KEY"] = "fsvs-34-dvsdvsdvpoiuytra"


def main():
    db_session.global_init("db/hestia_main.db")
    app.run(host="127.0.0.1", port=5000)


@app.route("/base")
def base():
    return render_template("base.html", title="Yfodfybt")


@app.route("/test", methods=['GET', 'POST'])
def test():
    form =
    if request.method == "POST":


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


@app.route("/catalog", methods=['GET'])
def catalog():
    catalog = []

    db_sess = db_session.create_session()

    catalog = db_sess.query(Constellation).all()  # запрос всех элементов из таблички

    return render_template('catalog.html', catalog=catalog)


@app.route("/cons/<int:id>", methods=['GET', 'POST'])
def learn(id):    #не на время

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



    return render_template('learn.html', data=data)


if __name__ == "__main__":
    main()
