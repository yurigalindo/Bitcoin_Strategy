from source.models.abstract_classes import Signal, SignalModel

class TrailLoss(SignalModel):
    def __init__(self,ratio_tolerance: float,ratio_sell: float,threshold: float = None,when_to_buy: float = 0.33):
        super().__init__()
        self.tolerance = ratio_tolerance
        self.ratio_sell = ratio_sell
        self.buy = when_to_buy
        self.threshold = threshold
        self.peak = None
        self.buy_price = 0

    def trade_signal(self, price: float) -> Signal:
        if self.peak is None:
            if self.buy_price == 0:
                self.peak = price
                self.buy_price = price
                return Signal.BUY
            if self.threshold is None or price>self.buy_price*(self.threshold):
                self.peak = price
                return Signal.HOLD
            else:
                return Signal.HOLD
        if price>self.peak:
            # Price is growing
            self.peak = price
            return Signal.HOLD
        if price<self.peak*self.buy:
            # Price is low enough to buy
            self.buy_price = price
            self.peak = None # Reset peak
            return Signal.BUY
        if price<self.peak*(1-self.tolerance):
            # Price dropped enough to sell
            return Signal.SELL
        return Signal.HOLD
    
        

