from src.domain.normalItem import *



class AgedBrie(NormalItem):



    def __init__(self, name, sellIn, quality):
    
        Item.__init__(self, name, sellIn, quality)



    def setQuality(self, price):

        if self.quality + price <= 50:
        
            self.quality += price
        

        else:
        
            self.quality = 50



    def updateQuality(self):

        if self.sellIn > 0:
        
            self.setQuality(+1)
        

        else:
        
            self.setQuality(+2)
        
        
        self.setSellIn()
    