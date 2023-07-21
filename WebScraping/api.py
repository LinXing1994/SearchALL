import json
from utils import utils
from urlsearcher import braveCaller

config = utils.config_yml()
token = config['API']['token']

def queryInput():
    userInput = input("Please tell us what you want to search: ")
    urlFetcher = braveCaller(userInput)
    url = urlFetcher.urlProducer()
    response = utils.braveAPICaller(token,url)
    return response 


print(queryInput())
