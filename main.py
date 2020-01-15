from datetime import datetime
from pytz import timezone
import requests

def singleton(cls):
    instances = dict()
    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrap

@singleton
class ElasticSearch():
    """
        Parameters
        ----------
        host: str  -- host of elasticsearch
        index: str -- index of elasticsearch
    """

    FORMAT = '%Y-%m-%dT%H:%M:%S-05:00'
    TIME_ZONE = timezone('America/Bogota')
    HEADERS = {'Content-Type': 'application/json'}

    def __init__(self, **kwargs):
        """
        """
        self.url = f'{kwargs.get("host")}/{kwargs.get("index")}/request'

    def send_message_to_elastic(self, message: dict):
        """
            Send message to ElasticSearch
            Parameters
            ----------
            message: dict
        """
        document = {
            "timestamp": datetime.now(self.TIME_ZONE).strftime(self.FORMAT),
            "message": message
        }
        response_elastic = requests.post(self.url, json=document, headers=self.HEADERS)
        print('response', response_elastic)

data = {'name':'Santiago', 'age': 23}
obj_elasticsearch = ElasticSearch(host='http://localhost:9200', index='INDEX_NAME')
obj_elasticsearch.send_message_to_elastic(data)

