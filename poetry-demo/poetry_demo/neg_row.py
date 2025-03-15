import pandas as pd
from abstract import Check


class NegativeRowCheck(Check):
    # find rows with negative num in it
    def check(self, df: pd.DataFrame) -> str:
        row_value_list = df.values.tolist()
        # print(row_value_list)
        negative_rows = []
        for index, list in enumerate(row_value_list):
            for num in list:
                if num < 0:
                    negative_rows.append(str(index))
                    break
        if len(negative_rows) == 0:
            return "No rows with negative values."
        elif len(negative_rows) == 1:
            return f"Row {negative_rows[0]} has negative values in it."
        else:
            return f"Rows {','.join(negative_rows)} have negative values in it."
