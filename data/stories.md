## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks
 
## story_name
* name{"name":"Sam"}
 - utter_greet
 

## story_joke_01
* joke
 - action_joke
 
## story_joke_02
 - utter_greet
* greet
 - utter_name
* name{"name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_greet
* unable_leave
 - action_getdata
* joke
 - action_joke
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 
## Generated Story -4980125356062770860
* greet
    - utter_name
* name{"name": "ravi"}
    - slot{"name": "ravi"}
    - utter_greet
* unable_leave
    - action_getdata
* unable_leave
    - action_getdata
* unable_leave
    - utter_issue
* unable_leave
    - utter_issue
* unable_leave
    - utter_issue

## Generated Story -1677822218857204854
* greet
    - utter_name
* name
    - utter_greet
    - action_default_fallback
    - rewind
* greet
    - utter_name
* name{"name": "kiran"}
    - slot{"name": "kiran"}
    - utter_greet
* unable_leave
    - utter_issue

## Generated Story -8601085139550001272
* greet
    - utter_name
* name
    - utter_greet
    - action_default_fallback
    - rewind
* name
    - utter_greet
* unable_leave
    - action_getdata

## Generated Story -1086709628166355294
* greet
    - utter_name
* name{"name": "surya"}
    - slot{"name": "surya"}
    - utter_greet
* unable_leave
    - action_getdata

## Generated Story -5544566689468315127
* greet
    - utter_name
* name
    - utter_greet
* name{"name": "surya"}
    - slot{"name": "surya"}
    - utter_greet
* unable_leave{"tool": "ess"}
    - action_getdata

## Generated Story 7897665747721065543
* greet
    - utter_name
* joke
    - action_joke
* unable_leave
    - action_getdata
* unable_leave
    - action_getdata

## Generated Story -7117285546512434209
* unable_leave{"tool": "ess"}
    - action_getdata

## Generated Story 6494661869973955918
* greet
    - utter_name
* unable_leave
    - action_getdata

