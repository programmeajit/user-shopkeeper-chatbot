from g_response import mobile_voiceover_response,question_on_budget,worong_input

def fetch_mobile_response(mobile_details):
    output = {
        'response_type': 'Answer',
        'voice_over_text': mobile_voiceover_response().replace('%s',mobile_details['mobile_name']),
        'details':{
            'name': mobile_details['mobile_name'],
            'price': mobile_details['price']
        }
    }
    return output

def wrongInput():
    output = {
        'response_type': 'Answer',
        'message': worong_input(),
    }
    return output

def questionOnBudget():
    output = {
        'response_type': 'question',
        'question': question_on_budget(),
    }
    return output


# mobile_response({'mobile_name':'redmi','price':2000})