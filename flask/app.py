from flask import Flask,request
from sqlalchemy import create_engine, text
from createdb import createDB
import os


user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
db   = os.environ['POSTGRES_DB']
host   = os.environ['POSTGRES_HOST']
app = Flask(__name__)
app.config["DEBUG"] = True
createDB(user,password,db,host)
@app.route('/', methods=['GET'])
def get():
    return "a30ee592b51f2f382a1e9d2dd0baed8920e8d51a"

@app.route('/', methods=['POST'])
def post():
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}/{db}", echo=True, future=True)
    with engine.connect() as conn:
        for row in request.get_json()['data']['observations']:
            for key,value in row['latestRecord'].items():
                row[key] = value
            stmt = """INSERT INTO records (time, clientmac, ipv4, ssid, os, manufacturer, nearestApMac,nearestApRssi)
                    VALUES (:time, :clientmac, :ipv4, :ssid, :os, :manufacturer, :nearestApMac, :nearestApRssi)"""
            conn.execute(text(stmt),[{"time":row["time"], "clientmac":row["clientMac"],"ipv4":row["ipv4"],
                                    "ssid":row["ssid"],"os":row['os'],"manufacturer":row["manufacturer"],
                                    "nearestApMac":row['nearestApMac'],"nearestApRssi":row['nearestApRssi']}]) 
        conn.commit()
    return "a30ee592b51f2f382a1e9d2dd0baed8920e8d51a"
    
    

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
    #app.run(debug=True,ssl_context=('cert.pem', 'key.pem'))

