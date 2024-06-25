#!/usr/bin/env python
# coding: utf-8
"""Tests de les funcions del mòdul load_data

Comprova les sortides de les funcions clean_csv i rename_col.
"""
import unittest
import pandas as pd
from usfirearms import load_data

data = pd.read_csv("../data/nics-firearm-background-checks.csv")

class TestLoadData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Loading dataset")
        #cls._df = pd.read_csv("../data/nics-firearm-background-checks.csv")
        cls._clean = load_data.clean_csv(data)

    def test_selected_columns(self):
        print("Test clean_csv")
        columns = list(self._clean.columns)
        test_columns = ["month", "state", "permit", "handgun", "long_gun"]
        self.assertEqual(columns, test_columns)

    def test_rename_column(self):
        print("Test rename_col")
        columns = list(load_data.rename_col(self._clean).columns)
        test_columns = ["month", "state", "permit", "handgun", "longgun"]
        self.assertEqual(columns, test_columns)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)
