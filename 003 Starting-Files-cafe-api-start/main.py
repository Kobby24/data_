from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


def cafe_data(cafe):
    return {
        'can_take_calls': cafe.can_take_calls,
        'coffee_price': cafe.coffee_price,
        'has_sockets': cafe.has_sockets,
        'has_toilet': cafe.has_toilet,
        'has_wifi': cafe.has_wifi,
        'id': cafe.id,
        'img_url': cafe.img_url,
        'location': cafe.location,
        'map_url': cafe.map_url,
        'name': cafe.name,
        'seats': cafe.seats
    }


@app.route('/random')
def get_random_cafe():
    cafes = Cafe.query.all()
    rand_cafe = random.choice(cafes)
    cafe = cafe_data(rand_cafe)

    return jsonify({'cafe': cafe})


@app.route('/all')
def get_all_cafes():
    cafes = Cafe.query.all()
    all_cafes = [cafe_data(rand_cafe) for rand_cafe in cafes]
    return jsonify({'cafes': all_cafes})


@app.route('/search')
def cafe_search():
    query_loc = request.args.get('loc')
    cafe = Cafe.query.filter_by(location=query_loc).first()
    if cafe:
        return jsonify({'cafe': cafe_data(cafe)})
    else:
        return jsonify({"error": {'Not found': "Sorry, we don't have a cafe at that location"}})


@app.route('/add',methods=['POST','GET'])
def add_cafe():
    if request.method =='POST':
        cafe = Cafe(
            can_take_calls=bool(request.form.get('can_take_calls')),
            coffee_price=request.form.get('coffee_price'),
            has_sockets=bool(request.form.get('has_sockets')),
            has_toilet=bool(request.form.get('has_toilet')),
            has_wifi=bool(request.form.get('has_wifi')),
            img_url=request.form.get('img_url'),
            location=request.form.get('location'),
            map_url=request.form.get('map_url'),
            name=request.form.get('name'),
            seats=request.form.get('seats')
        )
        db.session.add(cafe)
        db.session.commit()
        return jsonify({'response':{'success':'Successfully added the cafe.'}})
    else:
        return jsonify({'response':{'error':'oops!'}})

@app.route('/update-price/<cafe_id>',methods=['PATCH'])
def update_price(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        new_price = request.args.get('new_price')
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify({'success':'Successfully Updated the price'})
    else:
        return jsonify({'error':{'Not found':'Sorry a cafe with that id was not found in the database.'}}), 404

@app.route('/report-closed/<cafe_id>',methods=['DELETE'])
def report_closed(cafe_id):
    cafe = db.session.get(Cafe,cafe_id)
    api_key=request.args.get('api-key')
    if cafe and api_key == 'TopSecretAPIKey':
        db.session.delete(cafe)
        db.session.commit()
        return jsonify({'Success':'Cafe successfully deleted'})
    elif api_key != 'TopSecretAPIKey':
        return jsonify({'error':'Sorry that is not allowed make sure you have the corrct api_key'}), 403
    else:
        return jsonify({'error':{'Not found':'Sorry a cafe with that id was not found in the database.'}}), 404




## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
