from flask import Flask, request, jsonify
from flask_migrate import Migrate
from config import Config
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/heroes')
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict(only=('id', 'name', 'super_name')) for hero in heroes])

@app.route('/heroes/<int:id>')
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    
    return jsonify(hero.to_dict(only=('id', 'name', 'super_name', 'hero_powers.id', 'hero_powers.hero_id', 'hero_powers.power_id', 'hero_powers.strength', 'hero_powers.power.id', 'hero_powers.power.name', 'hero_powers.power.description')))

@app.route('/powers')
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict(only=('id', 'name', 'description')) for power in powers])

@app.route('/powers/<int:id>')
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    
    return jsonify(power.to_dict(only=('id', 'name', 'description')))

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    
    data = request.get_json()
    
    try:
        if 'description' in data:
            power.description = data['description']
        db.session.commit()
        return jsonify(power.to_dict(only=('id', 'name', 'description')))
    except ValueError as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    
    try:
        hero_power = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        db.session.add(hero_power)
        db.session.commit()
        
        return jsonify(hero_power.to_dict(only=('id', 'hero_id', 'power_id', 'strength', 'hero.id', 'hero.name', 'hero.super_name', 'power.id', 'power.name', 'power.description'))), 201
    except (ValueError, KeyError) as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400

if __name__ == '__main__':
    app.run(debug=True)