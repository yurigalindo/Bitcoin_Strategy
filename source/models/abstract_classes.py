from abc import ABC,abstractmethod
from typing import Any
from pandas import DataFrame
from enum import Enum

STARTING_MONEY = 100
NEGATIVE_TOLERANCE = -1E-7

class Signal(Enum):
    BUY = 1
    SELL = -1
    HOLD = 0

class BuySellModel(ABC):
    """Base class for models that will make trades
    """
    def __init__(self) -> None:
        self.usd = STARTING_MONEY
        self.btc = 0

    def __call__(self, price: float) -> None:
        return self.run_model(price)

    def update_reserves(self, trade:float, price:float) -> None:
        """"Updates usd and btc amount
        """
        self.usd -= trade*price
        self.btc += trade

    def run_model(self, price: float) -> None:
        """"Obtains signal, uses the signal to make a trade, and updates reserves
        """
        signal = self.trade_signal(price)
        trade = self.trade_order(signal, price)
        self.update_reserves(trade,price)

    def reset_model(self) -> None:
        """Resets model to re-start trading from scratch
        """
        self.usd = STARTING_MONEY
        self.btc = 0

    @abstractmethod
    def trade_signal(self, price:float ) -> Signal:
        """Returns a signal for the trade
        """
    
    @abstractmethod
    def trade_order(self, direction:Signal, price: float) -> float:
        """Decides how much to trade for, in btc
        """

    @property
    def usd(self):
        return self._usd
    
    @usd.setter
    def usd(self,new_usd: float):
        if new_usd < NEGATIVE_TOLERANCE:
            raise ValueError(f"Can't set negative value {new_usd} for dollar reserve")
        self._usd = new_usd
        
    @property
    def btc(self):
        return self._btc
    
    @btc.setter
    def btc(self,new_btc: float):
        if new_btc < NEGATIVE_TOLERANCE:
            raise ValueError(f"Can't set negative value {new_btc} for bitcoin allocation")
        self._btc = new_btc
        
class MachineLearningModel(BuySellModel):
    """Base class for trading models that use Machine Learning
    """
    @abstractmethod
    def train_model(self, training_data: DataFrame,**kwargs) -> None:
        """Trains a machine learning model
        """

    @abstractmethod
    def predict(self, row: DataFrame) -> float:
        """Predicts on a datapoint
        """
        
    @abstractmethod
    def reset_training(self) -> None:
        """Resets training of the model
        """