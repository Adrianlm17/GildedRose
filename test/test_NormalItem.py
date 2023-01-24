from src.domain.normalItem import *

import pytest 



@pytest.fixture
def stocktaking():

    item = NormalItem("Elixir of the Mongoose", 5, 7)
    return item



@pytest.mark.test_NormalItem
def test_NormalItem(stocktaking):    
    
    
    # ITEM: Elixir of the Mongoose    
    
    dayOne        = NormalItem("Elixir of the Mongoose", 4, 6)
    dayTwo        = NormalItem("Elixir of the Mongoose", 3, 5)
    dayThree      = NormalItem("Elixir of the Mongoose", 2, 4)
    dayFive       = NormalItem("Elixir of the Mongoose", 0, 2)
    dayTen        = NormalItem("Elixir of the Mongoose", -5, 0)
    dayFifteen    = NormalItem("Elixir of the Mongoose", -10, 0)
    dayTwenty     = NormalItem("Elixir of the Mongoose", -15, 0)
    dayTwentyFive = NormalItem("Elixir of the Mongoose", -20, 0)
    dayThirty     = NormalItem("Elixir of the Mongoose", -25, 0)


    stocktaking.updateQuality()
    assert repr(dayOne) == repr(stocktaking)

    stocktaking.updateQuality()
    assert repr(dayTwo) == repr(stocktaking)

    stocktaking.updateQuality()
    assert repr(dayThree) == repr(stocktaking)

    stocktaking.updateQuality()
    stocktaking.updateQuality()
    assert repr(dayFive) == repr(stocktaking)

    stocktaking.updateQuality()
    stocktaking.updateQuality()
    stocktaking.updateQuality()
    stocktaking.updateQuality()
    stocktaking.updateQuality()
    assert repr(dayTen) == repr(stocktaking)

    stocktaking.updateQuality()
    stocktaking.updateQuality()
    stocktaking.updateQuality()
    stocktaking.updateQuality()
    stocktaking.updateQuality()
    assert repr(dayFifteen) == repr(stocktaking)

    stocktaking.updateQuality()
    stocktaking.updateQuality()
    stocktaking.updateQuality()
    stocktaking.updateQuality()
    stocktaking.updateQuality()
    assert repr(dayTwenty) == repr(stocktaking)

    stocktaking.updateQuality()
    stocktaking.updateQuality()
    stocktaking.updateQuality()
    stocktaking.updateQuality()
    stocktaking.updateQuality()
    assert repr(dayTwentyFive) == repr(stocktaking)

    stocktaking.updateQuality()
    stocktaking.updateQuality()
    stocktaking.updateQuality()
    stocktaking.updateQuality()
    stocktaking.updateQuality()
    assert repr(dayThirty) == repr(stocktaking)
