from src.main import *

import pytest 



@pytest.fixture
def stocktakingFirstFirst():

    item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    return item



@pytest.mark.test_BackstagePassesFirst
def test_BackstagePassesFirst(stocktakingFirst):

    # ITEM: Backstage Passes (First)
    
    dayOne        = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 14, 21)
    dayTwo        = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 13, 22)
    dayThree      = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 12, 23)
    dayFive       = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 10, 25)
    dayTen        = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 5, 35)
    dayFifteen    = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 0, 50)
    dayTwenty     = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", -5, 0)
    dayTwentyFive = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", -10, 0)
    dayThirty     = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", -15, 0)


    stocktakingFirst.updateQuality()
    assert repr(dayOne) == repr(stocktakingFirst)

    stocktakingFirst.updateQuality()
    assert repr(dayTwo) == repr(stocktakingFirst)

    stocktakingFirst.updateQuality()
    assert repr(dayThree) == repr(stocktakingFirst)

    stocktakingFirst.updateQuality()
    assert repr(dayFive) == repr(stocktakingFirst)

    stocktakingFirst.updateQuality()
    assert repr(dayTen) == repr(stocktakingFirst)

    stocktakingFirst.updateQuality()
    assert repr(dayFifteen) == repr(stocktakingFirst)

    stocktakingFirst.updateQuality()
    assert repr(dayTwenty) == repr(stocktakingFirst)

    stocktakingFirst.updateQuality()
    assert repr(dayTwentyFive) == repr(stocktakingFirst)

    stocktakingFirst.updateQuality()
    assert repr(dayThirty) == repr(stocktakingFirst)






@pytest.fixture
def stocktakingSecond():

    item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 10, 49)
    return item



@pytest.mark.test_BackstagePassesSecond
def test_BackstagePassesSecond(stocktakingSecond):

    # ITEM: Backstage Passes (Second)
    
    dayOne        = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 9, 50)
    dayTwo        = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 8, 50)
    dayThree      = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 7, 50)
    dayFive       = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 5, 50)
    dayTen        = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 5, 35)
    dayFifteen    = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", -5, 0)
    dayTwenty     = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", -10, 0)
    dayTwentyFive = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", -15, 0)
    dayThirty     = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", -20, 0)


    stocktakingSecond.updateQuality()
    assert repr(dayOne) == repr(stocktakingSecond)

    stocktakingSecond.updateQuality()
    assert repr(dayTwo) == repr(stocktakingSecond)

    stocktakingSecond.updateQuality()
    assert repr(dayThree) == repr(stocktakingSecond)

    stocktakingSecond.updateQuality()
    assert repr(dayFive) == repr(stocktakingSecond)

    stocktakingSecond.updateQuality()
    assert repr(dayTen) == repr(stocktakingSecond)

    stocktakingSecond.updateQuality()
    assert repr(dayFifteen) == repr(stocktakingSecond)

    stocktakingSecond.updateQuality()
    assert repr(dayTwenty) == repr(stocktakingSecond)

    stocktakingSecond.updateQuality()
    assert repr(dayTwentyFive) == repr(stocktakingSecond)

    stocktakingSecond.updateQuality()
    assert repr(dayThirty) == repr(stocktakingSecond)






@pytest.fixture
def stocktakingThird():

    item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 5, 49)
    return item



@pytest.mark.test_BackstagePassesThird
def test_BackstagePassesThird(stocktakingThird):

    # ITEM: Backstage Passes (Third)
    
    dayOne        = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 4, 50)
    dayTwo        = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 3, 50)
    dayThree      = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 2, 50)
    dayFive       = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 0, 50)
    dayTen        = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", -5, 0)
    dayFifteen    = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", -10, 0)
    dayTwenty     = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", -15, 0)
    dayTwentyFive = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", -20, 0)
    dayThirty     = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", -25, 0)


    stocktakingThird.updateQuality()
    assert repr(dayOne) == repr(stocktakingThird)

    stocktakingThird.updateQuality()
    assert repr(dayTwo) == repr(stocktakingThird)

    stocktakingThird.updateQuality()
    assert repr(dayThree) == repr(stocktakingThird)

    stocktakingThird.updateQuality()
    assert repr(dayFive) == repr(stocktakingThird)

    stocktakingThird.updateQuality()
    assert repr(dayTen) == repr(stocktakingThird)

    stocktakingThird.updateQuality()
    assert repr(dayFifteen) == repr(stocktakingThird)

    stocktakingThird.updateQuality()
    assert repr(dayTwenty) == repr(stocktakingThird)

    stocktakingThird.updateQuality()
    assert repr(dayTwentyFive) == repr(stocktakingThird)

    stocktakingThird.updateQuality()
    assert repr(dayThirty) == repr(stocktakingThird)