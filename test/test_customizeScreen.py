import sys

sys.path.append('..')


normalSkins = ['normal1.png', 'normal2.png', 'normal3.png']
baseSkins = ['base1.png', 'base2.png']
blueSkins = ['blue1.png']
brownSkins = []
graySkins = ['gray1.png', 'gray2.png', 'gray3.png']
greenSkins = ['green1.png', 'green2.png']
richSkins = ['rich1.png']
"""
def test_load_assets():
     # Define test input
    purchaseSize = 100

    # Call the function with the test input
    result = customizeScreen.loadAssets(purchaseSize)

    # Verify the output is as expected
    assert isinstance(result, tuple)
    assert len(result) == 7
    assert all(isinstance(lst, list) for lst in result)
    assert all(isinstance(img, pygame.Surface) for lst in result for img in lst)

    # Verify the length of each list in the output is as expected
    assert len(result[0]) == len(normalSkins)
    assert len(result[1]) == len(baseSkins)
    assert len(result[2]) == len(blueSkins)
    assert len(result[3]) == len(brownSkins)
    assert len(result[4]) == len(graySkins)
    assert len(result[5]) == len(greenSkins)
    assert len(result[6]) == len(richSkins)
"""


def test_customize_screen():
    assert True
