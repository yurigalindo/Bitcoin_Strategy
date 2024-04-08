from pandas import DataFrame
from source.models.abstract_classes import DataPreprocessing

class ComposePreprocessing(DataPreprocessing):
    def __init__(self,steps: list = None):
        if steps:
            self.steps = steps
        else:
            self.steps = []

    def add_step(self, step: DataPreprocessing):
        self.steps.append(step)

    def preprocess_data(self, data: DataFrame) -> DataFrame:
        for step in self.steps:
            data = step(data)
        return data

class ShiftFeatures(DataPreprocessing):
    def __init__(self, shifts: list, column_to_shift: str = 'Open', drop_na:bool = True):
        self.shifts = shifts
        self.column_to_shift = column_to_shift
        self.drop_na = drop_na
    def preprocess_data(self, data: DataFrame) -> DataFrame:
        for shift in self.shifts:
            data[f'{self.column_to_shift}_{shift}'] = data[self.column_to_shift].shift(shift) 
        if self.drop_na:
            data = data.dropna()
        return data
        