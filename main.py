from selenium_driver import driver
from slack_client import client
import time

driver.get('https://www.tolvapc.co.uk/shop-2/offers/offers-offers/msi-geforce-rtx-2060-gaming-z-6gb-graphics-card/')

## Can you use this code to confirm you have done the correct css_selector path
# print(e.text) 

def isAvailableText(driver):
    e = driver.find_element_by_css_selector('.page-container > div > div > div > div > div > div > div > span')
    return e.text

def checkWebsite():
    print('refreshing page...')
    driver.refresh()
    try:
        availableText = isAvailableText(driver)
        if availableText == 'SOLD OUT':
            text_to_send = 'SOLD OUT'
        else:
            text_to_send = availableText + ' ' + '<@U027V06DZ60>'  # Place your slack id after the @
    except Exception as e:  # Sometimes slack breaks for unknown reason so we catch this
        text_to_send = str(e)
        
    if text_to_send != "SOLD OUT":
        client.chat_postMessage(channel='#trade', text=text_to_send)
        print('sent a message: ' + text_to_send)

waited = 0
while True:
    checkWebsite()
    # This used to run every 5 minutes.
    # I modified it to run every 10 minutes.
    print(f'waited for: {waited} minutes')
    # every 3 hours, make sure that this bot's still working
    if waited % 180 == 0:
        print("the bot's still working!")
        client.chat_postMessage(channel='#trade', text='update on the bot - still working!')
    for _ in range(10):
        time.sleep(60)
        waited += 1
