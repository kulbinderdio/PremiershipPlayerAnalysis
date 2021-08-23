import requests
import pandas as pd
from lxml import html
import numpy as np

user_agent = {'User-agent': 'Mozilla/5.0'}
response = requests.get('https://www.premierleague.com/clubs', headers = user_agent)
tree = html.fromstring(response.content)
urlPrefix = "https://www.premierleague.com"
playersList = []

def playerInfoExtract(playerURL, club):
    response = requests.get(playerURL, headers = user_agent)
    tree = html.fromstring(response.text)            
    
    firstItem = lambda x:x[0] if len(x)>0 else np.nan
    secondItem = lambda x:x[1] if len(x)>1 else np.nan
    shirtNo = firstItem(tree.xpath('//div[@class="number t-colour"]/text()'))
    height = firstItem(tree.xpath('//div[@class="personalLists"]/ul[@class="pdcol3"]/li/div[@class="info"]/text()'))
    weight = secondItem(tree.xpath('//div[@class="personalLists"]/ul[@class="pdcol3"]/li/div[@class="info"]/text()'))
    nationality = firstItem(tree.xpath('//span[@class="playerCountry"]/text()'))
    dob = firstItem(tree.xpath('//div[@class="personalLists"]/ul[@class="pdcol2"]/li/div[@class="info"]/text()'))
    

    playerURL = playerURL.replace('overview','stats')
    print(playerURL)
    response = requests.get(playerURL, headers = user_agent)
    
    tree = html.fromstring(response.text)
    appearances = tree.xpath("//div[@class='topStat'][1]/span/span/text()")[0]
    goals = tree.xpath("//div[@class='topStat'][2]/span/span/text()")[0]
    wins = tree.xpath("//div[@class='topStat'][3]/span/span/text()")[0]
    losses = tree.xpath("//div[@class='topStat'][4]/span/span/text()")[0]
    
    
    playerData = {"club":club,
                "name":tree.xpath('//div[@class="name t-colour"]/text()')[0],
               "shirtNo":shirtNo,
               "nationality":nationality,
               "dob":dob,
               "height":height,
               "weight":weight,
                 "appearances":appearances,
                 "goals":goals,
                 "wins":wins,
                 "losses":losses}
    
    print (playerData)
    return playerData
    
    

def getClubURLs():
    clubs = []
    response = requests.get('https://www.premierleague.com/clubs', headers = user_agent)
    tree = html.fromstring(response.content)
    urlPrefix = "https://www.premierleague.com"
    clubURLs = tree.xpath("//div[contains(@class, 'indexSection')]/div/ul/li/a/@href")
    
    for club in clubURLs:
        clubs.append(urlPrefix + club.replace('overview','squad'))

    return clubs

def getClubsPlayerURLs(clubURL, clubName):
    response = requests.get(clubURL, headers = user_agent)
    tree = html.fromstring(response.content)

    players = tree.xpath("//ul[contains(@class,'squadListContainer')]/li/a/@href")

    for player in players:
        print(urlPrefix + player)
        playersList.append(playerInfoExtract(urlPrefix + player,clubName))
    

clubURLs =  getClubURLs()
for club in clubURLs:
    name = club[0:club.find('/squad')]
    clubName = name[name.rfind('/')+1:]
    getClubsPlayerURLs(club, clubName)
    print(len(playersList))
