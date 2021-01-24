# test_with_unittest.py

from simpleclass import banner

def test_add():
    test = banner.hello_world()
    assert test.add(1,2) == 3
