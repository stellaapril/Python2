import csv, json

# create a json file
criteria = {}
criteria['fiscal_year'] = '2017', '2018'
criteria['start_date'] = '2017-2-8'
criteria['area'] = ''
criteria['asset_type'] = ''
criteria['planning_status'] = ''

# criteria = {"fiscal_year": [None], "start_date": [""], "area": [""], "asset_type": [""], "planning_status": [""]}

with open('jsonfile.json', 'w')as f:
    json.dump(criteria, f)

# load json criteria
with open('jsonfile.json') as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    # print(json_data['fiscal_year'])

jyear = json_data['fiscal_year']
jdate = json_data['start_date']
jarea = json_data['area']
jasset = json_data['asset_type']
jstatus = json_data['planning_status']

# open csv file
with open('capitalprojects.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    csv_list = []
    for row in csv_reader:
        csv_list.append(row)

'''
for x in csv_list:
  for y in jyear:
    if y == '' or y==x['fiscal_year']:
      datsalist.append(x)
'''
yearData = []
for x in csv_list:
    for y in jyear:
        if y == '' or y == x['fiscal_year']:
            yearData.append(x)

dateData = []
for x in yearData:
    for y in jdate:
        if y == '' or y == x['start_date']:
            dateData.append(x)

print(dateData)

'''
def getData (jdata,criteria,data_list):
  finallist=[]
  for x in data_list:
    for y in jdata:
      if y=='' or y==x[criteria]:
        finallist.append(x)
  return finallist


yearData=getData(jyear,'fiscal_year',csv_list)


dateData=getData(jdate,'start_date',yearData)

areaData=getData(jarea,'area',dateData)
assetData=getData(jasser,'asset_type',areaData)
statusData=getData(jstatus,'status'，asseData)
'''

# print(datalist)


'''


    if row['fiscal_year']==jyear:
      elif row['start_date']==jdate or row['start_date']=="":
        elif row['area']==jareaor or row['area']=="":
          elif row['asset_type']==jasset or row['asset_type']=="":
            elif row['status']==jstatus or row['status']=="":
              print(row)

    #print(row['fiscal_year'])





'''









