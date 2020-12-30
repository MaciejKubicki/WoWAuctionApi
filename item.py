class Item:

    def __init__(self):


        self.item_name
        self.id_item = 0
        self.price = 0
        self.list_with_same_id = []
        self.url = ''
        self.time_left = ''


    def make_url(self):
        """ wowhead url """
        self.url = "https://www.wowhead.com/item="+str(self.id_item)