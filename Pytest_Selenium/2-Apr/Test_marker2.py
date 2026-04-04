import pytest

@pytest.mark.parametrize('a,b',[(1,2),(2,3)])
def test_add(a,b):
    print(a+b)

# @pytest.mark.akshay         # this is custom marker
# @pytest.mark.smoke
@pytest.mark.skip
def test_print():
    print("Skip test")

@pytest.mark.skipif(True, reason="Skip test")     # we have control to skip by giving True and False, if skipping then it will give reason
def test_print2():
    print("Skip if test")

# driver.close()
#driver.quit()