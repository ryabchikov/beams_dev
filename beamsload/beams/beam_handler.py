#!/usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb
import re
import json
import decimal

db = MySQLdb.connect('localhost', 'root', 'Daf2Wy9o', 'mapsdb');
cursor = db.cursor()
sql = "SELECT id FROM beamsload_beam"
cursor.execute(sql)
_list = cursor.fetchall()
points = {}


for i in _list:
    get_points_request = ("SELECT latitude, longitude FROM beamsload_point WHERE beam_id = '%s'" % i[0])
    cursor.execute(get_points_request)
    coordinates = (cursor.fetchall())   
    buffer = []
    
    for j in coordinates:
        lat = float(j[0])
        lng = float(j[1])
        buffer.append({'lat': lat, 'lng': lng,})
        
    points[i[0]] = buffer              
              
db.close()

print(points)

'''
def jsonify(_list):
    json_object = json.dumps(_list)
    return json_object


filename = "G10"
beam_id = 10
db = MySQLdb.connect('localhost', 'root', 'Daf2Wy9o', 'mapsdb');
cursor = db.cursor()
sql = "SELECT latitude, longitude FROM beamsload_point WHERE beam_id=1;"

cursor.execute(sql)
coordinates = (cursor.fetchall())

points = []
for k in coordinates:
    lat = float(k[0])
    lng = float(k[1])
    points.append({"lat": lat, "lng": lng,})

x = jsonify(points)
print(x)


#print(json.dumps(coordinates))
'''
'''
lat and lng handler
f = open(filename, 'r')
for line in f:
    
    x = re.findall(r'(\d+.\d+)', line)
    latitude = (x[0])
    #print(type(latitude))
    longitude = (x[1])
    
    sql = "INSERT INTO beamsload_point(beam_id, latitude, longitude) \
           VALUES ('%d', '%s', '%s')" % \
           (beam_id, latitude, longitude)
           
    try :
        cursor.execute(sql)
        db.commit()
        print("SUCCESS")
    except:
        db.rollback()
        print("FAILURE")

    
f.close()
'''


