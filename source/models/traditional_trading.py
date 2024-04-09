from source.models.abstract_classes import SignalModel, Signal
from source.models.central_model import PRICE_COLUMN

class BuyAtSellAt(SignalModel):
    def __init__(self,buy_price=40_000,sell_price=60_000) -> None:
        super().__init__()
        self.buy_price = buy_price
        self.sell_price = sell_price
    def trade_signal(self, features,usd,btc) -> Signal:
        price = features[PRICE_COLUMN]
        if price >= self.sell_price:
            return Signal.SELL
        if price <= self.buy_price:
            return Signal.BUY
        return Signal.HOLD
