import time
import pandas as pd
from abstract import Check


def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        func(*args, **kwargs)
        end=time.time()
        print(f"Time taken: {end-start} seconds.")
    return wrapper

class CheckingFramework:
    def __init__(self) -> None:
        pass

    @timer
    def run(self, checks: list[Check], df: pd.DataFrame) -> str:
        for check in checks:
            print(check.check(df))
