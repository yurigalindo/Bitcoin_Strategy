import pandas as pd
import matplotlib.pyplot as plt
from source.models.parent_class import BuySellModel

class BacktestTradeModels():
    def __init__(self,csv: str, start_date = None, end_date = None):
        self.data = pd.read_csv(csv)
        if start_date:
            self.data = self.data[self.data['Date'] >= start_date]
        if end_date:
            self.data = self.data[self.data['Date'] <= end_date]
    
    def __call__(self, model: BuySellModel) -> float:
        self.plot(model)
        model.reset_model()
        return self.backtest(model)

    def plot(self, model: BuySellModel) -> None:
        self.plot_signals(model)
        self.plot_btc(model)
        self.plot_usd(model)

    def backtest(self, model: BuySellModel) -> float:
        model.reset_model()
        for _,row in self.data.iterrows():
            model.run_model(row['Open'])
        if model.btc != 0:
            # Sell remaining btc
            model.usd = model.btc*row['Open']
            model.btc = 0
        return model.usd
    
    def plot_signals(self, model: BuySellModel) -> None:
        model.reset_model()
        for i,row in self.data.iterrows():
            signal = model.trade_signal(row['Open']).value
            mark = ['.','^','v'][signal]
            color = ['gray','green','red'][signal]
            plt.title("Buy or Sell Signals")
            plt.plot(i,row['Open'],color=color,marker=mark)
        plt.figure()
    
    def plot_usd(self, model: BuySellModel) -> None:
        model.reset_model()
        usd = []
        for _,row in self.data.iterrows():
            model.run_model(row['Open'])
            usd.append(model.usd)
        plt.title("USD reserve evolution")
        plt.plot(usd)
        plt.figure()

    def plot_btc(self, model: BuySellModel) -> None:
        model.reset_model()
        btc = []
        for _,row in self.data.iterrows():
            model.run_model(row['Open'])
            btc.append(model.btc)
        plt.title("Allocated BTC evolution")
        plt.plot(btc)
        plt.figure()