from abc import ABC, abstractmethod

import pandas as pd


class Check(ABC):
    @abstractmethod
    def check(self, df: pd.DataFrame) -> str:
        pass
