import pytest

@pytest.fixture
def sample_data():
    print("set up: Test data")
    data = {"name": "Alice","age": 30}
    yield data
    print("clean up the data")

def Test_Sample(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
    print("Test executed Successfully")


