from calculator import add

def test_add():
    assert add(1, 1) == 2
    assert add(1, -1) == 0


if __name__ == "__main__":
    test_add()
