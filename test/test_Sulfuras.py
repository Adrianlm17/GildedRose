from src.domain.sulfuras import *

import pytest 





@pytest.fixture
def stocktakingPositive():

    item = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    return item



@pytest.mark.test_SulfurasPositive
def test_SulfurasPositive(stocktakingPositive):

    # ITEM: Sulfuras, Hand of Ragnaros (First)
    
    dayOne        = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    dayTwo        = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    dayThree      = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    dayFive       = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    dayTen        = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    dayFifteen    = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    dayTwenty     = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    dayTwentyFive = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    dayThirty     = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)


    stocktakingPositive.updateQuality()
    assert repr(dayOne) == repr(stocktakingPositive)

    stocktakingPositive.updateQuality()
    assert repr(dayTwo) == repr(stocktakingPositive)

    stocktakingPositive.updateQuality()
    assert repr(dayThree) == repr(stocktakingPositive)

    stocktakingPositive.updateQuality()
    assert repr(dayFive) == repr(stocktakingPositive)

    stocktakingPositive.updateQuality()
    assert repr(dayTen) == repr(stocktakingPositive)

    stocktakingPositive.updateQuality()
    assert repr(dayFifteen) == repr(stocktakingPositive)

    stocktakingPositive.updateQuality()
    assert repr(dayTwenty) == repr(stocktakingPositive)

    stocktakingPositive.updateQuality()
    assert repr(dayTwentyFive) == repr(stocktakingPositive)

    stocktakingPositive.updateQuality()
    assert repr(dayThirty) == repr(stocktakingPositive)





@pytest.fixture
def stocktakingNegative():

    item = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
    return item


@pytest.mark.test_SulfurasNegative
def test_SulfurasNegative(stocktakingNegative):

    # ITEM: Sulfuras, Hand of Ragnaros (Second)
    
    dayOne        = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
    dayTwo        = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
    dayThree      = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
    dayFive       = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
    dayTen        = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
    dayFifteen    = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
    dayTwenty     = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
    dayTwentyFive = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
    dayThirty     = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)


    stocktakingNegative.updateQuality()
    assert repr(dayOne) == repr(stocktakingNegative)

    stocktakingNegative.updateQuality()
    assert repr(dayTwo) == repr(stocktakingNegative)

    stocktakingNegative.updateQuality()
    assert repr(dayThree) == repr(stocktakingNegative)

    stocktakingNegative.updateQuality()
    assert repr(dayFive) == repr(stocktakingNegative)

    stocktakingNegative.updateQuality()
    assert repr(dayTen) == repr(stocktakingNegative)

    stocktakingNegative.updateQuality()
    assert repr(dayFifteen) == repr(stocktakingNegative)

    stocktakingNegative.updateQuality()
    assert repr(dayTwenty) == repr(stocktakingNegative)

    stocktakingNegative.updateQuality()
    assert repr(dayTwentyFive) == repr(stocktakingNegative)

    stocktakingNegative.updateQuality()
    assert repr(dayThirty) == repr(stocktakingNegative)