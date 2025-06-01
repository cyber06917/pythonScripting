from twttr import shorten
import pytest


def test_shorten():
    assert shorten("lalit kumar") == "llt kmr"
    assert shorten("17") == "17"
    assert shorten("LALIT KUMAR") == "LLT KMR"
    





