class GildedRose:



    def __init__(self, items):
 
        self.items = items
        


    def updateGildedRose(self):
     
        for item in self.items:
        
            item.updateQuality()
