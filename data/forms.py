from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField, BooleanField


#class Stars(FlaskForm):
    #title = StringField(id="title")
  #  m = IntegerField(id="m")
  #  constellation = IntegerField(id="constellation")
   # mabs = IntegerField(id="alpha")
  #  submit = SubmitField()


class Constellations(FlaskForm):
    title = StringField(id="title")
    image = StringField(id="image")
    declination = StringField(id="declination")
    polusharie = IntegerField(id="polusharie")
    ascent = StringField(id="ascent")
    info = StringField(id="info")
    lat = StringField(id="lat")
    submit = SubmitField()
