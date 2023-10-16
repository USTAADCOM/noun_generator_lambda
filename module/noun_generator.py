"""
noun generator module will take the string and return the nouns list in string.
"""
import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key  = os.getenv('OPENAI_API_KEY')

def make_prompt(paragraph: str)-> str:
    """
    make_prompt take paragrapph as input and retirn the prompt with the given
    pargraph.

    Parameters
    ----------
    paragraph: str
        string text to find the nouns.
    
    Return
    ------
    prompt: str
        prompt to find the nouns from given paragraph.
    """
    prompt = f"""
    You are a grammar expert you have given a paragraph {paragraph}.\
    Find the nouns from given paragraph. \
    Return each Noun only once. \
    And return the response as ["target 1", "target2"]. \
    """
    return prompt
    
def get_noun(paragraph, model = "gpt-3.5-turbo"):
    """
    get_noun method take paragraph and model as input and return the output
    according to the prompt.

    Parameters
    ----------
    prompt: str
        paragraph to generate the output.
    model: str
        model name.
    
    Return
    ------
        return reponse containig the nouns found in given paragraph.
    """
    prompt = make_prompt(paragraph)
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages,
        temperature = 1, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
