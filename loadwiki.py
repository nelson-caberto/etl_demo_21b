from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pickle

with open('data.pickle','rb') as filehandle:
    data = pickle.load(filehandle)

engine = create_engine(f'postgresql://postgres:postgres@localhost:5432/etlDEMO')
session = Session(engine)

for x in data:
    sqlSTMT = f"INSERT INTO languages (name, first_appeared) VALUES ('{x['name']}',{x['date']})"
    try:
        engine.execute(sqlSTMT)
    except:
        continue
session.commit()