# Data import
import requests 
from urllib.parse import urlencode


def get_data_ya_disk(data_keys):
    
    """
    Params:
        - list of public urls to ya disk files        
    Return:
        - list of download urls
    """
    
    # Base url
    ya_disk_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?' 
    
    # Direct URLs to the files
    download_urls = []
    
    for k in data_keys:
        public_key  = urlencode(dict(public_key=k))
        request_url = ya_disk_url + public_key
        r = requests.get(request_url) 
        download_urls.append(r.json()['href'])
        
    return download_urls

