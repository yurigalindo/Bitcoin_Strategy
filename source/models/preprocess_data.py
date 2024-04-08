from pandas import DataFrame
from source.models.abstract_classes import DataPreprocessing

class ComposePreprocessing(DataPreprocessing):
    def __init__(self,steps: list = None, drop_na: bool = True):
        if steps:
            self.steps = steps
        else:
            self.steps = []
        self.drop_na = drop_na

    def add_step(self, step: DataPreprocessing):
        self.steps.append(step)

    def preprocess_data(self, data: DataFrame) -> DataFrame:
        for step in self.steps:
            data = step(data)
        if self.drop_na:
            data = data.dropna()
        return data

class ShiftFeatures(DataPreprocessing):
    def __init__(self, shifts: list, column: str = 'Open', drop_na: bool = False):
        self.shifts = shifts
        self.column = column
        self.drop_na = drop_na
    def preprocess_data(self, data: DataFrame) -> DataFrame:
        for shift in self.shifts:
            data[f'{self.column}_{shift}'] = data[self.column].shift(shift) 
        if self.drop_na:
            data = data.dropna()
        return data
    
class RollingMean(DataPreprocessing):
    def __init__(self, day_lengths: list, column: str = 'Open', drop_na: bool = False):
        self.lengths = day_lengths
        self.column = column
        self.drop_na = drop_na
    def preprocess_data(self, data: DataFrame) -> DataFrame:
        for length in self.lengths:
            data[f'{self.column}_{length}_mean'] = data[self.column].rolling(length).mean()
        if self.drop_na:
            data = data.dropna()
        return data
        