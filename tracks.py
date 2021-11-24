from bs4 import BeautifulSoup
import requests 
import sqlite3
import json
import urllib.request,urllib.parse,urllib.error

service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
key = 'google_api_key'
conn = sqlite3.connect('race_tracks.sqlite')
cur = conn.cursor()
cur.execute('create table if not exists tracks(track_name text, lat text, lng text, country text)')


html_text = requests.get('https://www.racingcircuits.info/a-to-z-circuit-list.html').text
soup = BeautifulSoup(html_text,'lxml')
tracks = soup.find_all('div',class_= 'az-item')
for track in tracks:
        race_track= track.find('a').text
        parms = dict()
        parms['address'] = race_track
        parms['key'] = key
        url = service_url+urllib.parse.urlencode(parms)
        uh = urllib.request.urlopen(url)
        data =uh.read().decode()
        js = json.loads(data)
        if not ('status' in js and js['status']== 'OK'):
            continue
        lat = js['results'][0]['geometry']['location']['lat']
        lng = js['results'][0]['geometry']['location']['lng']
        long_address = js['results'][0]['formatted_address']
        country = long_address.split(',')[-1]
        print(f'loading track name: {race_track},country: {country} and latitude and longitude data into database')
        cur.execute('insert into tracks(track_name,lat,lng,country) values (?,?,?,?)',(race_track,lat,lng,country))
        conn.commit()       
print('Done loading data into database')
        
