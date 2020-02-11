from wtforms import Form, StringField

class GifSearchForm(Form):
    search = StringField('')