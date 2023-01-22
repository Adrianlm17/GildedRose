from src.main import *

import pytest 





@pytest.fixture
def stocktakingDexterity():

    item = Conjured("+5 Dexterity Vest", 10, 20)
    return item



@pytest.mark.test_ConjuredDexterity
def test_ConjuredDexterity(stocktakingDexterity):

    # ITEM: +5 Dexterity Vest
    
    dayOne        = Conjured("+5 Dexterity Vest", 9, 18)
    dayTwo        = Conjured("+5 Dexterity Vest", 8, 16)
    dayThree      = Conjured("+5 Dexterity Vest", 7, 14)
    dayFive       = Conjured("+5 Dexterity Vest", 5, 10)
    dayTen        = Conjured("+5 Dexterity Vest", 0, 0)
    dayFifteen    = Conjured("+5 Dexterity Vest", -5, 0)
    dayTwenty     = Conjured("+5 Dexterity Vest", -10, 0)
    dayTwentyFive = Conjured("+5 Dexterity Vest", -15, 0)
    dayThirty     = Conjured("+5 Dexterity Vest", -20, 0)


    stocktakingDexterity.updateQuality()
    assert repr(dayOne) == repr(stocktakingDexterity)

    stocktakingDexterity.updateQuality()
    assert repr(dayTwo) == repr(stocktakingDexterity)

    stocktakingDexterity.updateQuality()
    assert repr(dayThree) == repr(stocktakingDexterity)

    stocktakingDexterity.updateQuality()
    assert repr(dayFive) == repr(stocktakingDexterity)

    stocktakingDexterity.updateQuality()
    assert repr(dayTen) == repr(stocktakingDexterity)

    stocktakingDexterity.updateQuality()
    assert repr(dayFifteen) == repr(stocktakingDexterity)

    stocktakingDexterity.updateQuality()
    assert repr(dayTwenty) == repr(stocktakingDexterity)

    stocktakingDexterity.updateQuality()
    assert repr(dayTwentyFive) == repr(stocktakingDexterity)

    stocktakingDexterity.updateQuality()
    assert repr(dayThirty) == repr(stocktakingDexterity)





@pytest.fixture
def stocktakingMana():

    item = Conjured("Conjured Mana Cake", 3, 6)
    return item


@pytest.mark.test_ConjuredMana
def test_ConjuredMana(stocktakingMana):

    # ITEM: Conjured Mana Cake
    
    dayOne        = Conjured("Conjured Mana Cake", 2, 4)
    dayTwo        = Conjured("Conjured Mana Cake", 1, 2)
    dayThree      = Conjured("Conjured Mana Cake", 0, 0)
    dayFive       = Conjured("Conjured Mana Cake", -2, 0)
    dayTen        = Conjured("Conjured Mana Cake", -7, 0)
    dayFifteen    = Conjured("Conjured Mana Cake", -12, 0)
    dayTwenty     = Conjured("Conjured Mana Cake", -17, 0)
    dayTwentyFive = Conjured("Conjured Mana Cake", -22, 0)
    dayThirty     = Conjured("Conjured Mana Cake", -27, 0)


    stocktakingMana.updateQuality()
    assert repr(dayOne) == repr(stocktakingMana)

    stocktakingMana.updateQuality()
    assert repr(dayTwo) == repr(stocktakingMana)

    stocktakingMana.updateQuality()
    assert repr(dayThree) == repr(stocktakingMana)

    stocktakingMana.updateQuality()
    assert repr(dayFive) == repr(stocktakingMana)

    stocktakingMana.updateQuality()
    assert repr(dayTen) == repr(stocktakingMana)

    stocktakingMana.updateQuality()
    assert repr(dayFifteen) == repr(stocktakingMana)

    stocktakingMana.updateQuality()
    assert repr(dayTwenty) == repr(stocktakingMana)

    stocktakingMana.updateQuality()
    assert repr(dayTwentyFive) == repr(stocktakingMana)

    stocktakingMana.updateQuality()
    assert repr(dayThirty) == repr(stocktakingMana)