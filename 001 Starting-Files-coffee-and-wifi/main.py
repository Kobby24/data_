from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired,URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location URL',validators=[DataRequired(),URL()])
    open_time = StringField('Open time',validators=[DataRequired()])
    close_time = StringField('Closing time',validators=[DataRequired()])
    coffee_rating = SelectField('Coffee rating',choices=[('0','✘'),('1','☕️'),('2','☕️☕️'),('3','☕️☕️☕️'),('4','☕️☕️☕️☕️'),('5','☕️☕️☕️☕️☕️')],validators=[DataRequired()])
    wifi_rating = SelectField('Wifi rating',choices=[('0','✘'),('1','💪'),('2','💪💪️'),('3','💪️💪️💪️'),('4','💪💪️💪💪'),('5','💪️💪️💪💪️💪')],validators=[DataRequired()])
    power_outlet = SelectField('Power outlet rating fields',choices=[('0','✘'),('1','🔌'),('2','🔌🔌'),('3','🔌🔌️🔌'),('4','🔌🔌️🔌🔌'),('5','🔌🔌🔌🔌🔌')],validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=['POST','GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        coffee = ''
        power = ''
        wifi = ''
        if int(form.coffee_rating.data) > 0:
            for i in range(int(form.coffee_rating.data)):
                coffee+='☕️'
        else:
            coffee+='✘'
        if int(form.wifi_rating.data) > 0:
            for i in range(int(form.wifi_rating.data)):
                wifi+='💪'
        else:
            wifi+='✘'

        if int(form.power_outlet.data) > 0:
            for i in range(int(form.power_outlet.data)):
                power+='🔌'
        else:
            power+='✘'
        input_data = f"\n{form.cafe.data},{form.location.data},{form.open_time.data},{form.close_time.data},{coffee},{wifi},{power}"
        with open(file='cafe-data.csv',mode="a",encoding='utf-8') as file:
            file.write(input_data)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='',encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
