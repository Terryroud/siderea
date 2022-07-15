import wtforms
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField, BooleanField


class AnswerForm(FlaskForm):
    answer1 = wtforms.BooleanField(id='answer1')
    answer2 = wtforms.BooleanField(id='answer2')
    answer3 = wtforms.BooleanField(id='answer3')
    submit = SubmitField()


class Search(FlaskForm):
    search = StringField(id='search')
    submit = SubmitField()

