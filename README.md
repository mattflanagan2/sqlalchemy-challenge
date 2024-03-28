# SQL Alchemy Challenge
## Background
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area.

## Part 1 Goals
In this section, the goal was to use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, using SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, completing the following steps:
* Use the SQLAlchemy create_engine() function to connect to a SQLite database.
* Use the SQLAlchemy automap_base() function to reflect tables into classes, and then save references to the classes named station and measurement.
* Link Python to the database by creating a SQLAlchemy session.
* Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

### My Process
Here I used python to connect to a SQLite database and reflected the tables into classes using automap_base(). Then I linked the python database to SQLAlchemy session.

<img width="1298" alt="Screenshot 2024-03-28 at 5 04 52 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/248dc47e-e180-4010-b0fb-a5338977de95">
<img width="1298" alt="Screenshot 2024-03-28 at 5 05 08 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/80f2365c-637d-4789-8c2c-b6a2cbcc26a3">
<img width="1309" alt="Screenshot 2024-03-28 at 5 05 29 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/049ce383-3be4-447a-ad9b-cfb5f564bd34">

Next I performed an Exploratory Precipitation Analysis.


<img width="1309" alt="Screenshot 2024-03-28 at 5 09 41 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/b4cac866-aa42-4990-b1d6-5b8343ad98c1">
<img width="1309" alt="Screenshot 2024-03-28 at 5 10 15 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/37a25eac-1dde-4130-bb4c-0184ac89c84e">
<img width="1177" alt="Screenshot 2024-03-28 at 5 10 35 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/f1e5bd28-adb2-4a36-8190-d0b603809d01">
<img width="1195" alt="Screenshot 2024-03-28 at 5 10 48 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/1da431be-9b4b-4632-979a-02960345058f">


After that I performed an Exploratory Station Analysis


<img width="1199" alt="Screenshot 2024-03-28 at 5 12 07 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/83e4c06c-8b47-4596-b68e-5bfc1dd9d4f8">
<img width="1199" alt="Screenshot 2024-03-28 at 5 12 18 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/687db29f-f230-415b-9310-80b4eda8ccf1">
<img width="1199" alt="Screenshot 2024-03-28 at 5 12 29 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/09bde7a5-2984-4ee0-8f80-92ca0561b8d0">
<img width="933" alt="Screenshot 2024-03-28 at 5 12 42 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/9286e2f4-4888-49e9-b1ce-b033b97649da">

After this I made sure to close my session with session.close()

## Part 2 Designing a Climate App Goals
Now that you’ve completed your initial analysis, I designed a Flask API based on the queries that I just developed. To do so, I used Flask to create routes as follows:

* /
  * Start at the homepage.
  * List all the available routes.
 * /api/v1.0/precipitation
   * Convert the query results from precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
   * Return the JSON representation of the dictionary.
* /api/v1.0/stations
  * Return a JSON list of stations from the dataset.
* /api/v1.0/tobs
  * Query the dates and temperature observations of the most-active station for the previous year of data.
  * Return a JSON list of temperature observations for the previous year.
* /api/v1.0/<start> and /api/v1.0/<start>/<end>
  * Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
  * For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
  * For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

Here is the code I used to achieve the previous goals stated.

<img width="1272" alt="Screenshot 2024-03-28 at 5 21 32 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/4ac19b3b-fbf3-43b1-84ce-a77a62447a56">
<img width="1272" alt="Screenshot 2024-03-28 at 5 21 46 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/834d4732-37fc-47e7-8ecd-c2672b19c849">
<img width="1272" alt="Screenshot 2024-03-28 at 5 21 59 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/aa84f12b-49cb-4dd8-a1f9-5157da8f113d">
<img width="1272" alt="Screenshot 2024-03-28 at 5 22 13 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/4780ab1d-a0fd-4d1f-92a4-ca2332e69dd0">
<img width="1272" alt="Screenshot 2024-03-28 at 5 22 37 PM" src="https://github.com/mattflanagan2/sqlalchemy-challenge/assets/146908072/69018435-aefb-4218-bd23-912b30243fa0">

