from flask import Flask, request, jsonify
from flask import Blueprint, render_template
import requests
import json
import sys
sys.path.append(".")

from ESECAF.model.model import Population
from ESECAF.schema.schema import PopulationSchema
Population_schema = PopulationSchema()
Population_schema = PopulationSchema(many=True)

from ESECAF.model.model import Family
from ESECAF.schema.schema import FamilySchema
Family_schema = FamilySchema()
Family_schema = FamilySchema(many=True)


from ESECAF import db


ApiRoute = Blueprint('api',__name__)

class Api():
    @ApiRoute.route('/get-population',methods=['GET'])
    def get_population():

        all_Population = Population.query.all()
        result = Population_schema.dump(all_Population)
        return jsonify({
            "population": result
        })


    @ApiRoute.route('/post-population',methods=['POST'])
    def post_population():

        name =  request.values.get("name", type=str,)
        state = request.values.get("state", type=str )
        municipality =  request.values.get("municipality", type=str)
        tn = request.values.get("tn", type=int)
        tm = request.values.get("tm", type=int)

        new_population= Population(name,state,municipality,tn,tm)

        db.session.add(new_population)
        db.session.commit()
        return jsonify({
            "message": "Population created"
        })

    @ApiRoute.route('/put-population/<int:id>',methods=['PUT'])
    def put_population(id):
        update_population = Population.query.get(id)
        try:
            name =  request.values.get("name", type=str)
            state = request.values.get("state", type=str )
            municipality =  request.values.get("municipality", type=str)
            tn = request.values.get("tn", type=int)
            tm = request.values.get("tm", type=int)

            update_population.name = name
            update_population.state = state
            update_population.municipality = municipality
            update_population.tn = tn
            update_population.tm = tm

            db.session.commit()
            return jsonify({
            "message": "Population updated"
            })
        except:
            return jsonify({
            "message": "Population no found"
            })


    @ApiRoute.route('/delete-population/<int:id>',methods=['DELETE'])
    def delete_population(id):
        delete_population = Population.query.get(id)
        try:
            db.session.delete(delete_population)
            db.session.commit()
            return jsonify({
                "message": "Population deleted"
            })
        except:
            return jsonify({
            "message": "Population no found"
            })
# ! api de family

    @ApiRoute.route('/get-family/<int:id>',methods=['GET'])
    def get_family(id):
        Familia2 = Family.query.filter(Family.population_id == id)
        result = Family_schema.dump(Familia2)
        
        return jsonify(result)


