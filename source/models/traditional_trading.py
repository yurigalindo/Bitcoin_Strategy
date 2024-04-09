from source.models.abstract_classes import BuySellModel, Signal

class BuyAtSellAt(BuySellModel):
    def __init__(self,buy_price=40_000,sell_price=60_000) -> None:
        super().__init__()
        self.buy_price = buy_price
        self.sell_price = sell_price
    def trade_signal(self, price: float) -> Signal:
        if price >= self.sell_price:
            return Signal.SELL
        if price <= self.buy_price:
            return Signal.BUY
        return Signal.HOLD
    def trade_order(self, direction: Signal, price: float) -> float:
        if direction == Signal.HOLD:
            return 0
        if direction == Signal.BUY:
            return self.usd/price # Buy all in
        return -self.btc # Sell all
