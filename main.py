class BaseAdvertising:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.clicks = 0
        self.views = 0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_clicks(self):
        return self.clicks

    def get_views(self):
        return self.views

class Advertiser(BaseAdvertising):

    all_advertisers = []

    def __init__(self, id, name):
        super(Advertiser, self).__init__(id, name)
        Advertiser.all_advertisers.append(self)

    def inc_views(self):
        self.views += 1

    def inc_clicks(self):
        self.clicks += 1

    def help(self):
        print("Name:"+self.name)

    def describe_me(self):
        print("Advertiser")

    @staticmethod
    def get_total_clicks():
        total_clicks = 0
        for i in range(len(Advertiser.all_advertisers)):
            total_clicks += Advertiser.all_advertisers[i].get_clicks()
        return total_clicks

class Ad(BaseAdvertising):

    def __init__(self, id, name, img_url, link, advertiser: Advertiser = None):
        super(Ad, self).__init__(id, name)
        self.img_url = img_url
        self.link = link
        self.advertiser = advertiser

    def get_img_url(self):
        return self.img_url

    def set_img_url(self, img_url):
        self.img_url = img_url

    def inc_clicks(self):
        self.clicks += 1
        self.advertiser.inc_clicks()

    def inc_views(self):
        self.views += 1
        self.advertiser.inc_views()

    def set_advertiser(self, advertiser):
        self.advertiser = advertiser


base_advertising = BaseAdvertising("idid", "namename")
advertiser1 = Advertiser(1,"Advertiser1")
advertiser2 = Advertiser(2,"Advertiser2")
ad1 = Ad(1, "title1", "url1", "link1", advertiser1)
ad2 = Ad(2, "title2", "url2", "link2", advertiser2)
ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad2.inc_views()
ad1.inc_clicks()
ad1.inc_clicks()
ad2.inc_clicks()
print(advertiser2.get_name())
print(ad1.get_clicks())
print(advertiser2.get_clicks())
print(Advertiser.get_total_clicks())
print(advertiser1.get_views())




