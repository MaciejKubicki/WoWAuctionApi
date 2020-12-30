import realmlist as rl
import item

"""
 https://www.wowhead.com/item=x    id=82800 = pet_cage
 test['auctions'][0]['item']['id']
"""

def open_ah_json(path):
    """data auctionhouse"""

    ah_data = rl.open_json_file(path)
    return ah_data

file_path = 'test_file.json'

test = open_ah_json(file_path)

class_list = []
"""
loop adding 
"""
for class_item in range(len(test['auctions'])):
    create_class = item.Item()
    create_class.id_item = test['auctions'][class_item]['item']['id']
    create_class.time_left = test['auctions'][class_item]['time_left']
    create_class.make_url()

    #create_class.price = test['auctions'][class_item]['buyout']
    class_list.append(create_class)
