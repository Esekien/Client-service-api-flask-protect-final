from flask import Flask, request, jsonify, redirect, flash
from flask import Blueprint, render_template
import requests
import json
import sys
sys.path.append(".")

from ESECAF.model.model import Population
from ESECAF.schema.schema import PopulationSchema
Population_schema = PopulationSchema()
Population_schema = PopulationSchema(many=True)


from ESECAF import db


ProyectRoute = Blueprint('proyect',__name__)

class Proyect():
    @ProyectRoute.route('/',methods=['GET','POST'])
    def index():
        if request.method == 'POST':
            name = request.form['name']
            state = request.form['state']
            municipality = request.form['municipality']
            tn = request.form['tn']
            tm = request.form['tm']
            payload = {'name': name, 'state': state, 'municipality': municipality, 'tn': tn, 'tm':tm}
            url = 'http://127.0.0.1:5000/api/post-population'
            response = requests.post(url,data=payload)
            flash('creado correctamente')
            return redirect('/#poblaciones')


        url = 'http://127.0.0.1:5000/api/get-population'
        response = requests.request("GET",url)
        response_data = response.json()
        return render_template('index.html', datos = response_data)

    @ProyectRoute.route('/methods/<int:id>')
    def methods(id):

        url = 'http://127.0.0.1:5000/api/delete-population' + '/' + str(id)
        print(url)
        response = requests.delete(url)
        flash('eliminado correctamente')
        return redirect('/#poblaciones')

    @ProyectRoute.route('/put',methods=['POST'])
    def put():
        if request.method == 'POST':
            data = request.json
            id =  data['id']
            name = data['name']
            state = data['state']
            municipality = data['municipality']
            tn = data['tn']
            tm = data['tm']

            payload = {'name': name, 'state': state, 'municipality': municipality, 'tn': tn, 'tm':tm}

            url = 'http://127.0.0.1:5000/api/put-population' + '/' + str(id)
            response = requests.put(url,data=payload)
            
            
            flash('Actualizado correctamente')
            
            return json.JSONEncoder().encode(data)
    @ProyectRoute.route('/familiar/<int:id>',methods=['GET'])
    def getfamili(id):
        if request.method == 'GET':
            url = 'http://127.0.0.1:5000/api/get-family' + '/' + str(id)
            response = requests.get(url)
            
            data = Population_schema.dump(response)
            return json.JSONEncoder().encode(data)




