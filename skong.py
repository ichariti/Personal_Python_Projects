from requests import get, post
from bs4 import BeautifulSoup
from time import sleep

url='https://store.steampowered.com/app/1030300/Hollow_Knight_Silksong/'
hook='https://discord.com/api/webhooks/1355189948168278261/WypX4P9tx-ijTTfZ-jNfW4RXYZwgK5KQU51bk530ZytAmC4Avublpxw4FICgAxbs6ZNV'

while(True):
    try:
        html=get(url)
    except:
        print("HTTP GET request failed")
        continue
    soup=BeautifulSoup(html.content, 'html5lib')
    if(soup.find('div', {'class': 'date'}).text == 'To be announced'):
        post(hook, json={'content':'keep huffing copium'})
    else:
        post(hook, json={'content':"guess it wasn't a fever dream after all. SHAW!"})

    sleep(86400)      
