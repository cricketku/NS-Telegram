import requests
import importlib


class XMLGetter(object):
    __login_url = 'http://webservices.ns.nl/ns-api-storingen?actual=true'
    __login_keys = importlib.import_module('login_token') 
    __login_name = __login_keys.login_name
    __login_pass = __login_keys.login_pass

    def storingText(self):
        xml_session = requests.get(self.__login_url,auth = (self.__login_name,self.__login_pass))
        stor_text = xml_session.text
        return stor_text