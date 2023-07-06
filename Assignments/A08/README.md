# FastAPI - COVID-19 Data API
## Srinivas Makkena
This is a simple API that provides information about COVID-19 cases and deaths. It allows users to retrieve total counts, filter data by country and year, and find countries with maximum and minimum deaths in a specified date range.



| File          | Description                                     |
|---------------|-------------------------------------------------|
| [api.py](https://github.com/srinivasmakkena/4883-SoftwareTools-Makkena/blob/main/Assignments/A08/api.py)       | The main Python script for the FastAPI server.   |
| [data.csv](https://github.com/srinivasmakkena/4883-SoftwareTools-Makkena/blob/main/Assignments/A08/Resources/data.csv)      | The CSV file containing the COVID-19 data.       |


## Installation

To run the COVID-19 Data API, you need to have Python 3.x installed on your system. You also need to install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

## Usage

To start the API server, run the following command:

```
python api.py
```

The API server will be available at `http://localhost:5000/`.

### API Endpoints

- `/`: Redirects to the API documentation page.
- `/countries/`: Returns a list of unique countries.
- `/regions/`: Returns a list of unique WHO regions.
- `/deaths/`: Returns the total number of deaths based on optional filters (country, year, or region).
- `/cases/`: Returns the total number of new cases based on optional filters (country, year, or region).
- `/max_deaths/`: Returns the country with the maximum number of deaths within a specified date range.

For detailed information on each endpoint and their usage, please refer below examples

## API Documentation

The API documentation can be accessed at `http://localhost:5000/docs` when the server is running.

## Data Source

The data used by the API is sourced from a CSV file located at `Resources/data.csv`. The `DataReader` class is responsible for loading and processing the data from the CSV file.

## API Endpoints Usage

### `/countries/`

Returns a list of unique countries.

#### Example

- Request: GET `/countries/`

- Link: [http://localhost:5000/countries/](http://localhost:5000/countries/)

- Response:

```json
{
  "data": [
    "Afghanistan",
    "Albania",
    "Algeria",
    "...",
    "Zambia",
    "Zimbabwe"
  ],
  "success": true,
  "message": "All Unique countries",
  "size": 237
}
```

### `/regions/`

Returns a list of unique WHO regions.

#### Example

- Request: GET `/regions/`
  
- Link: [http://localhost:5000/regions/](http://localhost:5000/regions/)
  
- Response:

```json
{
  "data": [
    "EMRO",
    "EURO",
    "AFRO",
    "WPRO",
    "AMRO",
    "SEARO",
    "Other"
  ],
  "success": true,
  "message": "All Unique WHO regions",
  "size": 7
}
```

### `/deaths/`

Returns the total number of deaths based on optional filters (country, year, or region).

#### Parameters

- `country` (str): A country name (optional).
- `year` (int): A 4-digit year (optional).
- `region` (str): A region name (optional).

#### Example

- Request: GET `/deaths/?year=2021`

- Link: [http://localhost:5000/deaths/?year=2021](http://localhost:5000/deaths/?year=2021)

- Response:

```json
{
  "data": 3531524,
  "success": true,
  "message": "Total number of deaths in 2021 is 3531524"
}
```

### `/cases/`

Returns the total number of new cases based on optional filters (country, year, or region).

#### Parameters

- `country` (str): A country name (optional).
- `year` (int): A 4-digit year (optional).
- `region` (str): A region name (optional).

#### Example

- Request: GET `/cases/?year=2020&region=EMRO`

- Link: [http://localhost:5000/cases/?year=2020&region=EMRO](http://localhost:5000/cases/?year=2020&region=EMRO)
  
- Response:

```json
{
  "data": 4912291,
  "success": true,


"message": "Total number of new cases in 2020 for the WHO region of EMRO is 4912291"
}
```

### `/max_deaths/`

Returns the country with the maximum number of deaths within a specified date range.

#### Parameters

- `min_date` (str): The minimum date in the format 'YYYY-MM-DD' (optional).
- `max_date` (str): The maximum date in the format 'YYYY-MM-DD' (optional).

#### Example

- Request: GET `/max_deaths/?min_date=2020-12-28`

- Link:  [http://localhost:5000/max_deaths/?min_date=2020-12-28](http://localhost:5000/max_deaths/?min_date=2020-12-28)

- Response: 

```json
{
  "data": "United States of America",
  "success": true,
  "message": "The country with max deaths is United States of America with 1127152 deaths"
}
```
### `/min_deaths/`

Returns the country with the minimum number of deaths within a specified date range.

#### Parameters

- `min_date` (str): The minimum date in the format 'YYYY-MM-DD' (optional).
- `max_date` (str): The maximum date in the format 'YYYY-MM-DD' (optional).

#### Example

- Request: GET `/min_deaths/?min_date=2020-12-28`

- Link: [http://localhost:5000/min_deaths/?min_date=2020-12-28](http://localhost:5000/min_deaths/?min_date=2020-12-28)

- Response:

```json
{
  "data": "New Zealand",
  "success": true,
  "message": "The country with min deaths is New Zealand with 25 deaths"
}
```

### `/avg_deaths/`

Returns the average number of deaths per day within a specified date range.

#### Parameters

- `min_date` (str): The minimum date in the format 'YYYY-MM-DD' (optional).
- `max_date` (str): The maximum date in the format 'YYYY-MM-DD' (optional).

#### Example

- Request: GET `/avg_deaths/?min_date=2021-01-01&max_date=2021-12-31`

- Link: [http://localhost:5000/avg_deaths/?min_date=2021-01-01&max_date=2021-12-31](http://localhost:5000/avg_deaths/?min_date=2021-01-01&max_date=2021-12-31)

- Response:

```json
{
  "data": 1234.56,
  "success": true,
  "message": "The average number of deaths per day between 2021-01-01 and 2021-12-31 is 1234.56"
}
```
