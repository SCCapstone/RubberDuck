import sys

from views import customizeScreen
from assets import values

sys.path.append('..')



def test_loadAssets():
    # Test that the assets are loaded
    purchaseSize = int(values.screenX * .1504)
    customizeScreen.loadAssets(purchaseSize)
    assert customizeScreen.ownedSkins is not None
    assert customizeScreen.ownedBackgrounds is not None
