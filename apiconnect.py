import realmlist  # first realmlist execute then apiconnect !!!
from wowapi import WowApi
import json
import os
import datetime

key = '0d7282069bad432c8cac95125523f7cf'
secretkey = 'wLcGwQgP72kzpMzH81I8siD4UbZTlH2f'

api = WowApi(key, secretkey)


def current_date():
    """ return date m/d/y/h/m/s """
    current_date = datetime.datetime.now()
    string_date = current_date.strftime("%m_%d_%Y_%H_%M_%S")
    return string_date


def save_file_json(file_to_save, id_group_server):
    """ save downlaod file, taking arg id_group_server """
    with open('ah_' + str(id_group_server) + '_' + current_date() + '.json', 'w') as json_file:
        json.dump(file_to_save, json_file, indent=2)


def auction_house_download(id_group_servers, region='eu', dynamic='dynamic-eu'):
    """ send request to get auction house file, saveing it in Json with current date """

    json_ah_file = api.get_auctions(region, dynamic, id_group_servers)
    save_file_json(json_ah_file, id_group_servers)
    print(current_date()+' pobrano auction house')
    return json_ah_file
