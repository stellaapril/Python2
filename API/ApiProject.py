import json
import time
import urllib.request

API="9BSxAIWRZxI89ABd83fzGGMZffvDp5Xk"
countryCode='US'
cityinput=input('input a city name : ')

key=''
def getLocation(country,city):
  search_address='http://dataservice.accuweather.com/locations/v1/cities/'+country+'/search?apikey=9BSxAIWRZxI89ABd83fzGGMZffvDp5Xk&q='+city+'&details=true'

  with urllib.request.urlopen(search_address) as search_address:
    data=json.loads(search_address.read().decode())

  #print(data)
  location_key = data[0]['Key']
  return location_key





def getForcast(location_key):
  url = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/'+location_key+'?apikey=9BSxAIWRZxI89ABd83fzGGMZffvDp5Xk&details=true'

  with urllib.request.urlopen(url) as daliy_forecasts:
    data2 = json.loads(daliy_forecasts.read().decode())
  #print(data2['DailyForecasts'][1])


  for i in data2['DailyForecasts']:
    print('Weather Date: '+ i['Date'])
    print('Min Tempreture: '+str(i['Temperature']['Minimum']['Value']))
    print('Max Tempreture: '+str(i['Temperature']['Maximum']['Value']))
    print('Day Forcast : '+str(i['Day']['ShortPhrase']))
    print('----------------------------------')



key = getLocation(countryCode,cityinput)
getForcast(key)