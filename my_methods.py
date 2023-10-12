# your_module.py
from metaphor_python import Metaphor
import openai
import time 
import ast
import json
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#fix the api thing to maintain privacy

try:
    with open('open_api_key.txt', 'r') as file:
        open_api_key = file.read().strip()  # Read and remove leading/trailing whitespaces
except:
    pass

try:
    with open('metaphor_api_key.txt', 'r') as file:
        metaphor_api_key = file.read().strip()  # Read and remove leading/trailing whitespaces
    
except:
    pass


metaphor = Metaphor(metaphor_api_key)

def process_article(url):
    SYSTEM_MESSAGE = "You are a helpful assistant which extract information from a page and responds only with a Python dictionary containing the information."
    content = search_response.results[0]
    USER_QUESTION = "This is an import article article in %s?" %content

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": USER_QUESTION},
        ],
    )
    return ast.literal_eval(completion.choices[0].message.content)

def find_classic_papers(query):
    SYSTEM_MESSAGE = "You are a helpful assistant which writes search queries to look for classic research articles in scientific fields."
    USER_QUESTION = "What are trending articles in %s?" %query 

    completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_MESSAGE},
                {"role": "user", "content": USER_QUESTION},
            ],
        )

    search_response = metaphor.search(completion.choices[0].message.content, num_results=10, use_autoprompt=True)  # You can adjust the number of results as needed
    output = []
    # Retrieve information about the papers
    for result in search_response.results:
        _ = {"Title:": result.title,"Authors:": result.author, "Published Date:": result.published_date, "URL:": result.url }
        output.append(_)
    return output

def find_trending_papers(query):
    SYSTEM_MESSAGE = "You are a helpful assistant which writes search queries to look for trending research articles in scientific fields."
    USER_QUESTION = "What are trending articles in %s?" %query 

    completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_MESSAGE},
                {"role": "user", "content": USER_QUESTION},
            ],
        )

    search_response = metaphor.search(completion.choices[0].message.content, num_results=10, use_autoprompt=True)  # You can adjust the number of results as needed
    output = []
    # Retrieve information about the papers
    for result in search_response.results:
        _ = {"Title:": result.title,"Authors:": result.author, "Published Date:": result.published_date, "URL:": result.url }
        output.append(_)
    return output

def find_summaries(query):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant which gives a one-paragraph summary about a topic."},
        {"role": "user", "content": "What is algebraic number theory?"}
        ]
    )
    return response.choices[0].message.content

def find_terminology(query):
    SYSTEM_MESSAGE = "You are a helpful assistant which teaches me about terminology, and outputs only them \
                    in the form of a Python dictionary with the keys being the term, and the value being the explanation."
    USER_QUESTION = "What are some important terminologies in %s?" %query 

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": USER_QUESTION},
        ],
    )
    dictionary = ast.literal_eval(completion.choices[0].message.content)

    return dictionary

    # url = "https://api.metaphor.systems/search"
    # payload = {
    #     "numResults": 10,
    #     "query": "Here are some terms in natural language processing",
    #     # "includeDomains": ["en.wikipedia.org"]
    # }
    # headers = {
    #     "accept": "application/json",
    #     "content-type": "application/json",
    #     "x-api-key": "c1a0f4a6-369a-4fca-adab-3c6ba625630c"
    # }
    # response = requests.post(url, json=payload, headers=headers)
    # output = response.json()['results']
    # return [output[i]['url'] for i in range(len(output))]

def find_books(query):
    metaphor = Metaphor(metaphor_api_key)
    updated_query = 'find notable book in %s' %query
    search_response = metaphor.search(updated_query, use_autoprompt=True)
    return [result.url for result in search_response.results]



