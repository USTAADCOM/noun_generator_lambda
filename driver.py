"""
module contain the testing method for the created lanbda endpoints.
"""
import json
from lambda_function import lambda_handler
def test_noun_generator(json_data: json, content)-> None:
    """
    input json file and return the nouns from the given string results.

    Parameters
    ----------
    json_data: json
        json data containing the request content.

    Return
    ------
    None
    """
    result = lambda_handler(json_data, content)
    print(result)

CONTENT = None
json_data = {}
data = {
        "paragraph" : "Pakistan Pakistan is is my country"
       }
json_data["body"] = json.dumps(data)
test_noun_generator(json_data, CONTENT)
