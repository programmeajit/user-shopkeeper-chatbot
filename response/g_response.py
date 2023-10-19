import json 

# read data.json file 
myJsonFile = open('/home/ubuntu/data/data.json','r')
jsonData = myJsonFile.read()
obj = json.loads(jsonData)

def mobile_voiceover_response():
        response = obj['voiceover_text']
        return response

def question_on_budget():
        response = obj['question_on_budget']
        return response
 
def worong_input():
        response = obj['wrong_input']
        return response