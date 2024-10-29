import pytest

@pytest.mark.login
def test_regression():
    print("test_regression")

@pytest.mark.login
def test_sanity():
    print("test_sanity")

@pytest.mark.settings
def test_functional():
    print("test_functional")

@pytest.mark.settings
def test_api():
    print("test_api")

@pytest.mark.skip(reason="skipping as test taking longer time")
def test_api():
    print("test_api")

@pytest.mark.skipif(os.name, reason="skipping as test taking longer time")
def test_api():
    print("test_api" + os.name)