import yaml
import requests
import json

class utils:

    def config_yml():
        with open('./WebScraping/config.yml') as f:
            return yaml.load(f, Loader=yaml.FullLoader)
        
    def braveAPICaller(token,url):
        headers={'X-Subscription-Token':token}
        response = requests.get(url=url, headers=headers)
        output = json.dumps(response.json(), indent=4)
        outputNew = json.loads(output)
        urlList = []
        for i in outputNew['web']['results']:
            if 'www.amazon.com' in i['url']:
                urlList.append(i['url'])
        
        return urlList

