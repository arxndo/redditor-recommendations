from wtforms import Form, StringField, SelectField

class RedditorSearchForm(Form):
    choices = [('Username', 'Username'), \
                ('Subreddit', 'Subreddit')]
    select = SelectField('', choices=choices)
    search = StringField('')
