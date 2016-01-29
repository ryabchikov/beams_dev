'''

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

def offeredLoad():
    basic_url = 'https://jovian.nms.jupiter.rsccops.net/NMSAPI'
    url = 'https://jovian.nms.jupiter.rsccops.net/NMSAPI/secure/oauth/authorize?response_type=token&client_id=jovian&redirect_uri=/NMSAPI/secure/tokenService/accessToken'
    headers = {'Authorization': 'Basic <base64Encoding(RSCC_API_Apps:pAK43Vrr)>'}
    auth = ('RSCC_API_Apps', 'pAK43Vrr')
    req = requests.get(url, headers=headers, verify=False, auth=auth)
    req_dict = (req.json())
    access_token = req_dict['access_token']
    token_type = req_dict['token_type']
    access_token = (token_type + ' ' + access_token)
    headers_token = {'Authorization': access_token}

    beams_request_url = (basic_url + '/beams/monitor/outroute/current')
    beams_response_url = requests.get(beams_request_url, headers=headers_token, verify=False)
    
    offeredLoadDict = {}

    for k in beams_response_url.json() :
        beam_details_request_url = (basic_url + "/beams/" + str(k['beamId']) + "/monitor/outroute/minute")
        beam_details_request_url = requests.get(beam_details_request_url, headers=headers_token, verify=False)
        beam_details = beam_details_request_url.json()
        offeredLoad =  beam_details[0]['offeredLoad']
        offeredLoadDict[str(k['beamId'])] = offeredLoad
    
    return offeredLoadDict
    
'''

__author__ = 'aryabchikov'

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

basic_url = 'https://jovian.nms.jupiter.rsccops.net/NMSAPI'
url = 'https://jovian.nms.jupiter.rsccops.net/NMSAPI/secure/oauth/authorize?response_type=token&client_id=jovian&redirect_uri=/NMSAPI/secure/tokenService/accessToken'
headers = {'Authorization': 'Basic <base64Encoding(Isatel:P@$$4Isatel!)>'}
auth = ('Isatel', 'P@$$4Isatel!')
req = requests.get(url, headers=headers, verify=False, auth=auth)
req_dict = (req.json())

access_token = req_dict['access_token']
token_type = req_dict['token_type']
access_token = (token_type + ' ' + access_token)

headers_token = {'Authorization': access_token}
print(headers_token)
vsats_list = (basic_url + '/vsats/')
req_vsats_list = requests.get(vsats_list, headers=headers_token, verify=False)

vsats_dict = (req_vsats_list.json())

VSAT_IDs = []

for k in vsats_dict:
    VSAT_IDs.append(k['id'])

VSATS_STATUS_LIST = []
for VSAT_ID in VSAT_IDs:
    vsat_info_url = (basic_url + '/vsats/' + VSAT_ID + '/status')
    req_vsat_info = requests.get(vsat_info_url, headers=headers_token, verify=False)
    VSATS_STATUS_LIST.append(req_vsat_info.json())

print(VSATS_STATUS_LIST)

f = open('vsats.txt', 'wt')

for terminal in VSATS_STATUS_LIST:
    texting = (terminal['deviceID'], terminal['latitude'], terminal['longitude'], terminal['terminalStatus'])
    s = str(texting)
    s = s.replace('\'','')
    s = (s + '\n')
    # print(s)
    f.write(s)

f.close()

raw_f = open('raw_vsats.txt', 'wt')

for terminal in VSATS_STATUS_LIST:
    texting = (terminal)
    s = str(texting)
    s = s.replace('\'','')
    s = (s + '\n')
    # print(s)
    raw_f.write(s)

raw_f.close()

print('That\'s all folks\n')



#print(vsats_dict)

