from src.domain.normalItem import *



class BackstagePasses(NormalItem):



    def __init__(self, name, sellIn, quality):
        
        Item.__init__(self, name, sellIn, quality)



    def updateQuality(self):

        if self.sellIn < 0:

            self.quality = 0
        
        
        elif self.sellIn == 0:

            self.setQuality(50)
        

        elif self.sellIn <= 5:
            
            self.setQuality(+3)


        elif self.sellIn <= 10:

            self.setQuality(+2)


        else:

            self.setQuality(+1)
        

        self.setSellIn()
