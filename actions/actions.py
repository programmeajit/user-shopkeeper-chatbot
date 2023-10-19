# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet,UserUtteranceReverted,ActionReverted
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#from ..response.mobile_responses import fetch_mobile_response

import sys
sys.path.insert(1,'/home/ubuntu/response')
import mobile_responses

class BuyMobilePhone(Action):

    def name(self) -> Text:
        return "action_buy_mobile_phone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        response = mobile_responses.questionOnBudget()
        dispatcher.utter_message(json_message=response)

        return [SlotSet("user_told_requirement", True)]

class ExtractMobilePhoneOnBudget(Action):

    def name(self) -> Text:
        return "action_extract_mobile_phone_on_budget"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # fetch mobile phone on budget
        entities = tracker.latest_message['entities']
        #print(entities)

        name = ""
        price = 0
        response = ""
        user_told_requirement = tracker.get_slot('user_told_requirement')
        if user_told_requirement:
            for e in entities:
                if e['entity'] =='price':
                    budget = e['value']

                    if int(budget) <= 0:
                        response = mobile_responses.wrongInput()
                        dispatcher.utter_message(json_message=response)
                        return [UserUtteranceReverted()]
                        
                        
                    else:
                        if budget == "10000":
                            name="redmi"
                            price = 10000
                        elif budget == "20000":
                            name="realme"
                            price = 20000

                        response = mobile_responses.fetch_mobile_response({'mobile_name':name,'price':price})
                else:

                    response = mobile_responses.wrongInput()
                    dispatcher.utter_message(json_message=response)
                    return [UserUtteranceReverted()]
                    

        if not user_told_requirement:
            response = mobile_responses.wrongInput()
            dispatcher.utter_message(json_message=response)
            return [UserUtteranceReverted()]
         
        dispatcher.utter_message(json_message=response)

        return [SlotSet("user_told_requirement", False)]
    
