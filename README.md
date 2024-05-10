                              **Name**
                       Student: Paola Moreno
                   #  Module 10 / SQLAlchemy
                
![images.jpeg](images.jpeg)

## <a name="Data_Analysis_Report"></a> Data Analysis Report
This repository is designed to make a climate analysis on Honolulu, Hawaii, to help clients trip planning, and outline what they need to do in there vacation.


### <a name="Climate_Data"></a> Climate Data

The provided files (climate_starter.ipynb and hawaii.sqlite) will be utilized for this climate analysis and data exploration.

* Utilize the SQLAlchemy create_engine() function to establish a connection to the SQLite database.

* Employ the SQLAlchemy automap_base() function to reflect the database tables into classes. Subsequently, save references to these classes named station and 
measurement.

* Establish a link between Python and the database by creating a SQLAlchemy session. 

### <a name="Precipitation"></a> Precipitation
* Formulate a query to fetch the precipitation data for the past 12 months.

* Choose only the date and prcp columns from the retrieved data.

* Transfer the query results into a Pandas DataFrame and set the date column as the index.

* Arrange the DataFrame values in chronological order based on the date.

* Generate a plot of the precipitation data using the plot method provided by Pandas DataFrame.

* Utilize Pandas to display the summary statistics for the precipitation data.

### <a name="Stations"></a> Stations

* Create a query to determine the total count of stations within the dataset.

* Formulate a query to identify the most frequently used stations . 

* Develop a query to compute the lowest, highest, and average temperatures.

* Craft a query to retrieve the temperature observation (TOBS) data from the past 12 months.


## <a name="Flash_API"></a> Flash API Climate App 


Design a Flask API based on the queries that you have just developed.

* Use FLASK to create your routes.

### Home Page
Access the home page to view available routes.

### Routes:
Navigate to view a list of all available routes.

### /api/v1.0/precipitation:

* Perform a query to retrieve precipitation data.

* Convert the query results into a dictionary format using date as the key and prcp as the corresponding value.

* Return the JSON representation of the generated dictionary.

### /api/v1.0/stations:

* Access this route to obtain a JSON list of stations available in the dataset.

### /api/v1.0/tobs:

* Query the database for temperature observations (TOBS) from the previous year based on the last data point.
*Return a JSON list of temperature observations (tobs) for the previous year.

### /api/v1.0/<start> and /api/v1.0/<start>/<end>:

* Retrieve temperature data for a specified date range.
* Return a JSON list containing the minimum, average, and maximum temperatures.
* If only a start date is provided, calculate TMIN, TAVG, and TMAX for dates greater than or equal to the start date.
* If both start and end dates are provided, calculate TMIN, TAVG, and TMAX for dates within the specified range, inclusive.

