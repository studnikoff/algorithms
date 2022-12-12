import pytest
from bst import BST

@pytest.fixture
def bst():
    case = [10,5,15,3,7,13,17,1,11,14,16,18,12]
    bst = BST()
    for i in case:
        bst.put(key=i, value=f"value for {i}")
    return bst

class TestBST:
    @pytest.mark.parametrize("inp, expected", [
                                (5, "value for 5"),
                                (10, "value for 10"),
                                (100, None),
                                (-1, None)
                                ])
    def test_get(self, bst, inp, expected):
        assert bst.get(inp) == expected

    def test_min(self, bst):
        assert bst.min().key == 1

    @pytest.mark.parametrize("inp, expected", [
                                (5, 5),
                                (9, 7),
                                (100, 18),
                                (-1, None)
                                ])
    def test_floor(self, bst, inp, expected):
        assert bst.floor(key=inp) == expected
        
    