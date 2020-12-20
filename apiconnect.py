import realmlist # first realmlist execute then apiconnect !!!
from wowapi import WowApi
import os

key= '0d7282069bad432c8cac95125523f7cf'
secretkey ='wLcGwQgP72kzpMzH81I8siD4UbZTlH2f'

api = WowApi(key,secretkey)

def auction_house(region = 'eu', dynamic = 'dynamic-eu', id_group_servers):
    json_ah_file = api.get_auctions(region,dynamic,id_group_servers)
    return json_ah_file
