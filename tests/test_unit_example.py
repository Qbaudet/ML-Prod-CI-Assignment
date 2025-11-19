from app import add

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(0, 1) == 2