import pandas as pd
import yaml
from framework import CheckingFramework
from neg_col import NegativeColCheck
from neg_row import NegativeRowCheck
from sheet_sum import SheetSumCheck
from sum_eq_val import SumEqualValCheck


if __name__ == "__main__":
    checks = [NegativeColCheck(),NegativeRowCheck(),SheetSumCheck(),SumEqualValCheck(4)]  # user chg this
    # with open("./config/simple.yaml") as file:
    #     try:
    #         checks = yaml.safe_load(file)
    #     except yaml.YAMLError as exc:
    #         print(exc)
    # print(checks)

    framework = CheckingFramework()
    # framework.run(checks, pd.read_excel("Book2.xlsx"))
    framework.run(checks, pd.DataFrame([[1, -2, 3, 4, 5], [2, -1, 3, 3, 7], [1, 1, 1, 1, 1]]))

# 1. in 'poetry-demo' file, type 'poetry install' in terminal
# 2. in 'poetry_demo' file, type 'poetry run python test.py' in terminal to run