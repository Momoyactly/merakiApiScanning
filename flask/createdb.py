from sqlalchemy import create_engine, text
import os
import json

def createDB(user,password,db):
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@postgres-app/{db}", echo=True, future=True)
    with engine.connect() as conn:
        stmt = """CREATE TABLE IF NOT EXISTS records (id serial PRIMARY KEY, 
                                        time varchar, clientMac varchar,
                                        ipv4 varchar,ssid varchar,
                                        os varchar,manufacturer varchar,
                                        nearestApMac varchar,nearestApRssi varchar)"""
        conn.execute(text(stmt))
        conn.commit()
if __name__ == "__main__":
    user = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    db   = os.environ['POSTGRES_DB']
    createDB(user,password,db)
