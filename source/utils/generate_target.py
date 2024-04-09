from pandas import DataFrame
import pandas as pd
from source.utils.abstract_classes import GenerateTarget

class MeanDifferenceThreshold(GenerateTarget):
    def __init__(self, days: int, window: int, threshold: float) -> None:
        """Classifies based if the rolling mean of size *window* *days* days ahead rose or fell above a threshold
        """
        self.days = days
        self.window = window
        self.threshold = threshold

    def generate_target(self, data: DataFrame) -> DataFrame:
        data['target'] = data['Open'].rolling(self.window,center=True).mean()
        data['target'] = data['target'].shift(-self.days)
        def compute_target(row):
            if row['target'] > (1+self.threshold)*row['Open']:
                return 1
            if row['target'] < (1-self.threshold)*row['Open']:
                return -1
            if pd.isna(row['target']):
                return float('nan')
            return 0
        data['target'] = data.apply(compute_target,axis=1)
        data = data.dropna()
        return data
    
class MeanDifferenceBinary(GenerateTarget):
    def __init__(self, days: int, window: int) -> None:
        """Classifies based if the rolling mean of size *window* *days* days ahead rose or fell
        """
        self.days = days
        self.window = window

    def generate_target(self, data: DataFrame) -> DataFrame:
        data['target'] = data['Open'].rolling(self.window,center=True).mean()
        data['target'] = data['target'].shift(-self.days)
        def compute_target(row):
            if row['target'] >= row['Open']:
                return 1
            if pd.isna(row['target']):
                return float('nan')
            return -1
        data['target'] = data.apply(compute_target,axis=1)
        data = data.dropna()
        return data
    
