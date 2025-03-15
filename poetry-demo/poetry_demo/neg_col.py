import pandas as pd

from poetry_demo.abstract import Check


class NegativeColCheck(Check):
    def check(self, df: pd.DataFrame) -> str:
        negative_cols = []
        for col in df.columns:
            # print(df[col].tolist())  # Each column as a list
            column_list = df[col].tolist()
            for num in column_list:
                if num < 0:
                    negative_cols.append(str(col))
                    break
        if len(negative_cols) == 0:
            return "No columns with negative values."
        elif len(negative_cols) == 1:
            return f"Column {negative_cols[0]} has negative values in it."
        else:
            return f"Columns {','.join(negative_cols)} have negative values in it."
