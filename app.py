# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt
from datetime import datetime, timedelta

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/start<br/>"
        "/api/v1.0/start/end"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    most_recent_date = session.query(func.max(measurement.date)).scalar()
    most_recent_date_dt = datetime.strptime(most_recent_date, '%Y-%m-%d')
    one_year_date = most_recent_date_dt - timedelta(days=365)
    results = session.query(measurement.date, measurement.prcp) \
                     .filter(measurement.date >= one_year_date) \
                     .all()
    session.close()
    # Create a dictionary from the row data and append to a list of all_prcp
    all_prcp = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        all_prcp.append(prcp_dict)
    return jsonify(all_prcp)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    """Return a list of all stations"""
    # Query all stations
    results = session.query(station.station).all()
    session.close()
    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))
    return jsonify(all_names)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    active_station = 'USC00519281'
    most_recent_date = session.query(func.max(measurement.date)).scalar()
    most_recent_date_dt = datetime.strptime(most_recent_date, '%Y-%m-%d')
    one_year_date = most_recent_date_dt - timedelta(days=365)
    results = session.query(measurement.date, measurement.tobs) \
                     .filter(measurement.date >= one_year_date) \
                     .filter(measurement.station == active_station) \
                     .all()
    session.close()
    # Create a dictionary from the row data and append to a list of all_tobs
    all_tobs = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        all_tobs.append(tobs_dict)
    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>")
def start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    start_results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)) \
        .filter(measurement.date >= start).all()
    session.close()
    # Convert list of tuples into normal list
    all_start = list(np.ravel(start_results))
    return jsonify(all_start)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    start_end_results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)) \
        .filter(measurement.date >= start).filter(measurement.date <= end).all()
    session.close()
    # Convert list of tuples into normal list
    all_start_end = list(np.ravel(start_end_results))
    return jsonify(all_start_end)

if __name__ == '__main__':
    app.run(debug=True)
