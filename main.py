from wowapi import WowApi
import os

list_of_realms = []
api = WowApi('0d7282069bad432c8cac95125523f7cf','wLcGwQgP72kzpMzH81I8siD4UbZTlH2f') #key and secretkey from blizzardapi
#server_id = api.get_realm_index('eu', list)

name_of_realms_dict = api.get_realm_index('eu', 'dynamic-eu')

def add_to_list_realms(name_of_realms):
    for x in range(len(name_of_realms['realms'])):
        list_of_realms.append(name_of_realms['realms'][x])

diction = {}
add_to_list_realms(name_of_realms_dict)

#tarren-mill id 1306 slug='tarren-mill'
#conrealserch = api.get_connected_realm('eu','dynamic-eu',1084)
#auction = api.get_auctions('eu','dynamic-eu',1084)
z = api.get_connected_realms('eu','dynamic-eu')

