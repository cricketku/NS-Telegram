#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
@Author: Xinshuo Gu 
@Date: 2018-02-21 21:00:24  
@Last Modified by: Xinshuo Gu 
@Last Modified time: 2018-02-24 11:40:40 
'''

'''
Here defines Class XMLGetter to get the xml data
from NS API
'''

import requests
import importlib


class XMLGetter(object):
    __login_url = 'http://webservices.ns.nl/ns-api-storingen?actual=true'
    __login_keys = importlib.import_module('login_token') 
    # get your own api login key from ns
    __login_name = __login_keys.login_name
    __login_pass = __login_keys.login_pass

    def storingText(self):
        xml_session = requests.get(self.__login_url,auth = (self.__login_name,self.__login_pass))
        stor_text = xml_session.text
        return stor_text