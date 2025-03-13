from requests import get, post
from bs4 import BeautifulSoup
from time import sleep

url='https://savelshoes.gr/katastima/andrika-papoutsia/padofles/andrikes-pantofles-panines-1-624-24524-19-adams/'
discord_url='https://discord.com/api/webhooks/1349423699673088020/N4BlPdR3LEWOMSX72LZG0rKglR1OheEyEkBK0j-mzD_YfEroM9sdV3Qxn-Ij_lhZ5E0S'

while(True):
    html=get(url)
    soup=BeautifulSoup(html.content, 'html5lib')

    if len(soup.find('p', {"class": "price"}).text) > 1:
        post(discord_url, json={"content": "get in loser, we\'re going shopping"})

    sleep(86400)    #send a message once everyday