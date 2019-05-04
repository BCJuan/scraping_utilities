#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 17:02:59 2018

@author: juan
"""

from requests import get
from bs4 import BeautifulSoup
from re import compile as recompile
from urllib.parse import urljoin
from random import sample
import pickle
import os

class ProxyRotator():
    
    def __init__(self, reload=False):
        
        if os.path.exists("proxies") and not reload:
            with open("proxies", "rb") as file:
                self.proxies = pickle.load(file)
        else:
            self.get_proxies()
        
    def get_proxies(self):
    
        #page where proxies are lsited
        base = "https://free-proxy-list.net/"
        
        #request, and conten t retrieval
        req = get(base)
        html = req.content
        soup = BeautifulSoup(html, 'html.parser')
        
        #find rows of table of proxies
        table = soup.find('table', id='proxylisttable').find_all('tr')
       
        #set
        proxies = set({})
        
        #for every row check if it is from eliteproxy (neither transparent nor anonymous) and if it is https
        for i in table:
            if i.contents[4].text == "elite proxy" and i.contents[6].text== 'yes':
                proxy = str(i.contents[0].text) + ":" + str(i.contents[1].text)
                proxies.add(proxy)
        
        self.proxies = proxies
        
        with open("proxies", "wb") as file:
            pickle.dump(self.proxies, file)
        
    def proxy_server(self):
        i = sample(self.proxies, 1)[0]
        return {"https":i}

class UserAgentRotator():
    
    def __init__(self, reload=False):
        
        if os.path.exists("users") and not reload:
            with open("users", "rb") as file:
                self.user_agents = pickle.load(file)
        else:
            self.get_users()
    
    def get_users(self):
        
        base = "https://developers.whatismybrowser.com/useragents/explore/"
        
        req = get(base)
        soup = BeautifulSoup(req.content, 'html.parser')
        
        different_types = soup(text=recompile(r'(Linux|Computer|Chrome|Web Browser)'))
        
        user_agents = set({})
        for i in different_types:
            link = urljoin(base,i.parent.get('href'))
            
            req = get(link)
            soup = BeautifulSoup(req.content, 'html.parser')

            users = soup.find_all('td', class_='useragent')
            for j in users:
                user_agents.add(j.get_text())
                
        self.user_agents = user_agents
        
        with open("users", "wb") as file:
            pickle.dump(self.user_agents, file)
        
        
    def user_agent_server(self):
        
        return sample(self.user_agents,1)[0]
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        