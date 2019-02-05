# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action
import csv
import requests


logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []




############ testing #############

class ActionGetData(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_getdata"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        latest_msg = tracker.latest_message['intent']
        latest_intent=json.dumps(latest_msg['name'])

        f = open('getdata.csv')
        csv_f = csv.reader(f)

        for row in csv_f:
            intent='"'+row[0]+'"'
            if latest_intent==intent:
                latest_intent_1=row[0]
                impact=row[1]
                product_name=row[2]
                incident_service_type=row[3]

        ## till here we got the details of the incident from csv
        ## now we need to push these details to servicenow and create an incident
        ## then we neeed to retrieve that unique incident ID
        
        url = ''
        user = 'admin'
        pwd = 'admin'
        headers = {"Content-Type":"application/json","Accept":"application/json"}

        #  response = requests.post(url, auth=(user, pwd), headers=headers )

        #  data_to_be_posted = {"u_intent": latest_intent ,"u_impact": impact ,"u_product_type":product_name , "u_incident_service_type": incident_service_type }
        
        data_to_be_posted = {
        'u_intent': latest_intent_1 ,
        'u_impact': impact ,
        'u_product_type':product_name ,
        'u_incident_service_type': incident_service_type, 
        }

        #  response = requests.post(url, headers=headers, params=params,data=json.dumps(data_to_be_posted))

        
        response = requests.post(url, auth=(user, pwd), headers=headers ,data=json.dumps(data_to_be_posted))

        
        #  response = requests.post(url, auth=(user, pwd), headers=headers ,data='{"u_intent": "latest_intent"   ,"u_impact": "impact"    ,"u_product_type":"product_name"            , "u_incident_service_type": "incident_service_type" }')
        
        #  response = requests.post(url, auth=(user, pwd), headers=headers ,data='{"u_intent":"unable_leave_post","u_impact":"minor/local","u_product_type":"human resource management"}')

        #Check for HTTP codes other than 200

        #    if response.status_code != 200: 
        #        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        #        exit()

        #Decode the JSON response into a dictionary and use the data
        data = response.json()
        latest_data=json.dumps(data)
        #  print(data)
        

        u_number_string=data['result']['u_number']
        # u_number_string=json.dumps(data('u_number'))



        #############################




        
        #############################
        
        # reply= "As you are unable to apply leave, the impact is for you Issue is:"+impact+", and the product is under:"+product_name+", and incident service type is "+ 
        reply1= "A Ticket has been raised, you can note down your ticket's reference number:"+u_number_string
        dispatcher.utter_message(reply1)  # send the message back to the user
        return []
        
