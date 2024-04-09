from pandas import DataFrame
from source.models.abstract_classes import AllocationModel, Signal
from source.models.central_model import PRICE_COLUMN

class AllInAllOut(AllocationModel):
    def trade_order(self, direction: Signal, features: DataFrame, usd: float, btc: float,) -> float:
        if direction == Signal.HOLD:
            return 0
        if direction == Signal.BUY:
            return self.usd/features[PRICE_COLUMN] # Buy all in
        return -self.btc # Sell all