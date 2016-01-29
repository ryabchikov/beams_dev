#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests



def offeredLoad():
    basic_url = 'https://172.27.5.130/NMSAPI'
    url = 'https://172.27.5.130/NMSAPI/secure/oauth/authorize?response_type=token&client_id=jovian&redirect_uri=/NMSAPI/secure/tokenService/accessToken'
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
        offeredLoad =  round(beam_details[0]['offeredLoad'], 1)
        beam_details_request_url_inroute = (basic_url + "/beams/" + str(k['beamId']) + "/monitor/inroute/minute")
        beam_details_request_url_inroute = requests.get(beam_details_request_url_inroute, headers=headers_token, verify=False)
        beam_details_inroute = beam_details_request_url_inroute.json()
        offeredLoad_inroute =  round(beam_details_inroute[0]['offeredLoad'], 1)
        offeredLoadDict[str(k['beamId'])] = str(offeredLoad) + " / " + str(offeredLoad_inroute)
    
    return offeredLoadDict

offeredLoad()