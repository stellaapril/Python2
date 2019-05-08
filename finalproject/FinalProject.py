import requests
import csv
import json
import random

#open csv
file = open('us-state.csv',newline='')
csv_reader = csv.DictReader(file)
states_list=[]

#create states list
for row in csv_reader:
  states_list.append(row['origin'])

file.close()


#sample input
sample_number=input('Choose your number of samples:(5-30): ')

#select sample
def sample(number):
  states=random.sample(states_list, int(number))

  #print('select: ',states)
  return states

#select states sample capital city
file = open('us-state.csv',newline='')
csv_reader = csv.DictReader(file)
capital_list=[]
for y in csv_reader:
  for x in sample(sample_number):
    if y['origin']==x:
      capital_list.append(y['description'])

file.close()

#city_name = input('Please input city name: ')



#API
def citylibrary(cityname):
  overpass_url = "http://overpass-api.de/api/interpreter"
  overpass_query = """
  [out:json];
  ( area[name="%s"]; )->.a;
  (node(area.a)["amenity"="library"];
  way(area.a)["amenity"="library"];
  rel(area.a)["amenity"="library"];);
  out center;
  """
  new_query=overpass_query%(cityname)
  response = requests.get(overpass_url, params={'data': new_query})
  library_map = response.json()

  return library_map


def citymuseum(cityname2):
  overpass_url = "http://overpass-api.de/api/interpreter"
  overpass_query = """
  [out:json];
  ( area[name="%s"]; )->.a;
  (node(area.a)["tourism"="museum"];
  way(area.a)["tourism"="museum"];
  rel(area.a)["tourism"="museum"];);
  out center;
  """
  new_query2=overpass_query%(cityname2)
  response = requests.get(overpass_url, params={'data': new_query2})
  museum_map = response.json()

  return museum_map

def citypub(cityname):
  overpass_url = "http://overpass-api.de/api/interpreter"
  overpass_query = """
  [out:json];
  ( area[name="%s"]; )->.a;
  (node(area.a)["amenity"="pub"];
  way(area.a)["amenity"="pub"];
  rel(area.a)["amenity"="pub"];);
  out center;
  """
  pub_query=overpass_query%(cityname)
  response = requests.get(overpass_url, params={'data': pub_query})
  pub_map = response.json()

  return pub_map

def citycafe(cityname):
  overpass_url = "http://overpass-api.de/api/interpreter"
  overpass_query = """
  [out:json];
  ( area[name="%s"]; )->.a;
  (node(area.a)["amenity"="cafe"];
  way(area.a)["amenity"="cafe"];
  rel(area.a)["amenity"="cafe"];);
  out center;
  """
  cafe_query=overpass_query%(cityname)
  response = requests.get(overpass_url, params={'data': cafe_query})
  cafe_map = response.json()

  return cafe_map


#get data
def numberOflibrary(cityname):
    dic_lib=citylibrary(cityname)
    n=0
    for i in dic_lib['elements']:
        n=n+1
    return n

def numberOfmuseum(cityname2):
  dic_museum=citymuseum(cityname2)
  m=0
  for x in dic_museum['elements']:
    m=m+1
  return m

def numberOfpub(cityname3):
    dic_pub=citypub(cityname3)
    p=0
    for i in dic_pub['elements']:
        p=p+1
    return p


def numberOfcafe(cityname4):
    dic_cafe=citycafe(cityname4)
    f=0
    for l in dic_cafe['elements']:
        f=f+1
    return f



for z in capital_list:
  print('City Name:',z)
  print('Number of Library: ',numberOflibrary(z))
  print('Number of Museum: ',numberOfmuseum(z))
  print('Number of Pub: ',numberOfpub(z))
  print('Number of Cafe: ',numberOfcafe(z))
  print('--------------------------------------')

