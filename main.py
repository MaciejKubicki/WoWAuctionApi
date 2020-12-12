from wowapi import WowApi

list = []
api = WowApi('0d7282069bad432c8cac95125523f7cf','wLcGwQgP72kzpMzH81I8siD4UbZTlH2f') #key and secretkey from blizzardapi
#server_id = api.get_realm_index('eu', list)

name_of_realms = api.get_realm_index('eu', 'dynamic-eu')
api.get_realm('eu','dynamic-eu',)
#api.get_account_profile_summary('eu','')
#api.get_auctions('eu', 'silvermoon', locale='de_DE')
