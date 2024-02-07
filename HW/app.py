# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, distinct
import datetime as dt

from flask import Flask, jsonify



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """Listing all api routes"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"Please replace the word start with a date in (YYYY-MM-DD) format to query<br/>"
        f"/api/v1.0/start/end<br/>"
        f"Please replace the words start and end with a date in (YYYY-MM-DD) format to query<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    most_recent_date = dt.datetime(2017, 8, 23)
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    #retrieving query results
    rain_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= func.date(one_year_ago)).all()

    #putting into dictionary
    precipitation_data = {}
    for rain in rain_data:
        date = rain[0]
        prcp = rain[1]
        precipitation_data[date] = prcp


    return jsonify(precipitation_data)



@app.route("/api/v1.0/stations")
def stations():
    total_stations = session.query(Measurement.station).distinct().all()
    station_list = [station[0] for station in total_stations]

    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def tobs():
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    most_recent_date = dt.datetime(2017, 8, 23)
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    temp_data = session.query(Measurement.tobs).filter(Measurement.station == "USC00519281")\
                                            .filter(Measurement.date >= one_year_ago)\
                                            .filter(Measurement.date <= most_recent_date)\
                                            .all()
    
    temps = [temp[0] for temp in temp_data]

    return jsonify(temps)


@app.route("/api/v1.0/<start>")
def temp_start(start):
    start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    one_year_ago = dt.timedelta(days=365)
    start = start_date - one_year_ago
    end = dt.date(2017, 8, 23)
    temp_start_stats = session.query(func.min(Measurement.tobs),
                                func.max(Measurement.tobs),
                                func.avg(Measurement.tobs))\
                                .filter(Measurement.date >= start).filter(Measurement.date <= end)\
                                .all()

    
    labels = ['TMIN', 'TMAX', 'TAVG']
    temp_start_dict = {label: stat for label, stat in zip(labels, temp_start_stats[0])}

    return jsonify(temp_start_dict)

@app.route("/api/v1.0/<start>/<end>")
def temp_end(start,end):
    start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    end_date = dt.datetime.strptime(end, '%Y-%m-%d')
    one_year_ago = dt.timedelta(days=365)
    end = end_date-one_year_ago
    start = start_date-one_year_ago
    temp_end_stats = session.query(func.min(Measurement.tobs),
                                func.max(Measurement.tobs),
                                func.avg(Measurement.tobs))\
                                .filter(Measurement.date >= start).filter(Measurement.date <= end)\
                                .all()

    
    labels = ['TMIN', 'TMAX', 'TAVG']
    temp_end_dict = {label: stat for label, stat in zip(labels, temp_end_stats[0])}

    return jsonify(temp_end_dict)






if __name__ == '__main__':
    app.run(debug=True)

