import requests
import json

# --- 1 ---
URL = 'https://chroniclingamerica.loc.gov/search/titles/results/?format=json'
PARAMS = {}

r = requests.get(url=URL, params=PARAMS)

data = r.json()

total_number = data['totalItems']

print('Total number of newspapers = %d ' % total_number)

# --- 2 ---
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

maximum = max(location_counter.values())
for k in location_counter.keys():
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

for k in location_counter.keys():
    if location_counter[k] == minimum:
        print(k, location_counter[k])

# --- 4 ---
URL = 'https://chroniclingamerica.loc.gov/search/titles/results/?state=Alabama&format=json'
PARAMS = {}  # Should I be using this in order to somehow print the state name?

r = requests.get(url=URL, params=PARAMS)

data = r.json()

total_number = data['totalItems']

print('Alabama\'s total number of newspapers = %d ' % total_number)

# --- 5 ---
URL = 'https://chroniclingamerica.loc.gov/newspapers.json'
PARAMS = {}

r = requests.get(url=URL, params=PARAMS)

data = r.json()

oregon = []
total_newspapers = 0

for s in data['newspapers']:
    if s['state'] == 'Oregon':
        total_newspapers += 1
        oregon.append(s['title'])
print('Oregon\'s total number of newspapers = %d ' % total_newspapers)

counter = 0

for o in data['newspapers']:
    if o['state'] == 'Oregon':
        oregon_info = requests.get(url=o['url'])
        oregon_data = oregon_info.json()
        print('Title: ' + oregon_data['name'], end=', ')
        print('Start year: ' + oregon_data['start_year'], end=', ')
        print('Issues available: ' + str(len(oregon_data['issues'])))
        counter += 1
        if counter >= 20:
            break
