from abc import ABC,abstractmethod
from pandas import DataFrame
from enum import Enum

class Signal(Enum):
    BUY = 1
    SELL = -1
    HOLD = 0

class AllocationModel(ABC):
    @abstractmethod
    def trade_order(self, direction:Signal, features: DataFrame, usd: float, btc: float) -> float:
        """Decides how much to trade for, in btc
        """

    def __call__(self, direction:Signal, features: DataFrame, usd: float, btc: float) -> float:
        return self.trade_order(direction, features, usd, btc)
    
class SignalModel(ABC):
    @abstractmethod
    def trade_signal(self, features: DataFrame, usd: float, btc: float) -> Signal:
        """Returns a signal for the trade
        """

    def __call__(self, features: DataFrame, usd: float, btc: float) -> Signal:
        return self.trade_signal(features,usd,btc)

class MachineLearningSignal(Signal):
    """Base class for models that use Machine Learning to decide wether to buy, sell or hold
    """
    @abstractmethod
    def train_model(self, training_data: DataFrame,**kwargs) -> None:
        """Trains a machine learning model
        """

    @abstractmethod
    def predict(self, features: DataFrame) -> float:
        """Predicts on one or multiple datapoints
        """
