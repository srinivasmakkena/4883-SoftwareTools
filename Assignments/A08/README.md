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

The API server will be available at `http://localhost:8000/`.

## Endpoints

The API provides the following endpoints:

### GET /deaths/

This endpoint returns the total number of deaths. It can be further filtered by country, year, or WHO region.

**Parameters:**

- `country` (optional): A country name to filter the data by.
- `year` (optional): A 4-digit year to filter the data by.
- `region` (optional): A WHO region name to filter the data by.

**Response:**

- `data`: The total number of deaths based on the filters (if any).
- `success`: A boolean indicating the success of the request.
- `message`: A message providing additional information about the request.

### GET /cases/

This endpoint returns the total number of new cases. It can be further filtered by country, year, or WHO region.

**Parameters:**

- `country` (optional): A country name to filter the data by.
- `year` (optional): A 4-digit year to filter the data by.
- `region` (optional): A WHO region name to filter the data by.

**Response:**

- `data`: The total number of new cases based on the filters (if any).
- `success`: A boolean indicating the success of the request.
- `message`: A message providing additional information about the request.

### GET /max_deaths/

This endpoint returns the country with the maximum number of deaths in a specified date range. If no date range is provided, it considers the entire dataset.

**Parameters:**

- `min_date` (optional): The minimum date in the format 'YYYY-MM-DD'.
- `max_date` (optional): The maximum date in the format 'YYYY-MM-DD'.

**Response:**

- `data`: The country with the maximum number of deaths.
- `success`: A boolean indicating the success of the request.
- `message`: A message providing additional information about the request.

### GET /min_deaths/

This endpoint returns the country with the minimum number of deaths in a specified date range. If no date range is provided, it considers the entire dataset.

**Parameters:**

- `min_date` (optional): The minimum date in the format 'YYYY-MM-DD'.
- `max_date` (optional): The maximum date in the format 'YYYY-MM-DD'.

**Response:**

- `data`: The country with the minimum number of deaths.
- `success`: A boolean indicating the success of the request.
- `message`: A message providing additional information about the request.

### GET /avg_deaths/

This endpoint returns the average number of deaths across all countries.

**Response:**

- `data`: The average number of deaths.
- `success`: A boolean indicating the success of the request.
- `message`: A message providing additional information about the request.

## Implementation Process

The implementation process of the COVID-19 Data API involved creating several endpoints to handle different data retrieval scenarios. The endpoints were implemented using the FastAPI framework in Python. The data is stored in a pandas DataFrame and
