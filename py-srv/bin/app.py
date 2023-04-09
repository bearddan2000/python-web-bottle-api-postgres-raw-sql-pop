import bottle
from bottle import route, run, request
from bottle.ext.sqlalchemy import SQLAlchemyPlugin

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings
from model import Base
from strategy.cls_raw import Raw
# from strategy.cls_chained import Chained

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = engine = create_engine(
    '{engine}://{username}@{host}/{db_name}'.format(
        **settings.POSTGRESQL
    ),
    echo=settings.SQLALCHEMY['debug']
)
session_local = sessionmaker(
    bind=engine,
    autoflush=settings.SQLALCHEMY['autoflush'],
    autocommit=settings.SQLALCHEMY['autocommit']
)
def setup_routes():
     bottle.route('/pop/<pop_id>', ['GET', 'DELETE'], crud)
     bottle.route('/pop/<pop_name>/<pop_color>', ['PUT'], insert_entry)
     bottle.route('/pop/<pop_id>/<pop_name>/<pop_color>', ['POST'], update_entry)

def get_strategy(db):
     return Raw(db)

@route('/')
def hello():
	return {"hello": "world"}

@route('/pop')
def get_all(db):
    strategy = get_strategy(db)
    return strategy.all()

def crud(db, pop_id):
    strategy = get_strategy(db)
    if request.method == 'GET':
        return strategy.filter_by(pop_id)
    
    return strategy.delete_by(pop_id)

def insert_entry(db, pop_name, pop_color):
    strategy = get_strategy(db)
    return strategy.insert_entry(pop_name, pop_color)

def update_entry(db, pop_id, pop_name, pop_color):
    strategy = get_strategy(db)
    return strategy.update_entry(pop_id, pop_name, pop_color)

bottle.install(SQLAlchemyPlugin(engine, Base.metadata, create=False, create_session = session_local))

setup_routes()

run(host='0.0.0.0', port=8000,debug=True)
