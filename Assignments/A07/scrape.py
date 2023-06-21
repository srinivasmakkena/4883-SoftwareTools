import PySimpleGUI as sg
import json
import os
from datetime import datetime
from get_content import get_dynamic_content

currentlocation = os.path.dirname(os.path.abspath(__file__))
sg.theme('DarkAmber')
sg.set_options(font=('Helvetica', 12))

with open(currentlocation + '\\Resources\\airport-codes.json', 'r') as file:
    json_data = file.read()

# Convert JSON to dictionary
data_dict = json.loads(json_data)
airport_codes = [data['icao'] for data in data_dict]
current_date = datetime.now()
default_year = str(current_date.year)
default_month = current_date.strftime('%B')
default_day = str(current_date.day)
month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
              'September': 9, 'October': 10, 'November': 11, 'December': 12}

# Define the layout of the GUI
layout = [
    [sg.Column([
        [sg.Frame('Airport Weather', layout=[
            [sg.Text('Filter:', size=(10, 1)),
             sg.Combo(['daily'], key='-FILTER-', default_value='daily', size=(20, 1),
                      enable_events=True)],
            [sg.Text('Airport Code:', size=(10, 1)),
             sg.Combo(airport_codes, key='-AIRPORT-', size=(20, 1), default_value=airport_codes[0],
                      enable_events=True)],
            [sg.Text('Year:', size=(10, 1)),
             sg.Combo(['2021', '2022', '2023'], key='-YEAR-', default_value=default_year, size=(20, 1),
                      enable_events=True)],
            [sg.Text('Month:', size=(10, 1)),
             sg.Combo(month_dict.keys(), key='-MONTH-', default_value=default_month, size=(20, 1),
                      enable_events=True)],
            [sg.Text('Day:', size=(10, 1)),
             sg.Combo([str(day) for day in range(1, 32)], key='-DAY-', default_value=default_day, size=(20, 1),
                      enable_events=True)],
            [sg.Button('Submit', key='-SUBMIT-', size=(10, 1))]
        ])]
    ], element_justification='center', vertical_alignment='center', justification='center', pad=(50, 50))],

    # Add a close button
    [sg.Button('Close', key='-CLOSE-', size=(10, 1))]
]

window = sg.Window('Airport Weather', layout, element_justification='center', resizable=True)

def create_table_view(content, headings, airport_code, year, month, day):
    content = [row for row in content if row]
    headings =[row for row in headings if row][0]
    print(headings,content)
    layout = [
        [sg.Table(values=content, headings=headings, key='-TABLE-', justification='center')],
        [sg.Button('Close', key='-CLOSE-', size=(10, 1))]
    ]
    airport= next((d for d in data_dict if d["icao"] == airport_code), None)
    window = sg.Window('Airport Weather on '+str(month)+'-'+str(day)+'-'+str(year)+'  at '+ airport['name'], layout, element_justification='center', resizable=True)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == '-CLOSE-':
            break
    
    window.close()
    
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == '-CLOSE-':
        break

    elif event == '-SUBMIT-':
        selected_filter = values['-FILTER-']
        airport_code = values['-AIRPORT-']
        year = values['-YEAR-']
        month = month_dict.get(values['-MONTH-'], "")
        day = values['-DAY-']
        print(f'Filter: {selected_filter}')
        print(f'Airport Code: {airport_code}')
        print(f'Year: {year}')
        print(f'Month: {month}')
        print(f'Day: {day}')
        url = f'https://www.wunderground.com/history/{selected_filter}/{airport_code}/date/{year}-{month}-{day}'
        
        window.close()    
        content, headings = get_dynamic_content(url)
        
        create_table_view(content, headings,airport_code,year,month,day)
        
