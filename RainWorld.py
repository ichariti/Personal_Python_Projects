from requests import get, post
from bs4 import BeautifulSoup
from time import sleep

URL='https://store.steampowered.com/app/2857120/Rain_World_The_Watcher/'
dURL='https://discord.com/api/webhooks/1355172811261476995/7FUPk5S155NOom4r6T285oBONEiuwHFBnZ30UwBmQ0nl1CL8nHwZtFi60yxYvTn4U_d3'

while(True):
    HTML=get(URL)
    SOUP=BeautifulSoup(HTML.content, 'html5lib')
    if (SOUP.find('span', {'class': "not_yet"})==None):
        post(dURL, json={"content": "slugcatting time"})
    else:
        post(dURL, json={"content": "time is an illusion, and so are pants"})

    sleep(1200)
