from flask import Flask, jsonify, request, render_template
from models import Cupcake, connect_db, db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/api/cupcakes', methods=['GET'])
def get_all_cupcakes():
    cupcakes = [cupcake.serializeCupcake() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET'])
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id).serializeCupcake()
    return jsonify(cupcake=cupcake)


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    cupcake = Cupcake()
    cupcake.flavor = request.json.get('flavor')
    cupcake.size = request.json.get('size')
    cupcake.rating = request.json.get('rating')
    cupcake.image = request.json.get('image') if request.json.get('image') else None

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.serializeCupcake()), 201


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json.get('flavor')
    cupcake.size = request.json.get('size')
    cupcake.rating = request.json.get('rating')
    cupcake.image = request.json.get('image')

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.serializeCupcake())


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(cupcake=f'Successfully deleted cupcake with id = {cupcake.id}')
