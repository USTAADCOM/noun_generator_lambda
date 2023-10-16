# Noun Generator Lambda
AWS lambda function take text string as input and return the nouns list from this paragraph as output.
## Setup
  ```code
  git clone https://github.com/USTAADCOM/noun_generator_lambda.git
  cd noun_generator_lambda
  pip install requirements.txt -q
  ```
## .env setup
create .env and put your key
```code
OPENAI_API_KEY = "your sceret key here"
```
## Payload and Response 
 
Payload
```code
    {
      "paragraph" : "Your string here",
    }
```
Response 
```code
    {
      'statusCode': 200, 
      'body': "[noun1, noun2, noun3 ....., noun N]"
    }
```
