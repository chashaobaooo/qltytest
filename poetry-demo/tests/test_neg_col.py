import pandas as pd
import pytest

from poetry_demo.neg_col import NegativeColCheck


@pytest.fixture #initialise pytest fn
def neg_col_check():
    return NegativeColCheck()


class TestNegColCheck:
    def test_no_neg_col(self, neg_col_check):
        input_list = [[1, 2, 3, 4, 5], [2, 1, 3, 3, 7], [1, 1, 1, 1, 1]]
        df = pd.DataFrame(input_list)
        assert neg_col_check.check(df) == "No columns with negative values."

    def test_one_neg_col(self, neg_col_check):
        input_list = [[1, -2, 3, 4, 5], [2, -1, 3, 3, 7], [1, 1, 1, 1, 1]]
        df = pd.DataFrame(input_list)
        assert neg_col_check.check(df) == "Column 1 has negative values in it."

    def test_few_neg_col(self, neg_col_check):
        input_list = [[-1, -2, 3, 4, 5], [-2, 1, 3, 3, 7], [1, 1, 1, 1, 1]]
        df = pd.DataFrame(input_list)
        assert neg_col_check.check(df) == "Columns 0,1 have negative values in it."

# in 'tests' file, type 'poetry run pytest' in terminal to run tests