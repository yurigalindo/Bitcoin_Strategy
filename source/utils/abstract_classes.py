from abc import ABC, abstractmethod
from pandas import DataFrame

class DataPreprocessing(ABC):
    @abstractmethod
    def preprocess_data(self, data: DataFrame) -> DataFrame:
        """Pre-processes data to add features
        """

    def __call__(self, data: DataFrame) -> DataFrame:
        return self.preprocess_data(data)
    
class GenerateTarget(ABC):
    @abstractmethod
    def generate_target(self, data: DataFrame) -> DataFrame:
        """Adds a column 'target' to the dataframe
        """

    def validate_data(self, data: DataFrame) -> None:
        """Validates that the target column is adequate for classification
        """
        assert 'target' in data.columns
        assert len(data['target'].unique())

    def __call__(self, data: DataFrame) -> DataFrame:
        processed_data = self.generate_target(data)
        self.validate_data(processed_data)
        return processed_data