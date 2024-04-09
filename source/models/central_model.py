from abstract_classes import SignalModel, AllocationModel
from pandas import DataFrame

STARTING_MONEY = 100
NEGATIVE_TOLERANCE = -1E-7
PRICE_COLUMN = 'Open'

class TradingModel():
    """Base class for models that will make trades
    """
    def __init__(self,signal_model: SignalModel, allocation_model: AllocationModel) -> None:
        self.usd = STARTING_MONEY
        self.btc = 0
        self.signal_model = signal_model
        self.allocation_model = allocation_model

    def __call__(self, features: DataFrame) -> None:
        return self.run_model(features)

    def update_reserves(self, trade:float, price:float) -> None:
        """"Updates usd and btc amount
        """
        self.usd -= trade*price
        self.btc += trade

    def run_model(self, features: DataFrame) -> None:
        """"Obtains signal, uses the signal to make a trade, and updates reserves
        """
        signal = self.signal_model(features,self.usd,self.btc)
        trade = self.allocation_model(signal,features,self.usd,self.btc)
        self.update_reserves(trade,features[PRICE_COLUMN])
    
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
