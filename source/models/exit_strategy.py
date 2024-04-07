from source.models.parent_class import BuySellModel
from source.models.parent_class import Signal

class TrailLoss(BuySellModel):
    def __init__(self,ratio_tolerance: float,ratio_sell: float,when_to_buy: float = 0.2):
        super().__init__()
        self.tolerance = ratio_tolerance
        self.ratio_sell = ratio_sell
        self.buy = when_to_buy
        self.peak = None

    def reset_model(self) -> None:
        super().reset_model()
        self.peak = None
    
    def trade_signal(self, price: float) -> Signal:
        if self.peak is None:
            self.peak = price
            return Signal.BUY
        if price>self.peak:
            # Price is growing
            self.peak = price
            return Signal.HOLD
        if price<self.peak*self.buy:
            # Price is low enough to buy
            return Signal.BUY
        if price<self.peak*(1-self.tolerance):
            # Price dropped enough to sell
            return Signal.SELL
        return Signal.HOLD
    
    def trade_order(self, direction: Signal, price: float) -> float:
        if direction == Signal.HOLD:
            return 0
        if direction == Signal.BUY:
            #self.peak = None
            return self.usd/price # Buy all in
        return -self.btc*self.ratio_sell # Sell defined ratio
    
    
        

