import pandas as pd
from abstract import Check


class SheetSumCheck(Check):
    # get sum of all num in excel
    def check(self, df: pd.DataFrame) -> str:
        sheet_sum = 0
        for col in df.columns:
            column_list = df[col].tolist()
            col_sum = 0
            for num in column_list:
                col_sum += num
            sheet_sum += col_sum
        return f"Sum of all numbers in the sheet is {sheet_sum}."
