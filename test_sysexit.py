import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()

# runs with this command:
# pytest -q test_sysexit.py