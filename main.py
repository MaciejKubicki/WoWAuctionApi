from wowapi import WowApi

list_of_realms = []
api = WowApi('0d7282069bad432c8cac95125523f7cf','wLcGwQgP72kzpMzH81I8siD4UbZTlH2f') #key and secretkey from blizzardapi
#server_id = api.get_realm_index('eu', list)

name_of_realms_dict = api.get_realm_index('eu', 'dynamic-eu')

def add_to_list_realms(name_of_realms):
    for x in range(len(name_of_realms['realms'])):
        list_of_realms.append(name_of_realms['realms'][x])

add_to_list_realms(name_of_realms_dict)


