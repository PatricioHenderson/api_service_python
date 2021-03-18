#!/usr/bin/env python

import traceback
import io
import sys
import os
import base64
import json
import sqlite3
from datetime import datetime, timedelta
from flask import Flask, request, jsonify, render_template, Response, redirect
from usuarios_orm import db
import usuarios_orm as usuarios
from config import config

# Crear el server Flask
app = Flask(__name__)
# Obtener la path de ejecución actual del script
script_path = os.path.dirname(os.path.realpath(__file__))

# Obtener los parámetros del archivo de configuración
config_path_name = os.path.join(script_path, 'config.ini')
db_config = config('db', config_path_name)
server_config = config('server', config_path_name)

# Indicamos al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_config['database']}"
# Asociamos nuestro controlador de la base de datos con la aplicacion
db.init_app(app)

@app.route('/titles<id>', methods=['GET'])
def titles(id):
    try:
        data = usuarios.title_completed_count(id)
        return jsonify(data)

    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route('/user/graph', methods =['GET'])
def graph():
    try:
        data = usuarios.title_completed_count()
        return jsonify(data)
    
    except:
        return jsonify({'trace' : traceback.format_exc()})

'''
__[GET] /user/graph__
- Esta ruta es la encargada a informar el reporte y comparativa de cuantos títulos completó cada usuario en un gráfico.
Debe obtener la información de todos los usuarios (la cantidad de títulos que completó cada uno) para armar el gráfico que usted 
 crea mejor que resuelve el reporte solicitado.
NOTA: Puede Utilizar "title_completed_count" para obtener la información necesaria o crear una nueva función.
'''
if __name__ == '__main__':
    

    # Lanzar server
    app.run(host=server_config['host'],
            port=server_config['port'],
            debug=True)
