
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.template.loader import get_template



import datetime
import MySQLdb

from .models import Beam

from beamsload.templatetags import tojson
from beamsload.offeredLoad import offeredLoad
from beamsload.positions import positions

# Create your views here.


def index(request):
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
    
    beamsDict = offeredLoad()
    positionsDict = positions()
    
    
    t = get_template('index.html',)
    html = t.render(Context({'test': datetime.datetime.now(),'points': points, 'numbers': tojson.numbers, 'beamsDict': beamsDict, 'positionsDict': positionsDict,}))
 
    return HttpResponse(html)

