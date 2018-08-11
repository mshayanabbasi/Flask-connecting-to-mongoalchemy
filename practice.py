from flask import Flask
from flask_mongoalchemy import MongoAlchemy

app=Flask(__name__)
app.config['MONGOALCHEMY_DATABASE']='miti'
app.config['MONGOALCHEMY_CONNECTION_STRING']='mongodb://shayan:shayan123@ds111072.mlab.com:11072/miti'

db = MongoAlchemy(app)

class Example(db.Document):
    name=db.StringField()
    password=db.StringField()

Anthony=Example(name='Anthony',password='12356623')
Anthony.save()
Example.query.filter(Example.name=='Anthony').first()
a=Example.query.filter(Example.name=='Anthony').first()
a.name
a.password ='shayan123'
a.save()
b=Example.query.filter(Example.name=='Anthony').first()
b.remove()