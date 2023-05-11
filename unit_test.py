import os
import unittest
import pathlib as pl
TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'alice.txt')


class BaseTestClass(unittest.TestCase):
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    def assertIsEmpty(self, path):
        if os.path.getsize(path) == 0:
            raise AssertionError("File is empty: %s" % str(path))


class ActualTest(BaseTestClass):
    def test(self):
        path = pl.Path(TESTDATA_FILENAME)
        self.assertIsFile(path)

    def test2(self):
        path = pl.Path(TESTDATA_FILENAME)
        self.assertIsEmpty(path)
