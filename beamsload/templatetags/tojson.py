'''
from django import template

import json

register = template.Library()

@register.filter(name='tojson')
def jsonify(_list):
    json_object = json.dumps(_list)
    return json_object
'''

#dictionary of numbers

numbers = {}

numbers['1'] = 'm -10,-10 c 2.6330294,-0.695 13.0958568,-7.1088 13.1651468,-18.0404 l -2.91019,44.864 -9.9211147,1.3911 17.6690147,-2.4644'
numbers['2'] = 'm 5.2549109,1013.4459 c 0.5046899,-7.0419 12.0024031,-14.99103 14.4641921,-0.6297 1.232711,7.191 -18.2594547,29.2415 -14.3932919,37.5827 -1.758e-4,-5e-4 4.1800867,-8.3566 8.2314159,-4.2704 5.999762,6.0514 6.247988,5.4631 8.107731,-1.6372'

    