import pandas as pd
from abstract import Check


class SumEqualValCheck(Check):
    def __init__(self, entered_val: int) -> None:
        self.entered_val = entered_val

    def check(self, df: pd.DataFrame) -> str:
        match_cols = []
        for col in df.columns:
            column_list = df[col].tolist()
            # print(column_list)
            sum = 0
            for num in column_list:
                sum += num
            # print(sum)
            if sum == self.entered_val:
                match_cols.append(col)

        if len(match_cols) == 0:
            return f"No columns with sum equal to {self.entered_val}."
        elif len(match_cols) == 1:
            return f"Sum of values in column {match_cols[0]} is equals to {self.entered_val}."
        else:
            return f"Sum of values in columns {','.join(match_cols)} is equals to {self.entered_val}."
