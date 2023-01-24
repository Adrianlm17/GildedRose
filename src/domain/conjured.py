from src.domain.normalItem import *



class Conjured(NormalItem):



    def __init__(self, name, sellIn, quality):
        
        Item.__init__(self, name, sellIn, quality)



    def updateQuality(self):
        
        if self.sellIn >= 0:
            
            self.setQuality(-2)


        else:
            self.setQuality(-4)


        self.setSellIn()
    