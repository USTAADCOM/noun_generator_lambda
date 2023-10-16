"""
lamda metod mmodule 
"""
import json
from module import noun_generator
def make_success_response(output_data: dict)-> dict:
    """
    method take Tool data and return a response.

    Parameters

    ----------
    output_data: dict
        data dictionary return as output by requested Tool.

    Return
    ------
    dict
        return response as dictionary.
    
    """
    response_data = {
        "statusCode": 200,
        'headers': {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*'
                },
        "body": output_data
        }
    return response_data

def lambda_handler(event_jsonified, context):
    """
    lambda handler method recive the json data and return the response as json file.

    Parameters
    ----------

    event_jsonified: json
        json request data.
    context: Null
        null.
    Return
    ------
        return json resposne as a result according to the request.
    """
    output = {}
    try:
        if "body" not in event_jsonified:
            output["Error"] = "Bad Params"
            output["Message"] = "Body Params not found"
            return {
                "statusCode": 400,
                'headers': {
                            'Access-Control-Allow-Headers': '*',
                            'Access-Control-Allow-Origin': '*',
                            'Access-Control-Allow-Methods': '*'
                        },
                "body" : json.dumps(output)
                }
        else:
            event = event_jsonified['body']
            event = json.loads(event, strict = False)
            paragraph = event['paragraph']
            output =  noun_generator.get_noun(paragraph)
            response = make_success_response(output)
            return response

    except Exception as error:
        output["Error"] = error
        output["Message"] = "Internal Server Error"
        response = {
            'statusCode': 500,
            'headers': {
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*'
                    },
            'body' : json.dumps(output)
            }
        return response
