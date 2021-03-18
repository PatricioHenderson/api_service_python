#!/usr/bin/env python

__author__ = "Inove Coding School"
__email__ = "INFO@INOVE.COM.AR"
__version__ = "1.2"


import os
import sqlite3
import json
import requests

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = sqlalchemy.create_engine('sqlite:///profundizacion.db')
base = declarative_base()
session = sessionmaker(bind=engine)()


class Usuarios(base):
    __tablename__ = 'usuarios'
    idd = Column(Integer, primary_key=True)
    userId  = Column(Integer)#, primary_key = True , autoincrement= False)
    id = Column(Integer)
    title = Column(String)
    completed = Column(String)

    def __repr__(self):
        return f' userId : {self.userId} ,  id : {self.id} , title : {self.title} , completed : {self.completed} '

def clear():
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)



def fill():

    Session = sessionmaker(bind=engine)
    session = Session()

    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    data = json.loads(response.text)
    data = response.json()
    
    
    
    
    for i in data:
        
        
        
        usuario_add = Usuarios(userId=i['userId'] , id =i['id'] , title =i['title'] , completed=i['completed'])
        
        session.add(usuario_add)
        
  

    session.commit()


def title_completed_count(userId):
    Session = sessionmaker(bind=engine)
    session= Session()

    data = {}
    if userId == 0 :
        
        query = session.query(Usuarios).filter(Usuarios.userId)
        for i in query:
            print(i)
        
        
        
        
    else:
        query = session.query(Usuarios).filter((Usuarios.userId == userId) & (Usuarios.completed == True)).count()
    
    #print(query)
    return query

if __name__ == "__main__":
  # Borrar DB
  
  clear()

  # Completar la DB con el JSON request
  fill()

  userId=0
  title_completed_count(userId)

  # Lanzar server Flask
  #app.run()