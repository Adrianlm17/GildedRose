from src.main import *

import pytest 



@pytest.fixture
def stocktaking():

    item = AgedBrie("Aged Brie", 2, 0)
    return item



@pytest.mark.test_AgedBrie
def test_AgedBrie(stocktaking):

    # ITEM: Aged Brie   
    
    dayOne        = AgedBrie("Aged Brie", 1, 1)
    dayTwo        = AgedBrie("Aged Brie", 0, 2)
    dayThree      = AgedBrie("Aged Brie", -1, 4)
    dayFive       = AgedBrie("Aged Brie", -3, 8)
    dayTen        = AgedBrie("Aged Brie", -8, 18)
    dayFifteen    = AgedBrie("Aged Brie", -13, 28)
    dayTwenty     = AgedBrie("Aged Brie", -18, 38)
    dayTwentyFive = AgedBrie("Aged Brie", -23, 48)
    dayThirty     = AgedBrie("Aged Brie", -28, 50)


    stocktaking.updateQuality()
    assert repr(dayOne) == repr(stocktaking)

    stocktaking.updateQuality()
    assert repr(dayTwo) == repr(stocktaking)

    stocktaking.updateQuality()
    assert repr(dayThree) == repr(stocktaking)

    stocktaking.updateQuality()
    assert repr(dayFive) == repr(stocktaking)

    stocktaking.updateQuality()
    assert repr(dayTen) == repr(stocktaking)

    stocktaking.updateQuality()
    assert repr(dayFifteen) == repr(stocktaking)

    stocktaking.updateQuality()
    assert repr(dayTwenty) == repr(stocktaking)

    stocktaking.updateQuality()
    assert repr(dayTwentyFive) == repr(stocktaking)

    stocktaking.updateQuality()
    assert repr(dayThirty) == repr(stocktaking)
