from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import csv

engine = create_engine(f'postgresql://postgres:postgres@localhost:5432/etlDEMO')
session = Session(engine)

missing = set()
with open('etlDemo.csv') as filehandle:
    reader = csv.DictReader(filehandle)
    for row in reader:
        date = row['Date']
        del row['Date']
        for n, r in row.items():
            rate = float(r)
            sqlSTMT = f"SELECT name FROM languages WHERE name ILIKE '{n}'"
            if (name := session.execute(sqlSTMT).fetchall()):
                name = name[0][0]
                sqlSTMT = f"INSERT INTO populatiry (name, date, rating) VALUES ('{name}','{date}',{rate})"
                try:
                    session.execute(sqlSTMT)
                except Exception as e:
                    pass
            else:
                missing.add(n)
session.commit()
print(missing)