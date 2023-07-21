class braveCaller():
    def __init__(self,query):
        self.query = query


    def urlProducer(self):
        newQuery= self.query.replace(" ","+")
        # print(newQuery)
        brave_api_url = f'https://api.search.brave.com/res/v1/web/search?q={newQuery}'
        return brave_api_url
    
# test =braveCaller("asus g16")
# print(test.urlProducer())
    
    


