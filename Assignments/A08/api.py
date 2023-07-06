from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn, csv, json
import pandas as pd

description = """🚀
## 4883 Software Tools
### Where awesomeness happens
"""

class DataReader:
    def __init__(self, csv_file):
        self.data = None
        self.load_data(csv_file)

    def load_data(self, csv_file):
        self.data = pd.read_csv(csv_file)

    def get_attribute(self, attribute):
        return json.dumps(self.data[attribute].unique().tolist())

# Instantiate the DataReader class with the CSV file path
mydb = DataReader(r'D:\MSU\softwaretools\4883-SoftwareTools-Makkena\Assignments\A08\Resources\data.csv')

# print(mydb.data.head())
# print(mydb.data.shape[0])

# Initialize the FastAPI app with the provided description
app = FastAPI(description=description)

# Add a redirect route for the root endpoint
@app.get("/")
async def docs_redirect():
    """Redirects to the docs page."""
    return RedirectResponse(url="/docs")

# Define the countries route
@app.get("/countries/")
async def countries():
    """Returns a list of unique countries.
     ### Example:
      [http://localhost:5000/countries/](http://localhost:5000/countries/)
      ### Response
      {"data":["Afghanistan","Albania",
            "Algeria","........................ Futuna",
            "Yemen","Zambia","Zimbabwe"],
      "success":true,
      "message":"All Unique countries",
      "size":237}
    """

    response=  list(mydb.data['Country'].unique())
    return {"data": response, "success": True, "message": "All Unique countries", "size": len(response)}

# Define the regions route
@app.get("/regions/")
async def whos():
    """Returns a list of unique WHO regions.
       ### Example:
      [http://localhost:5000/regions/](http://localhost:5000/regions/)
       
       ### Response
       {"data":["EMRO","EURO","AFRO","WPRO","AMRO","SEARO","Other"],
      "success":true,
      "message":"All Unique WHO regions",
      "size":7}
      """
    response = list(mydb.data['WHO_region'].unique())
    return {"data": response, "success": True, "message": "All Unique WHO regions", "size": len(response)}


@app.get("/deaths/")
async def deaths(country:str = None,year:int = None,region:str = None):
    """
    This method will return a total death count or can be filtered by country and year.
    - **Params:**
      - country (str) : A country name
      - year (int) : A 4 digit year
      - region (str) : A region name
    - **Returns:**
      - (int) : The total sum of deaths based on filters (if any)
       ### Example:
        [http://localhost:5000/deaths/?year=2021](http://localhost:5000/deaths/?year=2021)
      
       ### Response
       {
        "data": 3531524,
        "success": true,
        "message": "Total number of deaths in 2021 is 3531524"
        }
    """
    response=int(mydb.data['New_deaths'].sum())
    message=f"Total number of entire deaths {response}"
    if year!=None:
        # response=int(mydb.data.loc[pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year), 'New_deaths'].sum())
        if country!=None:
            response=int(mydb.data.loc[(pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year)) & (mydb.data['Country'] == country), 'New_deaths'].sum())
            message=f"Total number of deaths in {year} for the country of {country} is {response}"
        elif region!=None:
            response=int(mydb.data.loc[(pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year)) & (mydb.data['WHO_region'] == region), 'New_deaths'].sum())
            message=f"Total number of deaths in {year} for the WHO region of {region} is {response}"
        else:
            response=int(mydb.data.loc[pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year), 'New_deaths'].sum())
            message=f"Total number of deaths in {year} is {response}"
    else:
        if country!=None:
            response=int(mydb.data[mydb.data['Country'] == country]['New_deaths'].sum())
            message=f"Total number of deaths in the country of {country} is {response}"
        if region!=None:
            response=int(mydb.data[mydb.data['WHO_region'] == region]['New_deaths'].sum())
            message=f"Total number of deaths in the WHO region of {region} is {response}"

    return {"data": response, "success": True, "message": message}

@app.get("/cases/")
async def cases(country:str = None,year:int = None,region:str = None):
    """
    This method will return a total new cases count or can be filtered by country and year.
    - **Params:**
      - country (str) : A country name
      - year (int) : A 4 digit year
      - region (str) : A region name
    - **Returns:**
      - (int) : The total sum of new cases based on filters (if any)

     ### Example:
        [http://localhost:5000/cases/?year=2020&region=EMRO](http://localhost:5000/cases/?year=2020&region=EMRO)
      
       ### Response
       {
        "data": 4912291,
        "success": true,
        "message": "Total number of new cases in 2020 for the WHO region of EMRO is 4912291"
        }
    """
    response=int(mydb.data['New_cases'].sum())
    message=f"Total number of entire new cases {response}"
    if year!=None:
        # response=int(mydb.data.loc[pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year), 'New_cases'].sum())
        if country!=None:
            response=int(mydb.data.loc[(pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year)) & (mydb.data['Country'] == country), 'New_cases'].sum())
            message=f"Total number of new cases in {year} for the country of {country} is {response}"
        elif region!=None:
            response=int(mydb.data.loc[(pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year)) & (mydb.data['WHO_region'] == region), 'New_cases'].sum())
            message=f"Total number of new cases in {year} for the WHO region of {region} is {response}"
        else:
            response=int(mydb.data.loc[pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year), 'New_cases'].sum())
            message=f"Total number of new cases in {year} is {response}"
    else:
        if country!=None:
            response=int(mydb.data[mydb.data['Country'] == country]['New_cases'].sum())
            message=f"Total number of new cases in the country of {country} is {response}"
        if region!=None:
            response=int(mydb.data[mydb.data['WHO_region'] == region]['New_cases'].sum())
            message=f"Total number of new cases in the WHO region of {region} is {response}"

    return {"data": response, "success": True, "message": message}

@app.get("/max_deaths/")
async def cases(min_date:str = None,max_date:str = None):
    """
    This method will return the country with the maximum number of deaths in a specified date range.
    If no date range is provided, it will consider the entire dataset.
    - **Params:**
      - min_date (str) : The minimum date in the format 'YYYY-MM-DD'
      - max_date (str) : The maximum date in the format 'YYYY-MM-DD'
    - **Returns:**
      - (str) : The country with the maximum number of deaths

     ### Example:
        [http://localhost:5000/max_deaths/?min_date=2020-12-28](http://localhost:5000/max_deaths/?min_date=2020-12-28)
      
       ### Response
       {
        "data": "United States of America",
        "success": true,
        "message": "The country with max deaths is United States of America with 1127152 deaths"
        }
    """
    response=''
    message="The country with max deaths is"
    mydb.data['Date_reported'] = pd.to_datetime(mydb.data['Date_reported'])

    if min_date!=None and max_date!=None:
        start_date = pd.to_datetime(min_date)
        end_date = pd.to_datetime(max_date)
        if start_date>end_date:
            start_date,end_date=end_date,start_date
        message=f"The country with max deaths between {start_date} and {end_date} is"
    else:
        start_date = mydb.data['Date_reported'].min()
        end_date = mydb.data['Date_reported'].max()
    
    filtered_df = mydb.data[(mydb.data['Date_reported'] >= start_date) & (mydb.data['Date_reported'] <= end_date)]
    grouped_df = filtered_df.groupby('Country')['New_deaths'].sum().reset_index()
    # else:
    #     grouped_df = mydb.data.groupby('Country')['New_deaths'].sum().reset_index()
    max_deaths_sum = grouped_df['New_deaths'].max()
    country_with_max_deaths_sum = grouped_df.loc[grouped_df['New_deaths'] == max_deaths_sum, 'Country'].values[0]
    response=country_with_max_deaths_sum
    message=f'{message} {response} with {max_deaths_sum} deaths'
    return {"data": response, "success": True, "message": message}



@app.get("/min_deaths/")
async def cases(min_date:str = None,max_date:str = None):
    """
    This method will return the country with the minimum number of deaths in a specified date range.
    If no date range is provided, it will consider the entire dataset.
    - **Params:**
      - min_date (str) : The minimum date in the format 'YYYY-MM-DD'
      - max_date (str) : The maximum date in the format 'YYYY-MM-DD'
    - **Returns:**
      - (str) : The country with the minimum number of deaths
    
       ### Example:
        [http://localhost:5000/min_deaths/?min_date=2020-12-28](http://localhost:5000/min_deaths/?min_date=2020-12-28)
      
       ### Response
        {
        "data": "Democratic People's Republic of Korea",
        "success": true,
        "message": "The country with min deaths is Democratic People's Republic of Korea with 0 deaths"
        }
    """
    response=''
    message="The country with min deaths is"
    mydb.data['Date_reported'] = pd.to_datetime(mydb.data['Date_reported'])

    if min_date!=None and max_date!=None:
        start_date = pd.to_datetime(min_date)
        end_date = pd.to_datetime(max_date)
        if start_date>end_date:
            start_date,end_date=end_date,start_date
        message=f"The country with min deaths between {start_date} and {end_date} is"
    else:
        start_date = mydb.data['Date_reported'].min()
        end_date = mydb.data['Date_reported'].max()
    
    filtered_df = mydb.data[(mydb.data['Date_reported'] >= start_date) & (mydb.data['Date_reported'] <= end_date)]
    grouped_df = filtered_df.groupby('Country')['New_deaths'].sum().reset_index()
    min_deaths_sum = grouped_df['New_deaths'].min()
    country_with_min_deaths_sum = grouped_df.loc[grouped_df['New_deaths'] == min_deaths_sum, 'Country'].values[0]
    response=country_with_min_deaths_sum
    message=f'{message} {response} with {min_deaths_sum} deaths'
    return {"data": response, "success": True, "message": message}


@app.get("/avg_deaths/")
async def avg_deaths():
    """
    This method will return the average number of deaths across all countries.
    - **Returns:**
     - (float) : The average number of deaths

      ### Example:
        [http://localhost:5000/avg_deaths/](http://localhost:5000/avg_deaths/)
      
       ### Response
       {
        "data": 29306.810126582277,
        "success": true,
        "message": "Average number of deaths across all countries: 29306.810126582277"
        }
    """
    response=int(mydb.data['New_deaths'].sum())/len(mydb.data['Country'].unique())
    message=f"Average number of deaths across all countries: {response}"
    return {"data": response, "success": True, "message": message}

if __name__ == "__main__":
    # Run the FastAPI app using uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=5000, log_level="debug", reload=True)
