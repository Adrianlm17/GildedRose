from src.item import *



class NormalItem(Item):



    def __init__(self, name, sellIn, quality):

        Item.__init__(self, name, sellIn, quality)

        
    
    def setSellIn(self):

        self.sellIn = self.sellIn - 1

    

    def setQuality(self, price):

        if self.quality + price >= 50:

            self.quality = 50


        elif self.quality + price >= 0:

            self.quality += price


        else:

            self.quality = 0



    def updateQuality(self):

        if self.quality > 0:

            self.setQuality(-1)


        else:

            self.setQuality(-2)

        
        self.setSellIn()
