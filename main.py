from time import sleep
from threading import Thread
import apiconnect as api

def func():

    api.auction_house_download(1084) #id tarenmill



while True:
        Thread(target=func()).start()
        sleep(4000)

