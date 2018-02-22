import xml.etree.ElementTree as ET
import re

class XMLReader(object):
    def __init__(self,xml_string):
        self.__root = ET.fromstring(xml_string)
        #self.__root = self.__tree.getroot()

        self.__storing_ongepland = self.__root[0].findall('Storing')
        self.__storing_gepland   = self.__root[1].findall('Storing')

    def __on_conv_rule(self,storing_list):
        traj  = storing_list.find('Traject').text
        datu  = storing_list.find('Datum').text
        msg   = storing_list.find('Bericht').text
        msg = re.sub(r'<br/>','\n\n',msg)
        msg = (re.sub(r'<.+>','',msg)).strip()
            
        return [datu,traj,msg]

    def __conv_rule(self,storing_list):
        traj  = storing_list.find('Traject').text
        peri  = storing_list.find('Periode').text
        msg   = storing_list.find('Bericht').text
        msg = re.sub(r'<br/>','\n\n',msg)
        msg = (re.sub(r'<.+>','',msg)).strip()
            
        return [peri,traj,msg]
    
    def ongepland_storing(self):
        storing_list = list(map(self.__on_conv_rule,self.__storing_ongepland))
        return storing_list


    def gepland_storing(self):
        storing_list = list(map(self.__conv_rule,self.__storing_gepland))
        return storing_list


