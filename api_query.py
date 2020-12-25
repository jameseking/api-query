import requests
import json

# --- 1 ---
URL = 'https://chroniclingamerica.loc.gov/search/titles/results/?format=json'  # URL to query
PARAMS = {}

r = requests.get(url=URL, params=PARAMS)  # GET request to specified URL

data = r.json()  # Convert data to json format

total_number = data['totalItems']  # json list - pull out totalItems value

print('Total number of newspapers = %d ' % total_number)

# --- 2 ---
URL = 'https://chroniclingamerica.loc.gov/newspapers.json'
PARAMS = {}

r = requests.get(url=URL, params=PARAMS)

data = r.json()

location_counter = {}  # Dictionary to append states and number of publications to

for n in data['newspapers']:  # This iterates through newspapers data and appends state and one 
    state = n['state']  # occurance first time state appears, increased occurance by one each subsequent
    if state in location_counter:  # time the state appears
        location_counter[state] += 1
    else:
        location_counter[state] = 1

maximum = max(location_counter.values())

for k in location_counter.keys():  # Find key value pair with max value, print key and value
    if location_counter[k] == maximum:
        print(k, location_counter[k])

# --- 3 ---
URL = 'https://chroniclingamerica.loc.gov/newspapers.json'
PARAMS = {}

r = requests.get(url=URL, params=PARAMS)

data = r.json()

location_counter = {}

for n in data['newspapers']:
    state = n['state']
    if state in location_counter:
        location_counter[state] += 1
    else:
        location_counter[state] = 1

minimum = min(location_counter.values())

for k in location_counter.keys(): # Same as above with minimum value instead of maximum
    if location_counter[k] == minimum:
        print(k, location_counter[k])

# --- 4 ---
URL = 'https://chroniclingamerica.loc.gov/search/titles/results/?state=Alabama&format=json'
PARAMS = {} 

r = requests.get(url=URL, params=PARAMS)

data = r.json()

total_number = data['totalItems']  # Search for Alabama's total publications using modified URL

print('Alabama\'s total number of newspapers = %d ' % total_number)

# --- 5 ---
URL = 'https://chroniclingamerica.loc.gov/newspapers.json'
PARAMS = {}

r = requests.get(url=URL, params=PARAMS)

data = r.json()

oregon = []
total_newspapers = 0

for s in data['newspapers']:  # Iterate through data, print state name and total number of newspapers from state
    if s['state'] == 'Oregon':
        total_newspapers += 1
        oregon.append(s['title'])
print('Oregon\'s total number of newspapers = %d ' % total_newspapers)

counter = 0

for o in data['newspapers']:  # Loop through Oregon newspapers
    if o['state'] == 'Oregon':
        oregon_info = requests.get(url=o['url'])  # Query for additional information
        oregon_data = oregon_info.json()
        print('Title: ' + oregon_data['name'], end=', ')  # Print title
        print('Start year: ' + oregon_data['start_year'], end=', ')  # Print starting year
        print('Issues available: ' + str(len(oregon_data['issues'])))  # Print total number of issues
        counter += 1
        if counter >= 20:  # Perform additinoal query for first 20 Oregon newspapers
            break
