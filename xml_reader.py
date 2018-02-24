#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
@Author: Xinshuo Gu 
@Date: 2018-02-21 21:00:24 
@Last Modified by: Xinshuo Gu 
@Last Modified time: 2018-02-24 11:41:24 
'''

'''
Here defines Class XMLReader 
to extract the information from NS API
'''

import xml.etree.ElementTree as ET
import re

import xml_getter

class XMLReader(xml_getter.XMLGetter):
    
    def __init__(self):
        xml_string = super().storingText()          # use the method from XMLGetter to get the API text
        self.__root = ET.fromstring(xml_string)
        #self.__root = self.__tree.getroot()

        self.__storing_ongepland = self.__root[0].findall('Storing')
        self.__storing_gepland   = self.__root[1].findall('Storing')

    def __on_conv_rule(self,storing_list):
        traj  = storing_list.find('Traject').text
        datu  = storing_list.find('Datum').text
        msg   = storing_list.find('Bericht').text   # formatting all the information
        msg = re.sub(r'<br/>','\n\n',msg)
        msg = (re.sub(r'<.+>','',msg)).strip()      # delete unuseful labels and spaces
        
        return [datu,traj,msg]

    def __conv_rule(self,storing_list):
        traj  = storing_list.find('Traject').text
        peri  = storing_list.find('Periode').text
        msg   = storing_list.find('Bericht').text   # formatting all the information
        msg = re.sub(r'<br/>','\n\n',msg)           
        msg = (re.sub(r'<.+>','',msg)).strip()      # delete unuseful labels and spaces
            
        return [peri,traj,msg]
    
    def ongepland_storing(self):
        storing_list = list(map(self.__on_conv_rule,self.__storing_ongepland))  # use "map" to convert the information into desired formatting
        return storing_list


    def gepland_storing(self):
        storing_list = list(map(self.__conv_rule,self.__storing_gepland))       # use "map" to convert the information into desired formatting
        return storing_list

    # return a list of a list containing [peri,traj,msg] for each disruption
