#-*- coding: UTF-8 -*-

import requests

class Request:
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    }

    def do(url, data=None):
        response = requests.post(url, data=data, headers=Request.headers) 
        return response.content
